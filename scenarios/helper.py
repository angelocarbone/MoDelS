import importlib

# TODO: The list of scenarios should be reached differently, and not in a simple list as below.
list_of_scenarios = ['scenario10']


def run_scenario(scenario_name):
    module = importlib.import_module("scenarios.src.{}".format(scenario_name))
    class_ = getattr(module, "Scenario")
    instance = class_()
    instance.base_scenario_factory(save_scenario_file=True, print_scenario=False)


def get_scenarios():
    sl = {}

    index = 0

    for s_name in list_of_scenarios:
        module = importlib.import_module("scenarios.src.{}".format(s_name))
        s_module = module.__name__
        s_description = module.__doc__

        tl = {}
        tl['name'] = s_name
        tl['module'] = s_module
        tl['description'] = s_description
        tl['vehicle_id'] = "JamCar"
        tl['vehicle_name'] = "Jam Car"
        sl[index] = tl

        index += 1

    return sl


def get_scenario_info(scenario_name):
    pass
