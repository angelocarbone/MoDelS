from .enumerations import e_DynamicsShapes, e_DynamicsDimension, e_ReferenceContext


class DynamicsConstrains:
    """ DynamicsConstrains is used by triggers

        Parameters
        ----------
            max_acceleration (float): maximum acceleration allowed

            max_deceleration (float): maximum deceleration allowed

            max_speed (float): maximum speed allowed

        Attributes
        ----------
            max_acceleration (float): maximum acceleration allowed

            max_deceleration (float): maximum deceleration allowed

            max_speed (float): maximum speed allowed

        Methods
        -------
            is_filled()
                check is any constraints are set

            get_element()
                Returns the full ElementTree of the class

            get_attributes()
                Returns a dictionary of all attributes of the class

    """

    def __init__(self, max_acceleration=None, max_deceleration=None, max_speed=None):
        """ initalize DynamicsConstrains

        """

        self.max_acceleration = max_acceleration
        self.max_deceleration = max_deceleration
        self.max_speed = max_speed


class TransitionDynamics:
    """ TransitionDynamics is used to define how the dynamics of a change

        Parameters
        ----------
            shape (DynamicsShapes): shape of the transition

            dimension (DynamicsDimension): the dimension of the transition (rate, time or distance)

            value (float): the value of the dynamics (time rate or distance)


        Attributes
        ----------
            shape (DynamicsShapes): shape of the transition

            dimension (DynamicsDimension): the dimension of the transition (rate, time or distance)

            value (float): the value of the dynamics (time rate or distance)

        Methods
        -------
            get_element()
                Returns the full ElementTree of the class

            get_attributes()
                Returns a dictionary of all attributes of the class

    """

    def __init__(self, shape: e_DynamicsShapes, dimension: e_DynamicsDimension, value):
        """
            Parameters
            ----------
                shape (e_DynamicsShapes): shape of the transition

                dimension (e_DynamicsDimension): the dimension of the transition (rate, time or distance)

                value (float): the value of the dynamics (time rate or distance)

        """
        if not hasattr(e_DynamicsShapes, str(shape)):
            raise TypeError('{0}; is not a valid shape.'.format(shape))

        self.shape = shape
        if not hasattr(e_DynamicsDimension, str(dimension)):
            raise ValueError('{0} is not a valid dynamics dimension'.format(dimension))
        self.dimension = dimension
        self.value = value


class Orientation:
    def __init__(self, h: float, p: float, r: float, reference_context: e_ReferenceContext = e_ReferenceContext.absolute):
        self.h = h
        self.p = p
        self.r = r
        self.reference_context = reference_context


class Axles:
    """
    A set of the axles of a cf_vehicle. A cf_vehicle must have a front axle and a rear axle. It might have additional axles.

    """
    def __init__(self, max_steer: float, track_width: float, wheel_diameter: float, x_pos: float, z_pos: float):
        self._max_steer = max_steer
        self._track_width = track_width
        self._wheel_diameter = wheel_diameter
        self._x_pos = x_pos
        self._z_pos = z_pos


class BoundingBox:
    """
    Defines geometric properties of the entities as a simplified three dimensional bounding box.
    """
    def __init__(self, height: float, length: float, width: float, x: float, y: float, z: float):
        self._height = height
        self._length = length
        self._width = width
        self._x = x
        self._y = y
        self._z = z


class Dynamics:
    def __init__(self, max_acceleration: float, max_deceleration: float, max_speed: float):
        self._max_acceleration = max_acceleration
        self._max_deceleration = max_deceleration
        self._max_speed = max_speed


class Position:
    def __init__(self):
        pass


class LanePosition(Position):
    def __init__(self, lane_id: str, offset: float, road_id: str, s: float, orientation: Orientation):
        super().__init__()
        self.lane_id = lane_id
        self.offset = offset
        self.road_id = road_id
        self.s = s
        self.orientation = orientation


class RoadPosition(Position):
    def __init__(self, road_id: str, s: float, t: float, orientation: Orientation):
        super().__init__()
        self.road_id = road_id
        self.s = s
        self.t = t
        self.orientation = orientation
