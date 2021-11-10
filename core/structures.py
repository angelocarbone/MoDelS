class CausalFactor:
    def __init__(self, id_: int, name: str, description: str):
        self.id_ = id_
        self.name = name
        self.description = description


class VehicleCausalFactor:
    def __init__(self):
        self.cf_driver = []
        self.cf_fellow_passenger = []
        self.cf_vehicle = []

    @property
    def cf_driver(self):
        return self.cf_driver

    @cf_driver.setter
    def cf_driver(self, value: CausalFactor):
        self.cf_driver.append(value)

    @property
    def cf_fellow_passenger(self):
        return self.cf_fellow_passenger

    @cf_fellow_passenger.setter
    def cf_fellow_passenger(self, value: CausalFactor):
        self.cf_fellow_passenger.append(value)

    @property
    def cf_vehicle(self):
        return self.cf_vehicle

    @cf_vehicle.setter
    def cf_vehicle(self, value: CausalFactor):
        self.cf_vehicle.append(value)


class SubScenario:
    def __init__(self):
        self.id_ = None
        self.name = None
        self.description = None


class Scenario:
    def __init__(self):
        self.id_ = None
        self.name = None
        self.description = None
        self.sub_scenarios: [SubScenario] = []

    @property
    def id_(self):
        return self.id_

    @id_.setter
    def id_(self, value: int):
        self.id_ = value

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value: str):
        self.name = value

    @property
    def description(self):
        return self.description

    @description.setter
    def description(self, value: str):
        self.description = value

    @property
    def sub_scenarios(self):
        return self.sub_scenarios

    @sub_scenarios.setter
    def sub_scenarios(self, value):
        self.sub_scenarios.append(value)


class VehicleSettings:
    def __init__(self):
        self.id_ = None
        self.vehicle_causal_factor_id = None
        self.vehicle_causal_factor_value = None
        self.vehicle_causal_factor_description = None
        self.driver_causal_factor_id = None
        self.driver_causal_factor_value = None
        self.driver_causal_factor_description = None
        self.fellow_passenger_causal_factor_id = None
        self.fellow_passenger_causal_factor_value = None
        self.fellow_passenger_causal_factor_description = None

    @property
    def vehicle_causal_factor_id(self):
        return self.vehicle_causal_factor_id

    @vehicle_causal_factor_id.setter
    def vehicle_causal_factor_id(self, value):
        self.vehicle_causal_factor_id = value

    @property
    def vehicle_causal_factor_value(self):
        return self.vehicle_causal_factor_value

    @vehicle_causal_factor_value.setter
    def vehicle_causal_factor_value(self, value):
        self.vehicle_causal_factor_value = value

    @property
    def vehicle_causal_factor_description(self):
        return self.vehicle_causal_factor_description

    @vehicle_causal_factor_description.setter
    def vehicle_causal_factor_description(self, value):
        self.vehicle_causal_factor_description = value

    @property
    def driver_causal_factor_id(self):
        return self.driver_causal_factor_id

    @driver_causal_factor_id.setter
    def driver_causal_factor_id(self, value):
        self.driver_causal_factor_id = value

    @property
    def driver_causal_factor_value(self):
        return self.driver_causal_factor_value

    @driver_causal_factor_value.setter
    def driver_causal_factor_value(self, value):
        self.driver_causal_factor_value = value

    @property
    def driver_causal_factor_description(self):
        return self.driver_causal_factor_description

    @driver_causal_factor_description.setter
    def driver_causal_factor_description(self, value):
        self.driver_causal_factor_description = value

    @property
    def fellow_passenger_causal_factor_id(self):
        return self.fellow_passenger_causal_factor_id

    @fellow_passenger_causal_factor_id.setter
    def fellow_passenger_causal_factor_id(self, value):
        self.fellow_passenger_causal_factor_id = value

    @property
    def fellow_passenger_causal_factor_value(self):
        return self.fellow_passenger_causal_factor_value

    @fellow_passenger_causal_factor_value.setter
    def fellow_passenger_causal_factor_value(self, value):
        self.fellow_passenger_causal_factor_value = value

    @property
    def fellow_passenger_causal_factor_description(self):
        return self.fellow_passenger_causal_factor_description

    @fellow_passenger_causal_factor_description.setter
    def fellow_passenger_causal_factor_description(self, value):
        self.fellow_passenger_causal_factor_description = value


class Scenarios:
    def __init__(self):
        self.scenario: [Scenario] = []
        self.ego_settings = []
        self.vehicle_settings: [VehicleSettings] = []
        self.passenger_settings = []

    @property
    def scenario(self):
        return self.scenario

    @scenario.setter
    def scenario(self, value: Scenario):
        self.scenario.append(value)

    @property
    def vehicle_settings(self):
        return self.vehicle_settings

    @vehicle_settings.setter
    def vehicle_settings(self, value: VehicleSettings):
        self.vehicle_settings.append(value)
