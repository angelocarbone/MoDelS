""" the actions module contains the actions defined OpenSCENARIO

"""
# TODO: Change descriptions in all module.

from .utils import TransitionDynamics, DynamicsConstrains, Position
from .enumerations import e_ActionType
from .entities import Entity


class Action:
    """ Private class used to define an action, should not be used by the user.
            Used as a wrapper to create the extra elements needed

            Parameters
            ----------
                name (str): name of the action

                action (*Action): any action

            Attributes
            ----------
                name (str): name of the action

                action (*Action): any action

            Methods
            -------
                get_element()
                    Returns the full ElementTree of the class

                get_attributes()
                    Returns a dictionary of all attributes of the class

        """
    def __init__(self, name: str, action_type: e_ActionType):
        self.name = name
        self.action_type = action_type


class TeleportAction(Action):
    """ the TeleportAction creates the Teleport action of OpenScenario

            Parameters
            ----------
                position (*Position): any position object

            Attributes
            ----------
                position (*Position): any position object


            Methods
            -------
                get_element()
                    Returns the full ElementTree of the class

        """
    _action_type = e_ActionType.TeleportAction

    def __init__(self, name: str, position: Position):
        super().__init__(name, self._action_type)
        self.position = position


# ***
# Private Actions
# ---
# LongitudinalAction
#


class AbsoluteSpeedAction(Action):
    """ The AbsoluteSpeedAction class specifies a LongitudinalAction of type SpeedAction with an abosulte target speed

        Parameters
        ----------
            speed (float): the speed wanted

            transition_dynamics (TransitionDynamics): how the change should be made

        Attributes
        ----------

            speed (float): the speed wanted

            transition_dynamics (TransitionDynamics): how the change should be made

        Methods
        -------
            get_element()
                Returns the full ElementTree of the class

            get_attributes()
                Returns a dictionary of all attributes of the class
    """
    _action_type = e_ActionType.AbsoluteSpeedAction

    def __init__(self, name: str, speed: float, transition_dynamics: TransitionDynamics):
        """ initalize the AbsoluteSpeedAction

        Parameters
        ----------
            speed (float): the speed wanted

            transition_dynamics (TransitionDynamics): how the change should be made

        """
        super().__init__(name, self._action_type)
        self.speed = speed
        if not isinstance(transition_dynamics, TransitionDynamics):
            raise TypeError('transition_dynamics input not of type TransitionDynamics')
        self.transition_dynamics = transition_dynamics


class RelativeSpeedAction(Action):
    """ The RelativeSpeedAction creates a LongitudinalAction of type SpeedAction with a relative target

        Parameters
        ----------
            speed (float): the speed wanted

            target (str): the name of the relative target (used for relative speed)

            transition_dynamics (TransitionDynamics): how the change should be made

            value_type (str): the type of relative speed wanted (used for relative speed)

            continuous (bool): if the controller tries to keep the relative speed

        Attributes
        ----------
            speed (float): the speed wanted

            target (str): the name of the relative target (used for relative speed)

            value_type (str): the type of relative speed wanted (used for relative speed)

            continuous (bool): if the controller tries to keep the relative speed

            transition_dynamics (TransitionDynamics): how the change should be made

        Methods
        -------
            get_element()
                Returns the full ElementTree of the class

            get_attributes()
                Returns a dictionary of all attributes of the class

    """
    _action_type = e_ActionType.RelativeSpeedAction

    def __init__(self, name: str, speed: float, entity: Entity, transition_dynamics: TransitionDynamics, value_type='delta', continuous=True):
        """ initalizes RelativeSpeedAction

        Parameters
        ----------
            speed (float): the speed wanted

            target (str): the name of the relative target (used for relative speed)

            transition_dynamics (TransitionDynamics): how the change should be made

            value_type (str): the type of relative speed wanted (used for relative speed)

            continuous (bool): if the controller tries to keep the relative speed

        """
        super().__init__(name, self._action_type)
        self.speed = speed
        self.target = entity
        self.value_type = value_type
        if not isinstance(continuous, bool):
            raise TypeError('continuous input not of type bool')

        if not isinstance(transition_dynamics, TransitionDynamics):
            raise TypeError('transition_dynamics input not of type TransitionDynamics')
        self.transition_dynamics = transition_dynamics
        self.continuous = continuous


