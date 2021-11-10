"""
    Simple example showing how one cf_vehicle triggers based on the speed of another vehcile, then changes it speed

    Some features used:

    - SpeedCondition

    - AbsoluteSpeedAction

    - RoadPosition

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

param_declaration.add_parameter(xosc.Parameter('$HostVehicle', xosc.ParameterType.string, 'car_white'))
param_declaration.add_parameter(xosc.Parameter('$TargetVehicle', xosc.ParameterType.string, 'car_red'))

# create vehicles
bb = xosc.BoundingBox(2, 5, 1.8, 2.0, 0, 0.9)
fa = xosc.Axle(0.523598775598, 0.8, 1.68, 2.98, 0.4)
ba = xosc.Axle(0.523598775598, 0.8, 1.68, 0, 0.4)
white_veh = xosc.Vehicle('car_white', xosc.VehicleCategory.car, bb, fa, ba, 69, 10, 10)

white_veh.add_property_file('../models/car_white.osgb')
white_veh.add_property('model_id', '0')

bb = xosc.BoundingBox(1.8, 4.5, 1.5, 1.3, 0, 0.8)
fa = xosc.Axle(0.523598775598, 0.8, 1.68, 2.98, 0.4)
ba = xosc.Axle(0.523598775598, 0.8, 1.68, 0, 0.4)
red_veh = xosc.Vehicle('car_red', xosc.VehicleCategory.car, bb, fa, ba, 69, 10, 10)

red_veh.add_property_file('../models/car_red.osgb')
red_veh.add_property('model_id', '2')

# create entities

ego_name = 'Ego'
vehicle_name = 'Target'

entities = xosc.Entities()
entities.add_scenario_object(ego_name, white_veh)
entities.add_scenario_object(vehicle_name, red_veh)

# create init

init = xosc.Init()

ego_start = xosc.TeleportAction(xosc.LanePosition(25, 0, -2, 0))
ego_step_time = xosc.TransitionDynamics(xosc.DynamicsShapes.sinusoidal, xosc.DynamicsDimension.time, 8)
ego_speed = xosc.AbsoluteSpeedAction(25, ego_step_time)

vehicle_start = xosc.TeleportAction(xosc.LanePosition(15, 0, -3, 0))
vehicle_step_time = xosc.TransitionDynamics(xosc.DynamicsShapes.step, xosc.DynamicsDimension.time, 1)
vehicle_speed = xosc.AbsoluteSpeedAction(15, vehicle_step_time)

# pedestrian_start = xosc.TeleportAction(xosc.RoadPosition(30,-5,0))

init.add_init_action(ego_name, ego_speed)
init.add_init_action(ego_name, ego_start)
init.add_init_action(vehicle_name, vehicle_speed)
init.add_init_action(vehicle_name, vehicle_start)

# create an event

trigger_condition = xosc.SpeedCondition(24, xosc.Rule.greaterThan)
trigger = xosc.EntityTrigger('MyTestTrigger', 0.2, xosc.ConditionEdge.none, trigger_condition, ego_name)

event = xosc.Event('MyFirstEvent', xosc.Priority.overwrite)
event.add_trigger(trigger)

linear_time = xosc.TransitionDynamics(xosc.DynamicsShapes.linear, xosc.DynamicsDimension.time, 5)
action = xosc.AbsoluteSpeedAction(30, linear_time)
event.add_action('NewSpeed', action)

# create the maneuver
maneuver = xosc.Maneuver('MyManeuver')
maneuver.add_event(event)

maneuver_group = xosc.ManeuverGroup('ManGroup')
maneuver_group.add_actor('$owner')
maneuver_group.add_maneuver(maneuver)
start_trigger = xosc.ValueTrigger('StartTrigger', 0, xosc.ConditionEdge.rising, xosc.SimulationTimeCondition(0, xosc.Rule.greaterThan))
act = xosc.Act('MyAct', start_trigger)
act.add_maneuver_group(maneuver_group)

# create the story
story_param = xosc.ParameterDeclarations()
story_param.add_parameter(xosc.Parameter('$owner', xosc.ParameterType.string, vehicle_name))
story = xosc.Story('MyStory', story_param)
story.add_act(act)

# create the storyboard
sb = xosc.StoryBoard(init, xosc.ValueTrigger('StopSimulation', 0, xosc.ConditionEdge.rising, xosc.SimulationTimeCondition(15, xosc.Rule.greaterThan), 'stop'))
sb.add_story(story)

# create the scenario
sce = xosc.Scenario('AdaptSpeedExample', 'Mandolin', param_declaration, entities=entities, storyboard=sb, roadnetwork=road, catalog=catalog)

# Print the resulting xml
# prettyprint(sce.get_element())

# write the OpenSCENARIO file as xosc using current script name
sce.write_xml("xosc/" + os.path.basename(__file__).replace('.py', '.xosc'))

# uncomment the following lines to display the scenario using esmini
from scenariogeneration import esmini

esmini(sce, os.path.join('esmini'))
