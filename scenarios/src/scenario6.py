import os
from scenariogeneration import xosc, prettyprint, ScenarioGenerator, esmini


class Scenario(ScenarioGenerator):

    def __init__(self):
        ScenarioGenerator.__init__(self)
        self._ego_name = 'Ego'
        self._pedestrian_name = 'Ped1'
        self._param_declaration = None
        self._catalog = None
        self._road = None
        self._entities = xosc.Entities()
        self._pedestrian_maneuver_group = None
        self._ego_maneuver_group = None
        self._act = None
        self._init = xosc.Init()
        self._story = None
        self._storyboard = None
        self._scenario = None

    def generate_scenario(self, save_scenario_file=False):
        self._create_parameters()
        self._create_catalogs()
        self._create_road()
        self._create_ego_entity()
        self._create_pedestrian_entity()
        self._create_init_ego()
        self._create_init_pedestrian()
        self._create_init_vehicle()
        self._create_event_ego()
        self._create_event_pedestrian_walk_event()
        self._create_event_vehicle()
        self._create_act()
        self._create_story()
        self._create_storyboard()
        self._create_scenario()
        self._print_scenario()
        self._print_scenario()
        self._run_scenario()

        if save_scenario_file:
            self._write_scenario()

    def _create_parameters(self):
        self._param_declaration = xosc.ParameterDeclarations()
        self._param_declaration.add_parameter(xosc.Parameter('HostVehicle', xosc.ParameterType.string, 'car_white'))
        self._param_declaration.add_parameter(xosc.Parameter('HostSpeed', xosc.ParameterType.double, 10.0))
        self._param_declaration.add_parameter(xosc.Parameter('PedestrianSpeed', xosc.ParameterType.double, 1.5))

    def _create_catalogs(self):
        self._catalog = xosc.Catalog()
        self._catalog.add_catalog('VehicleCatalog', '../xosc/Catalogs/Vehicles')
        self._catalog.add_catalog('RouteCatalog', '../xosc/Catalogs/Routes')

    def _create_road(self):
        self._road = xosc.RoadNetwork(roadfile="../xodr/fabriksgatan.xodr", scenegraph="../models/fabriksgatan.osgb")

    def _create_ego_entity(self):
        self._entities.add_scenario_object(self._ego_name, xosc.CatalogReference('VehicleCatalog', '$HostVehicle'))

    def _create_pedestrian_entity(self):
        pedestrian_bounding_box = xosc.BoundingBox(0.5, 0.6, 1.8, 0.06, 0.0, 0.923)
        pedestrian = xosc.Pedestrian(self._pedestrian_name, 'EPTa', 80, xosc.PedestrianCategory.pedestrian,
                                     pedestrian_bounding_box)

        pedestrian.properties.add_property('control', 'internal')
        pedestrian.properties.add_file('../models/walkman.osgb')
        self._entities.add_scenario_object(self._pedestrian_name, pedestrian)

    def _create_init_ego(self):
        step_time = xosc.TransitionDynamics(xosc.DynamicsShapes.step, xosc.DynamicsDimension.time, 1)
        catalog_reference = xosc.CatalogReference('RoutesAtFabriksgatan', 'HostStraightRoute')
        self._init.add_init_action(self._ego_name, xosc.AssignRouteAction(catalog_reference))
        self._init.add_init_action(self._ego_name, xosc.TeleportAction(xosc.LanePosition(0, 0, 1, 0)))
        self._init.add_init_action(self._ego_name, xosc.AbsoluteSpeedAction(10, step_time))

    def _create_init_pedestrian(self):
        pedestrian_orientation = xosc.Orientation(0, 0, 0, xosc.ReferenceContext.relative)
        self._init.add_init_action(self._pedestrian_name,
                                   xosc.TeleportAction(xosc.LanePosition(15, 0.5, 3, 0, pedestrian_orientation)))

    def _create_init_jam_vehicle(self):
        step_time = xosc.TransitionDynamics(xosc.DynamicsShapes.step, xosc.DynamicsDimension.time, 1)
        catalog_reference = xosc.CatalogReference('RoutesAtFabriksgatan', 'HostStraightRoute')
        self._init.add_init_action(self._ego_name, xosc.AssignRouteAction(catalog_reference))
        self._init.add_init_action(self._ego_name, xosc.TeleportAction(xosc.LanePosition(0, 0, 1, 0)))
        self._init.add_init_action(self._ego_name, xosc.AbsoluteSpeedAction(10, step_time))

    def _create_init_vehicle(self):
        pass

    def _create_event_pedestrian_walk_event(self):
        pedestrian_condition = xosc.EntityTrigger('ped_walk_event',
                                                  0.0,
                                                  xosc.ConditionEdge.rising,
                                                  xosc.TraveledDistanceCondition(5),
                                                  self._ego_name,
                                                  xosc.TriggeringEntitiesRule.any)
        p_trigger_condition = xosc.ConditionGroup()
        p_trigger_condition.add_condition(pedestrian_condition)
        pedestrian_event = xosc.Event('ped_walk_event', xosc.Priority.overwrite, maxexecution=1)
        pedestrian_event.add_trigger(p_trigger_condition)

        pedestrian_transition_dynamic = xosc.TransitionDynamics(xosc.DynamicsShapes.linear, xosc.DynamicsDimension.rate,
                                                                2)
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

        self._pedestrian_maneuver_group = xosc.ManeuverGroup('ped_mangroup', 1, selecttriggeringentities=False)
        self._pedestrian_maneuver_group.add_maneuver(pedestrian_maneuver)
        self._pedestrian_maneuver_group.add_actor(self._pedestrian_name)

    def _create_event_pedestrian_collide_event(self):
        pedestrian_condition = xosc.EntityTrigger('ped_fall_condition',
                                                  0.0,
                                                  xosc.ConditionEdge.rising,
                                                  xosc.TraveledDistanceCondition(5),
                                                  self._ego_name,
                                                  xosc.TriggeringEntitiesRule.any)
        p_trigger_condition = xosc.ConditionGroup()
        p_trigger_condition.add_condition(pedestrian_condition)

        pedestrian_event = xosc.Event('ped_collide_event', xosc.Priority.overwrite, maxexecution=1)
        pedestrian_event.add_trigger(p_trigger_condition)

        pedestrian_action_fall = xosc.TeleportAction(xosc.RelativeObjectPosition(self._pedestrian_name, 0.0, 0.0, 0.0))
        pedestrian_event.add_action('fall_action', pedestrian_action_fall)

        pedestrian_transition_dynamic = xosc.TransitionDynamics(xosc.DynamicsShapes.step, xosc.DynamicsDimension.time,
                                                                0.0)
        pedestrian_action_be_still = xosc.AbsoluteSpeedAction(0, pedestrian_transition_dynamic)
        pedestrian_event.add_action('be_still_action', pedestrian_action_be_still)

        # todo: Aggiungere al Maneuver
        # todo: Aggiungere al ManeuverGroup

    def _create_event_pedestrian_raise_event(self):
        pedestrina_condition = xosc.ValueTrigger('ped_raise_condition', 0.8, xosc.ConditionEdge.rising,
                                                 xosc.StoryboardElementStateCondition(xosc.StoryboardElementType.action,
                                                                                      'be_still_action',
                                                                                      xosc.StoryboardElementState.endTransition))
        p_trigger_condition = xosc.ConditionGroup()
        p_trigger_condition.add_condition(pedestrina_condition)

        pedestrian_event = xosc.Event('ped_raise_event', xosc.Priority.overwrite, maxexecution=1)
        pedestrian_event.add_trigger(p_trigger_condition)

        pedestrian_action_fall = xosc.TeleportAction(xosc.RelativeObjectPosition(self._pedestrian_name, 0.0, 0.0, 0.0,
                                                                                 xosc.Orientation(0, 0, -1.57,
                                                                                                  xosc.ReferenceContext.relative)))
        pedestrian_event.add_action('raise_action', pedestrian_action_fall)

        # todo: Aggiungere al Maneuver
        # todo: Aggiungere al ManeuverGroup

    def _create_event_ego(self):
        ego_condition = xosc.EntityTrigger('brake_Condition',
                                           0.0,
                                           xosc.ConditionEdge.rising,
                                           xosc.TimeToCollisionCondition(1.7, xosc.Rule.lessThan, True, True,
                                                                         self._pedestrian_name),
                                           self._ego_name,
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

        self._ego_maneuver_group = xosc.ManeuverGroup('brake-for-ped_mangroup', maxexecution=1,
                                                      selecttriggeringentities=False)
        self._ego_maneuver_group.add_maneuver(ego_maneuver)
        self._ego_maneuver_group.add_actor(self._ego_name)

    def _create_event_vehicle(self):
        pass

    def _create_act(self):
        start_trigger = xosc.ValueTrigger('ActStartCondition', 0.0, xosc.ConditionEdge.none,
                                          xosc.SimulationTimeCondition(0.0, xosc.Rule.greaterThan))

        entity_condition = xosc.ReachPositionCondition(xosc.LanePosition(0, 0, -3, 0), 5.0)
        stop_trigger = xosc.EntityTrigger('QuitCondition', 0.0, xosc.ConditionEdge.rising, entity_condition,
                                          self._pedestrian_name, xosc.TriggeringEntitiesRule.any)

        self._act = xosc.Act('LTAPActNPC', starttrigger=start_trigger)
        self._act.add_maneuver_group(self._ego_maneuver_group)
        self._act.add_maneuver_group(self._pedestrian_maneuver_group)

    def _create_story(self):
        self._story = xosc.Story('LTAPStory')
        self._story.add_act(self._act)
        story_parameter = xosc.Parameter('owner', xosc.ParameterType.string, 'NPC')
        self._story.parameter.add_parameter(story_parameter)

    def _create_storyboard(self):
        self._storyboard = xosc.StoryBoard(self._init,
                                           xosc.ValueTrigger('stop_simulation', 0, xosc.ConditionEdge.rising,
                                                             xosc.SimulationTimeCondition(10, xosc.Rule.greaterThan),
                                                             'stop'))
        self._storyboard.add_story(self._story)

    def _create_scenario(self):
        self._scenario = xosc.Scenario('adapt_speed_example', 'Angelo Carbo??e',
                                       self._param_declaration,
                                       entities=self._entities,
                                       storyboard=self._storyboard,
                                       roadnetwork=self._road,
                                       catalog=self._catalog)

    def _print_scenario(self):
        prettyprint(self._scenario.get_element())

    def _write_scenario(self):
        # write the OpenSCENARIO file as xosc using current script name
        self._scenario.write_xml("../xosc/" + os.path.basename(__file__).replace('.py', '.xosc'))

    def _run_scenario(self):
        esmini(self._scenario, os.path.join('../../esmini'))


scenario = Scenario()
scenario.generate_scenario(save_scenario_file=True)
