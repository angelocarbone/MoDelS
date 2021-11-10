from owlready2 import Thing
from .utils import Axles, BoundingBox, Dynamics
from .enumerations import e_EntityType, e_CausalFactorType, e_DrivingErrorType, e_LineType


class EntityThing(Thing):
    pass


class RoadThing(Thing):
    pass


class SectionThing(Thing):
    pass


class Entity:
    """
    Definition of entities (scenario objects or entity selections) in a scenario.
    """
    def __init__(self, name: str,
                 mass: float,
                 entity_type: e_EntityType,
                 bounding_box: BoundingBox,
                 front_axle: Axles = None,
                 rear_axle: Axles = None,
                 dynamics: Dynamics = None):
        self.name = name
        self.mass = mass
        self.entity_type = entity_type
        self.bounding_box = bounding_box
        self.front_axle = front_axle
        self.rear_axle = rear_axle
        self.dynamics = dynamics


class CausalFactor:
    def __init__(self, name: str, entity_type: e_CausalFactorType):
        self.name = name
        self.entity_type = entity_type


class DrivingError:
    def __init__(self, name: str, driving_error_type: e_DrivingErrorType):
        self.name = name
        self.driving_error_type = driving_error_type


class Road:
    def __init__(self, id_: int, speed: float):
        self.id_ = id_
        self.speed = speed


class Section:
    def __init__(self, id_: int, road_individual: RoadThing):
        self.id_ = id_
        self.road_individual = road_individual


class Lane:
    def __init__(self, id_: int, speed: float, width: float, line_type: e_LineType, section_individual: SectionThing):
        self.id_ = id_
        self.speed = speed
        self.width = width
        self.line_type = line_type
        self.section_individual = section_individual


class Junction:
    def __init__(self, id_: int, road_individual: RoadThing):
        self.id_ = id_
        self.road_individual = road_individual
