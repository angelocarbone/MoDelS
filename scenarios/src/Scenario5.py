import os
from scenariogeneration import xosc, prettyprint

# create parameters
param_declaration = xosc.ParameterDeclarations()
param_declaration.add_parameter(xosc.Parameter('HostVehicle', xosc.ParameterType.string, 'car_white'))
param_declaration.add_parameter(xosc.Parameter('HostSpeed', xosc.ParameterType.double, 10.0))
param_declaration.add_parameter(xosc.Parameter('PedestrianSpeed', xosc.ParameterType.double, 1.5))

# create catalogs
catalog = xosc.Catalog()
catalog.add_catalog('VehicleCatalog', '../xosc/Catalogs/Vehicles')
catalog.add_catalog('RouteCatalog', '../xosc/Catalogs/Routes')

# create road
road = xosc.RoadNetwork(roadfile="../xodr/fabriksgatan.xodr", scenegraph="../models/fabriksgatan.osgb")

# create entities
ego_name = 'Ego'
pedestrian_name = 'Ped1'

entities = xosc.Entities()
entities.add_scenario_object(ego_name, xosc.CatalogReference('VehicleCatalog', '$HostVehicle'))

pedestrian_bounding_box = xosc.BoundingBox(0.5, 0.6, 1.8, 0.06, 0.0, 0.923)
pedestrian = xosc.Pedestrian(pedestrian_name, 'EPTa', 80, xosc.PedestrianCategory.pedestrian, pedestrian_bounding_box)

pedestrian.properties.add_property('control', 'internal')
pedestrian.properties.add_file('../models/walkman.osgb')
entities.add_scenario_object(pedestrian_name, pedestrian)

# create init

init = xosc.Init()

step_time = xosc.TransitionDynamics(xosc.DynamicsShapes.step, xosc.DynamicsDimension.time, 1)
# init.add_init_action(ego_name, xosc.TeleportAction(xosc.LanePosition(0, 0, 1, 0)))
# # init.add_init_action(ego_name, xosc.AbsoluteSpeedAction(param_declaration.parameters['HostSpeed'], step_time))
# init.add_init_action(ego_name, xosc.AbsoluteSpeedAction(10, step_time))

catalog_reference = xosc.CatalogReference('RoutesAtFabriksgatan', 'HostStraightRoute')
init.add_init_action(ego_name, xosc.AssignRouteAction(catalog_reference))
init.add_init_action(ego_name, xosc.TeleportAction(xosc.LanePosition(0, 0, 1, 0)))
init.add_init_action(ego_name, xosc.AbsoluteSpeedAction(10, step_time))

pedestrian_orientation = xosc.Orientation(0, 0, 0, xosc.ReferenceContext.relative)
init.add_init_action(pedestrian_name, xosc.TeleportAction(xosc.LanePosition(15, 0.5, 3, 0, pedestrian_orientation)))

# create an event for pedestrian

pedestrian_condition = xosc.EntityTrigger('ped_walk_event',
                                          0.0,
                                          xosc.ConditionEdge.rising,
                                          xosc.TraveledDistanceCondition(5),
                                          ego_name,
                                          xosc.TriggeringEntitiesRule.any)
p_trigger_condition = xosc.ConditionGroup()
p_trigger_condition.add_condition(pedestrian_condition)
pedestrian_event = xosc.Event('ped_event', xosc.Priority.overwrite, maxexecution=1)
pedestrian_event.add_trigger(p_trigger_condition)

pedestrian_transition_dynamic = xosc.TransitionDynamics(xosc.DynamicsShapes.linear, xosc.DynamicsDimension.rate, 2)
# pedestrian_action_walk_speed = xosc.AbsoluteSpeedAction(param_declaration['PedestrianSpeed'], pedestrian_transition_dynamic)
pedestrian_action_walk_speed = xosc.AbsoluteSpeedAction(1.5, pedestrian_transition_dynamic)
pedestrian_event.add_action('walk_speed', pedestrian_action_walk_speed)

