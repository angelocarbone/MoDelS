from model.utils import Orientation, Axles, BoundingBox, Dynamics, LanePosition, TransitionDynamics
from model.enumerations import e_EntityType, e_DynamicsShapes, e_DynamicsDimension, e_ActionType
from model.actions import TeleportAction, AbsoluteSpeedAction
from model.knowledge_base import kb
from model.entities import Entity


def add_object_event(func):
    def wrapper(*args, **kwargs):
        res, entity_name = func(*args, **kwargs)

        if type(res).__name__ == "Event":
            actions = res.action
            for o in actions:
                o_action = o.action
                o_name = type(o_action).__name__

                if o_name == e_ActionType.AbsoluteSpeedAction.name:
                    entity_thing = kb.get_entity_from_cache(entity_name)
                    transition_dynamic = TransitionDynamics(e_DynamicsShapes.by_name(o_action.transition_dynamics.shape.name),
                                                            e_DynamicsDimension.by_name(o_action.transition_dynamics.dimension.name),
                                                            o_action.transition_dynamics.value)
                    action = AbsoluteSpeedAction('absolute_speed_action_' + entity_name, o_action.speed, transition_dynamic)
                    kb.assign_action(entity_thing, action)

    return wrapper


def add_init_action(func):
    def wrapper(*args, **kwargs):
        res, entity_name = func(*args, **kwargs)
        entity_thing = kb.get_entity_from_cache(entity_name)

        for o in res:
            o_name = type(o).__name__

            if o_name == e_ActionType.TeleportAction.name:
                position = o.position
                lane_id = position.lane_id
                offset = position.offset
                road_id = position.road_id
                s = position.s
                orient = position.orient
                h = orient.h
                p = orient.p
                r = orient.r
                ref = orient.ref

                # Assign teleport action to entity
                orientation = Orientation(h, p, r, ref)
                position = LanePosition(lane_id, offset, road_id, s, orientation)
                teleport_action = TeleportAction("teleport_action_" + entity_name, position)
                kb.assign_action(entity_thing, teleport_action)

            if o_name == e_ActionType.AbsoluteSpeedAction.name:
                # ***
                # AbsoluteSpeedAction
                #
                absoluteSpeedAction = o
                speed = absoluteSpeedAction.speed
                asa_transition_dynamics = absoluteSpeedAction.transition_dynamics
                dimension_class_name = asa_transition_dynamics.dimension.classname
                dimension_name = asa_transition_dynamics.dimension.name
                shape_class_name = asa_transition_dynamics.shape.classname
                shape_name = asa_transition_dynamics.shape.name
                value = asa_transition_dynamics.value
                # Assign absolute speed action to entity
                transition_dynamics = TransitionDynamics(e_DynamicsShapes.by_name(shape_name),
                                                         e_DynamicsDimension.by_name(dimension_name),
                                                         value)
                absolute_speed_action = AbsoluteSpeedAction("absolute_speed_action_" + entity_name, speed,
                                                            transition_dynamics)
                kb.assign_action(entity_thing, absolute_speed_action)

    return wrapper


def add_scenario_object(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)

        o = type(res).__name__

        if o == e_EntityType.Vehicle.name():
            _insert_vehicle(res)
        elif o == e_EntityType.Pedestrian.name():
            _insert_pedestrian(res)

    return wrapper


def _insert_vehicle(res):
    axles = res.axles
    front_axle_max_steer = axles.frontaxle.maxsteer
    front_axle_track_width = axles.frontaxle.track_width
    front_axle_wheel_diameter = axles.frontaxle.wheeldia
    front_axle_x_pos = axles.frontaxle.xpos
    front_axle_z_pos = axles.frontaxle.zpos

    rear_axle_max_steer = axles.rearaxle.maxsteer
    rear_axle_track_width = axles.rearaxle.track_width
    rear_axle_wheel_diameter = axles.rearaxle.wheeldia
    rear_axle_x_pos = axles.rearaxle.xpos
    rear_axle_z_pos = axles.rearaxle.zpos

    bounding_box_dimensions = res.boundingbox.boundingbox
    height = bounding_box_dimensions.height
    length = bounding_box_dimensions.length
    width = bounding_box_dimensions.width

    bounding_box_center = res.boundingbox.center
    x = bounding_box_center.x
    y = bounding_box_center.y
    z = bounding_box_center.z

    dynamics = res.dynamics
    max_acceleration = dynamics.max_acceleration
    max_deceleration = dynamics.max_deceleration
    max_speed = dynamics.max_speed

    mass = res.mass
    name = res.name

    vehicle_type = res.vehicle_type
    vehicle_type_class_name = vehicle_type.classname
    vehicle_type_name = vehicle_type.name

    # ***
    # Save in ontology
    #
    front_axle = Axles(front_axle_max_steer, front_axle_track_width, front_axle_wheel_diameter, front_axle_x_pos,
                       front_axle_z_pos)
    rear_axle = Axles(rear_axle_max_steer, rear_axle_track_width, rear_axle_wheel_diameter, rear_axle_x_pos,
                      rear_axle_z_pos)
    bounding_box = BoundingBox(height, length, width, x, y, z)
    dynamics_ = Dynamics(max_acceleration, max_deceleration, max_speed)

    e = Entity(name, mass, e_EntityType.Vehicle.Car, bounding_box, front_axle, rear_axle, dynamics_)
    kb.insert_entity(e)


def _insert_pedestrian(res):
    bounding_box_dimensions = res.boundingbox.boundingbox
    height = bounding_box_dimensions.height
    length = bounding_box_dimensions.length
    width = bounding_box_dimensions.width

    bounding_box_center = res.boundingbox.center
    x = bounding_box_center.x
    y = bounding_box_center.y
    z = bounding_box_center.z

    category = res.category
    category_class_name = category.classname
    category_name = category.name

    mass = res.mass
    name = res.name
    model = res.model

    # ***
    # Save in ontology
    #
    bounding_box = BoundingBox(height, length, width, x, y, z)
    e = Entity(name, mass, e_EntityType.Pedestrian.People, bounding_box)
    kb.insert_entity(e)

