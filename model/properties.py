from .enumerations import e_Relation
from .actions import Action
from .events import Event


class TemporalRelation:
    def __init__(self, relation: e_Relation, object_is_action: Action = None, object_is_event: Event = None):
        self.relation = relation
        if object_is_action is None and object_is_event is None:

            raise AttributeError

        if object_is_action is not None and object_is_event is not None:
            # only one
            raise AttributeError

        self.object_is_action = object_is_action
        self.object_is_event = object_is_event