trajectory = xosc.Trajectory('ped_traj', False)
a_time = [0, 0, 0, 0, 0, 0]
positions = [
    xosc.LanePosition(15, 0.5, 3, 0, xosc.Orientation(0, 0, 0, xosc.ReferenceContext.relative)),
    xosc.LanePosition(10.5, 0.5, 3, 0, xosc.Orientation(0, 0, 0, xosc.ReferenceContext.relative)),
    xosc.LanePosition(10, 0.0, 3, 0, xosc.Orientation(1.57, 0, 0, xosc.ReferenceContext.relative)),
    xosc.LanePosition(10, 0.0, -3, 0, xosc.Orientation(4.71, 0, 0, xosc.ReferenceContext.relative)),
    xosc.LanePosition(9.5, -0.5, -3, 0, xosc.Orientation(3.14, 0, 0, xosc.ReferenceContext.relative)),
    xosc.LanePosition(0, -0.5, -3, 0, xosc.Orientation(3.14, 0, 0, xosc.ReferenceContext.relative)),
]
shape = xosc.Polyline(time=a_time, positions=positions)
trajectory.add_shape(shape)
pedestrian_action_walk_route = xosc.FollowTrajectoryAction(trajectory, xosc.FollowMode.position)
pedestrian_event.add_action('walk_route', pedestrian_action_walk_route)


pedestrian_maneuver = xosc.Maneuver('ped_maneuver')
pedestrian_maneuver.add_event(pedestrian_event)

pedestrian_maneuver_group = xosc.ManeuverGroup('ped_mangroup', 1, selecttriggeringentities=False)
pedestrian_maneuver_group.add_maneuver(pedestrian_maneuver)
pedestrian_maneuver_group.add_actor(pedestrian_name)


ego_condition = xosc.EntityTrigger('brake_Condition',
                                   0.0,
                                   xosc.ConditionEdge.rising,
                                   xosc.TimeToCollisionCondition(1.7, xosc.Rule.lessThan, True, True, pedestrian_name),
                                   ego_name,
                                   xosc.TriggeringEntitiesRule.any
                                   )
e_trigger_condition = xosc.ConditionGroup()
e_trigger_condition.add_condition(ego_condition)

ego_event = xosc.Event('brake_Event', xosc.Priority.overwrite, maxexecution=1)
ego_event.add_trigger(e_trigger_condition)

ego_transition_dynamic = xosc.TransitionDynamics(xosc.DynamicsShapes.linear, xosc.DynamicsDimension.rate, -5)
ego_action_brake = xosc.AbsoluteSpeedAction(0, ego_transition_dynamic)
ego_event.add_action('brake_Action', ego_action_brake)

ego_maneuver = xosc.Maneuver('brake_Maneuver')
ego_maneuver.add_event(ego_event)

ego_maneuver_group = xosc.ManeuverGroup('brake-for-ped_mangroup', maxexecution=1, selecttriggeringentities=False)
ego_maneuver_group.add_maneuver(ego_maneuver)
ego_maneuver_group.add_actor(ego_name)

start_trigger = xosc.ValueTrigger('ActStartCondition', 0.0, xosc.ConditionEdge.none, xosc.SimulationTimeCondition(0.0, xosc.Rule.greaterThan))

entity_condition = xosc.ReachPositionCondition(xosc.LanePosition(0, 0, -3, 0), 5.0)
stop_trigger = xosc.EntityTrigger('QuitCondition', 0.0, xosc.ConditionEdge.rising, entity_condition, pedestrian_name, xosc.TriggeringEntitiesRule.any)

act = xosc.Act('LTAPActNPC', starttrigger=start_trigger)
act.add_maneuver_group(ego_maneuver_group)
act.add_maneuver_group(pedestrian_maneuver_group)

# create the story
story = xosc.Story('LTAPStory')
story.add_act(act)
story_parameter = xosc.Parameter('owner', xosc.ParameterType.string, 'NPC')
story.parameter.add_parameter(story_parameter)

# create the storyboard
sb = xosc.StoryBoard(init, xosc.ValueTrigger('stop_simulation', 0, xosc.ConditionEdge.rising, xosc.SimulationTimeCondition(10, xosc.Rule.greaterThan), 'stop'))
sb.add_story(story)

# create the scenario
sce = xosc.Scenario('adapt_speed_example', 'Angelo Carboπe', param_declaration, entities=entities, storyboard=sb, roadnetwork=road, catalog=catalog)

# Print the resulting xml
prettyprint(sce.get_element())

# write the OpenSCENARIO file as xosc using current script name
sce.write_xml("xosc/" + os.path.basename(__file__).replace('.py', '.xosc'))

# uncomment the following lines to display the scenario using esmini
from scenariogeneration import esmini
esmini(sce, os.path.join('esmini'))