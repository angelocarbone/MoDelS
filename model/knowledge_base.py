from owlready2 import get_ontology, default_world, sync_reasoner_pellet
from config import ROOT_DIR
from .enumerations import e_EntityType, e_Relation, e_CausalFactorType
from .entities import Entity, EntityThing, Road, CausalFactor
from .actions import Action
from .properties import TemporalRelation
from core.utils import get_formatted_name


# Annotazione
# Innesto causal factor
# Interrogazione


class KnowledgeBase:
    _instance = None
    onto_path = ROOT_DIR + '/model/owl/' + 'onto.owl'
    _entity_cache = {}

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(KnowledgeBase, cls).__new__(cls)
            # Put any initialization here.
        return cls._instance

    def __init__(self, path=onto_path):
        try:
            self.onto = get_ontology(path).load()
        except Exception:
            AssertionError('Error')

    def insert_entity(self, entity_: Entity) -> EntityThing:
        """
        Creating an Individual instance in ontology.
        The first parameter is the name (or identifier) of the Individual;
        The Instance is immediately available in the ontology.

        :param entity_: An instance of Entity
        :return: An instance of Entity
        """
        individual_ = None

        parent_entity_type = entity_.entity_type.class_name

        if parent_entity_type == e_EntityType.Vehicle.name():
            individual_ = self.onto[entity_.entity_type](get_formatted_name(entity_.name))
        elif parent_entity_type == e_EntityType.Pedestrian.name():
            individual_ = self.onto[entity_.entity_type](get_formatted_name(entity_.name))
        elif entity_.entity_type == e_EntityType.Driver:
            individual_ = self.onto[entity_.entity_type](get_formatted_name(entity_.name))
        elif entity_.entity_type == e_CausalFactorType.HumanFactor.MentalOrEmotionalFactor.Distraction:
            individual_ = self.onto[entity_.entity_type](get_formatted_name(entity_.name))
        else:
            AssertionError('Not allowed entity type.')

        self.put_entity_in_entity_cache(get_formatted_name(entity_.name), individual_)

        self.save_and_sync()

        return individual_

    def get_entity_from_cache(self, entity_name):
        return self._entity_cache[get_formatted_name(entity_name)]

    def put_entity_in_entity_cache(self, entity_name: str, entity_object):
        self._entity_cache[entity_name] = entity_object

    def insert_road(self, road: Road):
        pass

    def destroy_entity(self, entity_: Entity):
        raise NotImplementedError()

    def assign_action(self, entity_thing: EntityThing, action: Action, when: TemporalRelation = None):
        # todo: to replace with add_relation function
        """
        Assigns an action to an entity.

        :param entity_thing:
        :param action:
        :param when:
        :return:
        """
        action_thing = None
        if entity_thing.is_a:
            # parent_action_type = action_individual.action_type.class_name
            # Creates new individual of action_individual
            action_thing = self.onto[action.action_type.name](get_formatted_name(action.name))
            # Relates new individual to entity_thing
            entity_thing.performsAction = action_thing

            if when:
                # TODO: Implement me
                raise NotImplementedError

            print(action_thing.__class__)
        return action_thing

    def add_relation(self, entity_subject: EntityThing, entity_object: EntityThing, relation: e_Relation):
        if entity_subject.is_a and entity_object.is_a:
            print(__class__)

        if relation == e_Relation.isOn.isOnVehicle.driverIsOnVehicle:
            entity_subject.driverIsOnVehicle = entity_object
        elif relation == e_Relation.isImpaired.entityIsImpaired:
            entity_subject.entityIsImpaired = entity_object
        elif relation == e_Relation.isImpaired.driverIsImpaired:
            entity_subject.driverIsImpaired = entity_object

        self.save_and_sync()

    def get_current_action(self, entity_subject: EntityThing):
        if entity_subject.is_a:
            return entity_subject.performsAction.__class__

    def save_and_sync(self):
        sync_reasoner_pellet()
        self.onto.save(self.onto_path)

    def select_driving_error_by_causal_factor(self, causal_factor_: CausalFactor):
        l = default_world.sparql(
            """
            PREFIX mds: <http://www.angelocarbone.com/ontologies/MoDelS#>
            
            SELECT ?de
            WHERE {
                ?cf mds:isCauseOf ?de
            }
            """
        )

    def select_next_action_by_current_action(self, current_action: CausalFactor):
        pass

    def select_next_alternative_actions(self, current_action: Action, next_expected_action: Action,
                                        causal_factor: CausalFactor):
        pass


kb = KnowledgeBase()

#
#
# from utils import BoundingBox
#
# e1 = Entity('Jam', 10, e_EntityType.Vehicle.Car, BoundingBox(0.5, 0.6, 1.8, 1.3, 0.0, 0.8))
# e1_i = kb.insert_entity(e1)
#
# e2 = Entity('Andrea', 10, e_EntityType.Driver, BoundingBox(0.5, 0.6, 1.8, 1.3, 0.0, 0.8))
# e2_i = kb.insert_entity(e2)
#
# kb.add_relation(e2_i, e1_i, e_Relation.isOn.isOnVehicle.driverIsOnVehicle)
#
#
