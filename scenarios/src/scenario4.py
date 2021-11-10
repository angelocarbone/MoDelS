"""
    An example setting up multiple vehicles triggering on eachother and running in parallel

    Some features used:

    - AbsoluteLaneChangeAction

    - TimeHeadwayCondition

"""
import os
from scenariogeneration import xosc, prettyprint

# create catalogs
catalog = xosc.Catalog()
catalog.add_catalog('VehicleCatalog', '../xosc/Catalogs/Vehicles')

# create road
road = xosc.RoadNetwork(roadfile='../xodr/e6mini.xodr', scenegraph='../models/e6mini.osgb')

# create parameters
param_declaration = xosc.ParameterDeclarations()


# create entities
ego_name = 'Ego'
red_name = 'Target1'
yellow_name = 'Target2'

entities = xosc.Entities()
entities.add_scenario_object(ego_name, xosc.CatalogReference('VehicleCatalog', 'car_white'))
entities.add_scenario_object(red_name, xosc.CatalogReference('VehicleCatalog', 'car_red'))
entities.add_scenario_object(yellow_name, xosc.CatalogReference('VehicleCatalog', 'car_yellow'))

# create init

init = xosc.Init()
step_time = xosc.TransitionDynamics(xosc.DynamicsShapes.step, xosc.DynamicsDimension.time, 1)

init.add_init_action(ego_name, xosc.TeleportAction(xosc.LanePosition(25, 0, -3, 0)))
init.add_init_action(ego_name, xosc.AbsoluteSpeedAction(30, step_time))

init.add_init_action(red_name, xosc.TeleportAction(xosc.LanePosition(15, 0, -2, 0)))
init.add_init_action(red_name, xosc.AbsoluteSpeedAction(40, step_time))

init.add_init_action(yellow_name, xosc.TeleportAction(xosc.LanePosition(35, 0, -4, 0)))
init.add_init_action(yellow_name, xosc.AbsoluteSpeedAction(30, step_time))


# create an event for the red car
r_trigger_condition = xosc.TimeHeadwayCondition(red_name, 0.1, xosc.Rule.greaterThan)
r_trigger = xosc.EntityTrigger('red_trigger', 0.2, xosc.ConditionEdge.rising, r_trigger_condition, ego_name)

r_event = xosc.Event('first_lane_change', xosc.Priority.overwrite)
r_event.add_trigger(r_trigger)

r_transition_dynamic = xosc.TransitionDynamics(xosc.DynamicsShapes.sinusoidal, xosc.DynamicsDimension.time, 4)
r_action = xosc.AbsoluteLaneChangeAction(-4, r_transition_dynamic)
r_event.add_action('lane_change_red', r_action)

# create the act for the red car
r_maneuver = xosc.Maneuver('red_maneuver')
r_maneuver.add_event(r_event)

r_maneuver_group = xosc.ManeuverGroup('maneuver_group_red')
r_maneuver_group.add_actor(red_name)
r_maneuver_group.add_maneuver(r_maneuver)

act = xosc.Act('red_act', xosc.ValueTrigger('start_trigger', 0, xosc.ConditionEdge.rising,
                                            xosc.SimulationTimeCondition(0, xosc.Rule.greaterThan)))
act.add_maneuver_group(r_maneuver_group)

# create an event for the yellow car
y_trigger_condition = xosc.TimeHeadwayCondition(red_name, 0.5, xosc.Rule.greaterThan)
y_trigger = xosc.EntityTrigger('yellow_trigger', 0, xosc.ConditionEdge.rising, y_trigger_condition, yellow_name)

y_event = xosc.Event('yellow_lane_change', xosc.Priority.overwrite)
y_event.add_trigger(y_trigger)

y_transition_dynamic = xosc.TransitionDynamics(xosc.DynamicsShapes.sinusoidal, xosc.DynamicsDimension.time, 2)
y_action = xosc.AbsoluteLaneChangeAction(-3, y_transition_dynamic)
y_event.add_action('lane_change_yellow', y_action)

# create the act for the yellow car
y_maneuver = xosc.Maneuver('yellow_maneuver')
y_maneuver.add_event(y_event)

y_maneuver_group = xosc.ManeuverGroup('yellow_maneuver_group')
y_maneuver_group.add_actor(yellow_name)
y_maneuver_group.add_maneuver(y_maneuver)
y_start_trigger = xosc.ValueTrigger('start_trigger', 0, xosc.ConditionEdge.rising, xosc.SimulationTimeCondition(0, xosc.Rule.greaterThan))
act.add_maneuver_group(y_maneuver_group)

# create the story
story = xosc.Story('my_story')
story.add_act(act)

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