from scenarios import helper
from scenarios.builder import Builder
from model.enumerations import e_ExperienceFactor, e_MentalOrEmotionalFactor, e_PhyOrPhyFactor, e_EntityType, e_Relation, e_CausalFactorType
from model.knowledge_base import kb
from model.entities import Entity, CausalFactor
from model.utils import BoundingBox
from model import rule


class Controller:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print('Controller object has been created.')
            cls._instance = super(Controller, cls).__new__(cls)
            # Put any initialization here.
        return cls._instance

    def __init__(self, v_obj, m_obj):
        self._v_obj = v_obj
        self._m_obj = m_obj

    def __str__(self):
        return "Controller"

    def withdraw_btn_callback(self):
        val = float(self._v_obj.rmb_text.displayText())
        self._m_obj.withdraw(val)

    def deposit_btn_callback(self):
        val = float(self._v_obj.rmb_text.displayText())
        self._m_obj.deposit(val)

    def get_experience_causal_factor(self):
        res = e_ExperienceFactor.all()
        causal_factors = []
        for _ in res:
            causal_factors.append(_[0])
        return causal_factors

    def get_mental_or_emotional_causal_factor(self):
        res = e_MentalOrEmotionalFactor.all()
        causal_factors = []
        for _ in res:
            causal_factors.append(_[0])
        return causal_factors

    def get_phy_or_phy_causal_factor(self):
        res = e_PhyOrPhyFactor.all()
        causal_factors = []
        for _ in res:
            causal_factors.append(_[0])
        return causal_factors

    def list_of_vehicle_causal_factor(self):
        _ = {
            "cf_driver": {
                "0": {
                    "id": "0",
                    "name": "Name of causal factor",
                    "description": "Description of causal factor."
                },
                "1": {
                    "id": "0",
                    "name": "Name of causal factor",
                    "description": "Description of causal factor."
                },
                "3": {
                    "id": "0",
                    "name": "Name of causal factor",
                    "description": "Description of causal factor."
                },
            },
            "cf_fellow_passenger": {
                "0": {
                    "id": "0",
                    "name": "Name of causal factor",
                    "description": "Description of causal factor."
                },
                "1": {
                    "id": "0",
                    "name": "Name of causal factor",
                    "description": "Description of causal factor."
                },
                "3": {
                    "id": "0",
                    "name": "Name of causal factor",
                    "description": "Description of causal factor."
                },
            },
            "cf_vehicle": {
                "0": {
                    "id": "0",
                    "name": "Name of causal factor",
                    "description": "Description of causal factor."
                },
                "1": {
                    "id": "0",
                    "name": "Name of causal factor",
                    "description": "Description of causal factor."
                },
                "3": {
                    "id": "0",
                    "name": "Name of causal factor",
                    "description": "Description of causal factor."
                },
            },
        }

        return _

    def list_of_pedestrian_causal_factor(self):
        pass

    def list_of_scenarios(self):
        # todo: Load list of scenarios from dedicate module.
        _ = {
                "0": {
                    "name": "scenario7",
                    "description": "Description of scenario 01 here",
                    "sub_scenarios": {
                        "0": {
                            "name": "scenario01_20211016-100245",
                            "description": "Description of scenario01_20211016-100245",
                        },
                        "1": {
                            "name": "scenario01_20211016-101607",
                            "description": "Description of scenario01_20211016-101607",
                        },
                        "2": {
                            "name": "scenario01_20211021-101607",
                            "description": "Description of scenario01_20211021-101607",
                        }
                    },
                    "ego_settings": {},
                    "vehicles_settings": {
                        "0": {
                            "cf_vehicle": {
                                "causal_factor": {}
                            },
                            "cf_driver": {
                                "causal_factor": {
                                    "id": "1",
                                    "value": "distraction",
                                    "description": "Description of causal factor.",
                                }
                            },
                            "cf_fellow_passenger": {}
                        },
                    },
                    "pedestrian_settings": {},
                },
                "1": {"name": "Scenario02", "description": "Description of scenario 02 here"},
            }
        return helper.get_scenarios()

    def run_scenario_callback(self, scenario_name: str):
        print("pushButton_run_scenario {}".format(scenario_name))
        helper.run_scenario(scenario_name)

    def run_sub_scenario_callback(self, scenario):
        import os
        from scenariogeneration import esmini
        from config import ESMINI_DIR
        esmini(scenario, os.path.join(ESMINI_DIR))

    def action_exit_callback(self):
        return True

    def update_scenario_callback(self, vehicle_id):
        print("pushButton_update_scenario")
        # done: create Driver (AndreA) instance in ontology
        # done: link Driver to Vehicle (JamCar)
        # done: assign CausalFactor to Driver (AndreA) instance
        # done: SPARQL: Given a CausalFactor, give me DrivingError
        # todo: SPARQL: Given current Action + DrivingError, give me next Actions.
        # todo: For each actions returned, link each one to an alternative behavior in library
        # todo: Present alternative to UI
        entity = Entity('Andrea', 68, e_EntityType.Driver, BoundingBox(0.5, 0.6, 1.8, 1.3, 0.0, 0.8))
        andrea = kb.insert_entity(entity)

        vehicle = kb.get_entity_from_cache(vehicle_id)
        kb.add_relation(andrea, vehicle, e_Relation.isOn.isOnVehicle.driverIsOnVehicle)
        current_action = kb.get_current_action(vehicle)
        cf = CausalFactor("test_name", e_CausalFactorType.HumanFactor.MentalOrEmotionalFactor.Distraction)
        cf_i = kb.insert_entity(cf)
        kb.add_relation(andrea, cf_i, e_Relation.isImpaired.driverIsImpaired)
        driving_errors = rule.get_driving_error_to_causal_factor_rule(e_CausalFactorType.HumanFactor.MentalOrEmotionalFactor.Distraction)

        builder = Builder()

        sub_scenarios = builder.get_sub_scenario_foo()

        import re
        for d_error in driving_errors:
            _ = re.sub(".*#", "", d_error['x'])
            # builder.build("scenario10", _, current_action)

        return sub_scenarios

