import importlib
from model.enumerations import e_DrivingErrorType
from model import rule


class Builder:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(Builder, cls).__new__(cls)
            # Put any initialization here.
        return cls._instance

    def __init__(self):
        pass

    def build(self, scenario_name: str, driving_error, current_action):
        factory_module = importlib.import_module("scenarios.src.{0}".format(scenario_name))
        factory_class_ = getattr(factory_module, "Scenario")
        factory_instance = factory_class_()

        current_action = "AbsoluteSpeedAction"
        next_actions = rule.get_driving_error_to_action_rule(driving_error, current_action)

        lane_change_action = False
        short_distance_lane_change_action = False
        long_distance_lane_change_action = False
        short_time_lane_change_action = False
        long_time_lane_change_action = False

        injected_init_function = []
        injected_event_function = []

        # parent_driving_error = driving_error.class_name
        #
        # if parent_driving_error == e_DrivingErrorType.DecisionError:
        #     if driving_error == e_DrivingErrorType.DecisionError.AggressiveDriving:
        #         raise NotImplementedError
        #     elif driving_error == e_DrivingErrorType.DecisionError.AvoidingConflict:
        #         raise NotImplementedError
        #     elif driving_error == e_DrivingErrorType.DecisionError.ImproperManeuver:
        #         raise NotImplementedError
        #     elif driving_error == e_DrivingErrorType.DecisionError.ImproperStoppingOrDecelerating:
        #         raise NotImplementedError
        #     elif driving_error == e_DrivingErrorType.DecisionError.SpeedRelatedError:
        #         raise NotImplementedError
        # elif parent_driving_error == e_DrivingErrorType.PerformanceError:
        #     if driving_error == e_DrivingErrorType.PerformanceError.PoorLateralControl:
        #         raise NotImplementedError
        #     elif driving_error == e_DrivingErrorType.PerformanceError.PoorLongitudinalControl:
        #         raise NotImplementedError
        # elif parent_driving_error == e_DrivingErrorType.RecognitionError:
        #     if driving_error == e_DrivingErrorType.RecognitionError.DistractionError:
        #         raise NotImplementedError
        #     elif driving_error == e_DrivingErrorType.RecognitionError.RecognitionFailure:
        #         raise NotImplementedError
        # elif parent_driving_error == e_DrivingErrorType.Violation:
        #     if driving_error == e_DrivingErrorType.Violation.IllegalManeuver:
        #         raise NotImplementedError
        #     elif driving_error == e_DrivingErrorType.Violation.IntentionalIntersectionViolation:
        #         raise NotImplementedError
        #     elif driving_error == e_DrivingErrorType.Violation.SpeedViolation:
        #         raise NotImplementedError
        #     elif driving_error == e_DrivingErrorType.Violation.UnintentionalIntersectionViolation:
        #         raise NotImplementedError
        # else:
        #     raise AttributeError

        factory_instance.base_scenario_factory(save_scenario_file=True,
                                               print_scenario=False,
                                               injected_init_function=factory_instance.add_jam_vehicle_accelerate_event(
                                                   absolute_speed_action_value=50),
                                               injected_event_function=factory_instance.add_jam_vehicle_lane_change_left_event(),
                                               run_scenario_file=False)

    def foo1(self):
        scenario_name = "scenario10"
        factory_module = importlib.import_module("scenarios.src.{0}".format(scenario_name))
        factory_class_ = getattr(factory_module, "Scenario")
        factory_instance = factory_class_()
        sub_scenarios = []

        res = factory_instance.base_scenario_factory(save_scenario_file=True,
                                                     print_scenario=False,
                                                     injected_init_function=factory_instance.add_jam_vehicle_accelerate_event(
                                                         absolute_speed_action_value=50),
                                                     injected_event_function=factory_instance.add_jam_vehicle_lane_change_left_event(),
                                                     run_scenario_file=False)

        sub_scenarios.append(res)

        return sub_scenarios

    def get_sub_scenario_foo(self):
        scenario_name = "scenario10"
        factory_module = importlib.import_module("scenarios.src.{0}".format(scenario_name))
        factory_class_ = getattr(factory_module, "Scenario")
        factory_instance = factory_class_()
        sub_scenarios = []

        # sub-scenario 0
        # Jam Car accelerates with absolute speed action 50 m/s.
        res = factory_instance.base_scenario_factory(save_scenario_file=True,
                                                     print_scenario=False,
                                                     run_scenario_file=False,
                                                     injected_init_function=None,
                                                     injected_event_function=factory_instance.add_jam_vehicle_accelerate_event,
                                                     absolute_speed_action_value=50)

        sub_scenarios.append(res)

        # sub-scenario 1
        # Jam Car swerves on the right changing lane.
        res = factory_instance.base_scenario_factory(save_scenario_file=True,
                                                     print_scenario=False,
                                                     run_scenario_file=False,
                                                     injected_init_function=None,
                                                     injected_event_function=factory_instance.add_jam_vehicle_lane_change_right_event,
                                                     absolute_change_lane_value=-2)

        sub_scenarios.append(res)

        # sub-scenario 2
        # Jam Car brakes and accelerates continously.
        res = factory_instance.base_scenario_factory(save_scenario_file=True,
                                                     print_scenario=False,
                                                     run_scenario_file=False,
                                                     injected_init_function=factory_instance.create_init_jam_vehicle,
                                                     injected_event_function=factory_instance.add_jam_vehicle_brake_and_accelerate_event,
                                                     lane_position_s=280,
                                                     lane_position_offset=0,
                                                     lane_position_lane_id=-1,
                                                     lane_position_road_id=2,
                                                     absolute_speed_action=10,
                                                     speed_after_brake=2,
                                                     speed_to_accelerate=30)

        sub_scenarios.append(res)

        # sub-scenario 3
        # Jam Car swerves on the left changing lane.
        res = factory_instance.base_scenario_factory(save_scenario_file=True,
                                                     print_scenario=False,
                                                     run_scenario_file=False,
                                                     injected_init_function=None,
                                                     injected_event_function=factory_instance.add_jam_vehicle_lane_change_left_event,
                                                     absolute_change_lane_value=2)

        sub_scenarios.append(res)

        return sub_scenarios
