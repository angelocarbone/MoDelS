"""
    Collection of the enumerations defined in MoDelS, and used in the MoDO ontology.
"""
XMLNS = 'http://www.w3.org/2001/XMLSchema-instance'
XSI = 'OpenScenario.xsd'

from enum import Enum, auto
# from .exceptions import OpenSCENARIOVersionError
from os import error

_MINOR_VERSION = 1


class VersionBase:
    """ base class for checking different versions of OpenSCENARIO """
    version_major = 1
    version_minor = _MINOR_VERSION

    def isVersion(self, major=1, minor=1):
        return major == self.version_major and minor == self.version_minor


class _MoDelSEnum(VersionBase):
    """ custom "enum" class to be able to handle different versions of the enums in MoDelS

        Parameters
        ----------
            name (str): enum name

            class_name (str): name of the enum class (only used for printouts to help debugging)

            min_minor_version (int): how the relative distance should be calculated
                Default: 0

            max_minor_version (int): the max "minor version" where the enum is valid
                Default: Current Supported Version

        Attributes
        ----------
            name (str): enum name

            class_name (str): name of the enum class (only used for printouts to help debugging)

            min_minor_version (int): how the relative distance should be calculated

            max_minor_version (int): the max "minor version" where the enum is valid

        Methods
        -------
            get_name()
                Returns the correct string of the Enum, will take care of versions

    """

    def __init__(self, class_name, name, pretty_name="", description="", min_minor_version=0, max_minor_version=_MINOR_VERSION):
        """ initalize the _MoDelSEnum

            Parameters
            ----------
                name (str): enum name

                class_name (str): name of the enum class (only used for printouts to help debugging)

                min_minor_version (int): how the relative distance should be calculated
                    Default: 0

                max_minor_version (int): the max "minor version" where the enum is valid
                    Default: Current Supported Version
        """

        self.name = name
        self.class_name = class_name
        self.pretty_name = pretty_name == "" if name else pretty_name
        self.description = description
        self.min_minor_version = min_minor_version
        self.max_minor_version = max_minor_version

    def __eq__(self, other):
        if isinstance(other, _MoDelSEnum):
            if self.name == other.name and \
                    self.class_name == other.class_name:
                return True
        return False

    def get_name(self):
        """ method that should be used when using the _MoDelSEnum to get the string, will check version of the enum to see if it is used correctly with the used version

            Returns
            -------
            name (str)
        """

        # if self.min_minor_version > self.version_minor:
        #     raise OpenSCENARIOVersionError(self.class_name + '.' + self.name + ' is not part of OpenSCENARIO V' + str(
        #         self.version_major) + '.' + str(self.version_minor) + ', was introduced in V' + str(
        #         self.version_major) + '.' + str(self.min_minor_version))
        # elif self.max_minor_version < self.version_minor:
        #     raise OpenSCENARIOVersionError(self.class_name + '.' + self.name + ' is not part of OpenSCENARIO V' + str(
        #         self.version_major) + '.' + str(self.version_minor) + ', was deprecated in V' + str(
        #         self.version_major) + '.' + str(self.max_minor_version))
        # return self.name

    def __str__(self):
        return self.name


class e_Vehicle:
    Bus = _MoDelSEnum("Vehicle", "Bus")
    Bike = _MoDelSEnum("Vehicle", "Bike")
    Car = _MoDelSEnum("Vehicle", "Car")
    Motorbike = _MoDelSEnum("Vehicle", "Motorbike")
    Train = _MoDelSEnum("Vehicle", "Train")
    Trailer = _MoDelSEnum("Vehicle", "Trailer")
    Van = _MoDelSEnum("Vehicle", "Van")
    Tram = _MoDelSEnum("Vehicle", "Tram")
    Semitrailer = _MoDelSEnum("Vehicle", "Semitrailer")
    Truck = _MoDelSEnum("Vehicle", "Truck")

    @classmethod
    def name(cls):
        return "Vehicle"


class e_Pedestrian:
    Animal = _MoDelSEnum("Pedestrian", "Animal")
    Wheelchair = _MoDelSEnum("Pedestrian", "Wheelchair")
    People = _MoDelSEnum("Pedestrian", "People")

    @classmethod
    def name(cls):
        return "Pedestrian"


class e_EntityType:
    Vehicle = e_Vehicle
    Pedestrian = e_Pedestrian
    Driver = _MoDelSEnum("EntityType", "Driver")
    Passenger = _MoDelSEnum("EntityType", "Passenger")


class e_Relation:
    class e_connectedTo:
        junctionToJunction = _MoDelSEnum("connectedTo", "junctionToJunction")
        sectionToJunction = _MoDelSEnum("connectedTo", "sectionToJunction")
        sectionToSection = _MoDelSEnum("connectedTo", "sectionToSection")

        @classmethod
        def name(cls):
            return "connectedTo"

    class e_hasLane:
        hasLeftLane = _MoDelSEnum("hasLane", "hasLeftLane")
        hasRightLane = _MoDelSEnum("hasLane", "hasRightLane")

        @classmethod
        def name(cls):
            return "hasLane"

    class e_temporalRelation:
        before = _MoDelSEnum("temporalRelation", "before")
        equals = _MoDelSEnum("temporalRelation", "equals")
        overlaps = _MoDelSEnum("temporalRelation", "overlaps")
        meets = _MoDelSEnum("temporalRelation", "meets")
        during = _MoDelSEnum("temporalRelation", "during")
        starts = _MoDelSEnum("temporalRelation", "starts")
        finishes = _MoDelSEnum("temporalRelation", "finishes")

        @classmethod
        def name(cls):
            return "temporalRelation"

    class e_hasPosition:
        hasLanePosition = _MoDelSEnum("hasPosition", "hasLanePosition")
        hasRoadPosition = _MoDelSEnum("hasPosition", "hasRoadPosition")

        @classmethod
        def name(cls):
            return "hasPosition"

    class e_impairs:
        impairsDriver = _MoDelSEnum("impaires", "impairsDriver")
        impairsEntity = _MoDelSEnum("impaires", "impairsEntity")

        @classmethod
        def name(cls):
            return "impairs"

    class e_isImpaired:
        driverIsImpaired = _MoDelSEnum("isImpaired", "driverIsImpaired")
        entityIsImpaired = _MoDelSEnum("isImpaired", "entityIsImpaired")

        @classmethod
        def name(cls):
            return "isImpaired"

    class e_isOn:
        class e_isOnRoad:
            isOnCrosswalk = _MoDelSEnum("isOnRoad", "isOnCrosswalk")
            isOnIntersection = _MoDelSEnum("isOnRoad", "isOnIntersection")
            isOnLane = _MoDelSEnum("isOnRoad", "isOnLane")

            @classmethod
            def name(cls):
                return "isOnRoad"

        class e_isOnVehicle:
            driverIsOnVehicle = _MoDelSEnum("isOnVehicle", "driverIsOnVehicle")
            passengerIsOnVehicle = _MoDelSEnum("isOnVehicle", "passengerIsOnVehicle")

            @classmethod
            def name(cls):
                return "isOnVehicle"

        isOnRoad = e_isOnRoad
        isOnVehicle = e_isOnVehicle

    class e_objectOf:
        objectOfAction = _MoDelSEnum("objectOf", "objectOfAction")
        objectOfEvent = _MoDelSEnum("objectOf", "objectOfEvent")

        @classmethod
        def name(cls):
            return "objectOf"

    class e_partOf:
        junctionPartOfRoad = _MoDelSEnum("partOf", "junctionPartOfRoad")
        lanePartOfSection = _MoDelSEnum("partOf", "lanePartOfSection")
        miscStaticObjectPartOfRoad = _MoDelSEnum("partOf", "miscStaticObjectPartOfRoad")
        sectionPartOfRoad = _MoDelSEnum("partOf", "sectionPartOfRoad")

        @classmethod
        def name(cls):
            return "partOf"

    class e_performs:
        actionIsPerformed = _MoDelSEnum("performs", "actionIsPerformed")
        causesEvent = _MoDelSEnum("performs", "causesEvent")
        eventIsPerformed = _MoDelSEnum("performs", "eventIsPerformed")
        notPerformsAction = _MoDelSEnum("performs", "notPerformsAction")
        performsAction = _MoDelSEnum("performs", "performsAction")

        @classmethod
        def name(cls):
            return "performs"

    class e_triggers:
        actionTriggersAction = _MoDelSEnum("triggers", "actionTriggersAction")
        actionTriggersEvent = _MoDelSEnum("triggers", "actionTriggersEvent")
        eventTriggersAction = _MoDelSEnum("triggers", "eventTriggersAction")
        eventTriggersEvent = _MoDelSEnum("triggers", "eventTriggersEvent")

        @classmethod
        def name(cls):
            return "triggers"

    connectedTo = e_connectedTo
    drivesWith = _MoDelSEnum("Relation", "drivesWith")
    hasDriver = _MoDelSEnum("Relation", "hasDriver")
    hasDrivingSkill = _MoDelSEnum("Relation", "hasDrivingSkill")
    hasLane = e_hasLane
    hasPassenger = _MoDelSEnum("Relation", "hasPassenger")
    haPosition = e_hasPosition
    hasSafetyEquipment = _MoDelSEnum("Relation", "hasSafetyEquipment")
    impairs = e_impairs
    isBehindOf = _MoDelSEnum("Relation", "isBehindOf")
    isCausedBy = _MoDelSEnum("Relation", "isCausedBy")
    isCauseOf = _MoDelSEnum("Relation", "isCauseOf")
    isDrivingSkill = _MoDelSEnum("Relation", "isDrivingSkill")
    isFrontOf = _MoDelSEnum("Relation", "isFrontOf")
    isImpaired = e_isImpaired
    isLeftOf = _MoDelSEnum("Relation", "isLeftOf")
    isOn = e_isOn
    isRightOf = _MoDelSEnum("Relation", "isRightOf")
    isSafetyEquipment = _MoDelSEnum("Relation", "isSafetyEquipment")
    objectOf = e_objectOf
    sendSignal = _MoDelSEnum("Relation", "sendSignal")
    partOf = e_partOf
    performs = e_performs
    temporalRelation = e_temporalRelation
    triggers = e_triggers

    @classmethod
    def name(cls):
        return "Relation"


class e_ActionType:
    AbsoluteSpeedAction = _MoDelSEnum("Action", "AbsoluteSpeedAction")
    RelativeSpeedAction = _MoDelSEnum("Action", "RelativeSpeedAction")
    LongitudinalDistanceAction = _MoDelSEnum("Action", "LongitudinalDistanceAction")

    # ---
    BeingAction = _MoDelSEnum("Action", "BeingAction")
    Screaming = _MoDelSEnum("Action", "Screaming")
    Talking = _MoDelSEnum("Action", "Talking")
    GlobalAction = _MoDelSEnum("Action", "GlobalAction")
    PrivateAction = _MoDelSEnum("Action", "PrivateAction")
    ActivateControllerAction = _MoDelSEnum("Action", "ActivateControllerAction")
    ControllerAction = _MoDelSEnum("Action", "ControllerAction")
    LateralAction = _MoDelSEnum("Action", "LateralAction")
    LaneChangeAction = _MoDelSEnum("Action", "LaneChangeAction")
    LongDistanceLaneChangeAction = _MoDelSEnum("Action", "LongDistanceLaneChangeAction")
    LongTimeLaneChangeAction = _MoDelSEnum("Action", "LongTimeLaneChangeAction")
    ShortDistanceLaneChangeAction = _MoDelSEnum("Action", "ShortDistanceLaneChangeAction")
    ShortTimeLaneChangeAction = _MoDelSEnum("Action", "ShortTimeLaneChangeAction")
    LateralDistanceAction = _MoDelSEnum("Action", "LateralDistanceAction")
    IncreaseLateralDistanceAction = _MoDelSEnum("Action", "IncreaseLateralDistanceAction")
    ReduceLateralDistanceAction = _MoDelSEnum("Action", "ReduceLateralDistanceAction")
    SameLateralDistanceAction = _MoDelSEnum("Action", "SameLateralDistanceAction")
    LongitudinalAction = _MoDelSEnum("Action", "LongitudinalAction")
    IncreaseLongitudinalDistanceAction = _MoDelSEnum("Action", "IncreaseLongitudinalDistanceAction")
    ReduceLongitudinalDistanceAction = _MoDelSEnum("Action", "ReduceLongitudinalDistanceAction")
    SameLongitudinalDistanceAction = _MoDelSEnum("Action", "SameLongitudinalDistanceAction")
    SpeedAction = _MoDelSEnum("Action", "SpeedAction")
    IncreaseSpeedAction = _MoDelSEnum("Action", "IncreaseSpeedAction")
    OvertakeSpeedAction = _MoDelSEnum("Action", "OvertakeSpeedAction")
    ReduceSpeedAction = _MoDelSEnum("Action", "ReduceSpeedAction")
    SameSpeedAction = _MoDelSEnum("Action", "SameSpeedAction")
    ZeroSpeedAction = _MoDelSEnum("Action", "ZeroSpeedAction")
    RoutingAction = _MoDelSEnum("Action", "RoutingAction")
    SynchronizeAction = _MoDelSEnum("Action", "SynchronizeAction")
    TeleportAction = _MoDelSEnum("Action", "TeleportAction")
    VisibilityAction = _MoDelSEnum("Action", "VisibilityAction")
    UserDefinedAction = _MoDelSEnum("Action", "UserDefinedAction")

    # ***
    # To delete ?
    #
    # Approaching = _MoDelSEnum("Action", "Approaching")
    # AvoidingCollision = _MoDelSEnum("Action", "AvoidingCollision")
    # Blocking = _MoDelSEnum("Action", "Blocking")
    # Colliding = _MoDelSEnum("Action", "Colliding")
    # Crossing = _MoDelSEnum("Action", "Crossing")
    # CuttingIn = _MoDelSEnum("Action", "CuttingIn")
    # CuttingOut = _MoDelSEnum("Action", "CuttingOut")
    # Decelerating = _MoDelSEnum("Action", "Decelerating")
    # DrivingInOppositeDirection = _MoDelSEnum("Action", "DrivingInOppositeDirection")
    # DrivingStraight = _MoDelSEnum("Action", "DrivingStraight")
    # FallingBehind = _MoDelSEnum("Action", "FallingBehind")
    # FallingDown = _MoDelSEnum("Action", "FallingDown")
    # Following = _MoDelSEnum("Action", "Following")
    # GlidingOnWheels = _MoDelSEnum("Action", "GlidingOnWheels")
    # LaneChanging = _MoDelSEnum("Action", "LaneChanging")
    # LaneChangingLeft = _MoDelSEnum("Action", "LaneChangingLeft")
    # LaneChangingRight = _MoDelSEnum("Action", "LaneChangingRight")
    # LoosingControl = _MoDelSEnum("Action", "LoosingControl")
    # Overtaking = _MoDelSEnum("Action", "Overtaking")
    # Parked = _MoDelSEnum("Action", "Parked")
    # Parking = _MoDelSEnum("Action", "Parking")
    # Passing = _MoDelSEnum("Action", "Passing")
    # Reversing = _MoDelSEnum("Action", "Reversing")
    # Rising = _MoDelSEnum("Action", "Rising")
    # Running = _MoDelSEnum("Action", "Running")
    # Sitting = _MoDelSEnum("Action", "Sitting")
    # Standing = _MoDelSEnum("Action", "Standing")
    # Standstill = _MoDelSEnum("Action", "Standstill")
    # Stopped = _MoDelSEnum("Action", "Stopped")
    # Stopping = _MoDelSEnum("Action", "Stopping")
    # Swerving = _MoDelSEnum("Action", "Swerving")
    # Turning = _MoDelSEnum("Action", "Turning")
    # TurningLeft = _MoDelSEnum("Action", "TurningLeft")
    # TurningRight = _MoDelSEnum("Action", "TurningRight")
    # uTurning = _MoDelSEnum("Action", "uTurning")
    # Waiting = _MoDelSEnum("Action", "Waiting")
    # Walking = _MoDelSEnum("Action", "Walking")

    @classmethod
    def name(cls):
        return "Action"


class e_ExperienceFactor:
    DrivingExperience = _MoDelSEnum("ExperienceFactor", "DrivingExperience")
    RoadAreaUnfamiliarity = _MoDelSEnum("ExperienceFactor", "RoadAreaUnfamiliarity")
    VehicleUnfamiliarity = _MoDelSEnum("ExperienceFactor", "VehicleUnfamiliarity")

    @classmethod
    def name(cls):
        return "ExperienceFactor"

    @classmethod
    def all(cls):
        import inspect
        attributes = inspect.getmembers(cls, lambda a: not(inspect.isroutine(a)))
        return [a for a in attributes if not (a[0].startswith('__') and a[0].endswith('__'))]


class e_MentalOrEmotionalFactor:
    Distraction = _MoDelSEnum("MentalOrEmotionalFactor", "Distraction")
    EmotionalUpset = _MoDelSEnum("MentalOrEmotionalFactor", "EmotionalUpset")
    Frustration = _MoDelSEnum("MentalOrEmotionalFactor", "Frustration")
    InHurry = _MoDelSEnum("MentalOrEmotionalFactor", "InHurry")
    Panic = _MoDelSEnum("MentalOrEmotionalFactor", "Panic")
    PressureOrStrain = _MoDelSEnum("MentalOrEmotionalFactor", "PressureOrStrain")
    SelfConfidence = _MoDelSEnum("MentalOrEmotionalFactor", "SelfConfidence")
    Uncertainty = _MoDelSEnum("MentalOrEmotionalFactor", "Uncertainty")

    @classmethod
    def name(cls):
        return "ExperienceFactor"

    @classmethod
    def all(cls):
        import inspect
        attributes = inspect.getmembers(cls, lambda a: not (inspect.isroutine(a)))
        return [a for a in attributes if not (a[0].startswith('__') and a[0].endswith('__'))]


class e_PhyOrPhyFactor:
    AlcoholImpairment = _MoDelSEnum("PhyOrPhyFactor", "AlcoholImpairment")
    Deafness = _MoDelSEnum("PhyOrPhyFactor", "Deafness")
    Drowsy = _MoDelSEnum("PhyOrPhyFactor", "Drowsy")
    DrugImpairment = _MoDelSEnum("PhyOrPhyFactor", "DrugImpairment")
    Fatigued = _MoDelSEnum("PhyOrPhyFactor", "Fatigued")
    ReducedVision = _MoDelSEnum("PhyOrPhyFactor", "ReducedVision")

    @classmethod
    def name(cls):
        return "ExperienceFactor"

    @classmethod
    def all(cls):
        import inspect
        attributes = inspect.getmembers(cls, lambda a: not (inspect.isroutine(a)))
        return [a for a in attributes if not (a[0].startswith('__') and a[0].endswith('__'))]


class e_HumanFactor:
    ExperienceFactor = e_ExperienceFactor
    MentalOrEmotionalFactor = e_MentalOrEmotionalFactor
    PhyOrPhyFactor = e_PhyOrPhyFactor

    @classmethod
    def name(cls):
        return "HumanFactor"


class e_VehicleFactor:
    BrakeProblem = _MoDelSEnum("VehicleFactor", "BrakeProblem")
    EngineSystemFailure = _MoDelSEnum("VehicleFactor", "EngineSystemFailure")
    FunctionalFailure = _MoDelSEnum("VehicleFactor", "FunctionalFailure")
    LightingProblem = _MoDelSEnum("VehicleFactor", "LightingProblem")
    SensorFailure = _MoDelSEnum("VehicleFactor", "SensorFailure")
    SteeringProblem = _MoDelSEnum("VehicleFactor", "SteeringProblem")
    TireWheelProblem = _MoDelSEnum("VehicleFactor", "TireWheelProblem")
    VisionObscured = _MoDelSEnum("VehicleFactor", "VisionObscured")

    @classmethod
    def name(cls):
        return "HumanFactor"


class e_CausalFactorType:

    HumanFactor = e_HumanFactor
    VehicleFactor = e_VehicleFactor

    @classmethod
    def name(cls):
        return "CausalFactor"


class e_DecisionError:
    AggressiveDriving = _MoDelSEnum("DecisionError", "AggressiveDriving")
    AvoidingConflict = _MoDelSEnum("DecisionError", "AvoidingConflict")
    ImproperManeuver = _MoDelSEnum("DecisionError", "ImproperManeuver")
    ImproperStoppingOrDecelerating = _MoDelSEnum("DecisionError", "ImproperStoppingOrDecelerating")
    SpeedRelatedError = _MoDelSEnum("DecisionError", "SpeedRelatedError")

    @classmethod
    def name(cls):
        return "DecisionError"


class e_RecognitionError:
    _name = "RecognitionError"

    DistractionError = _MoDelSEnum(_name, "DistractionError")
    RecognitionFailure = _MoDelSEnum(_name, "RecognitionFailure")

    @classmethod
    def name(cls):
        return cls._name


class e_PerformanceError:
    _name = "PerformanceError"

    PoorLateralControl = _MoDelSEnum(_name, "PoorLateralControl")
    PoorLongitudinalControl = _MoDelSEnum(_name, "PoorLongitudinalControl")

    @classmethod
    def name(cls):
        return cls._name


class e_Violation:
    _name = "Violation"

    IllegalManeuver = _MoDelSEnum(_name, "IllegalManeuver")
    IntentionalIntersectionViolation = _MoDelSEnum(_name, "IllegalManeuver")
    SpeedViolation = _MoDelSEnum(_name, "IllegalManeuver")
    UnintentionalIntersectionViolation = _MoDelSEnum(_name, "IllegalManeuver")

    @classmethod
    def name(cls):
        return cls._name


class e_DrivingErrorType:
    DecisionError = e_DecisionError
    RecognitionError = e_RecognitionError
    PerformanceError = e_PerformanceError
    Violation = e_Violation

    @classmethod
    def name(cls):
        return "DrivingError"


class e_LineType:
    _name = "LineType"

    solid = _MoDelSEnum(_name, "solid")
    dashed = _MoDelSEnum(_name, "dashed")
    solid_dashed = _MoDelSEnum(_name, "solid_dashed")
    dashed_solid = _MoDelSEnum(_name, "dashed_solid")
    none = _MoDelSEnum(_name, "none")

    @classmethod
    def name(cls):
        return cls._name


class e_ReferenceContext:
    _name = "ReferenceContext"

    absolute = _MoDelSEnum(_name, "absolute")
    relative = _MoDelSEnum(_name, "relative")

    @classmethod
    def name(cls):
        return cls._name


class e_DynamicsShapes:
    """ Enum for DynamicsShapes
    """
    _name = "ReferenceContext"

    linear = _MoDelSEnum('DynamicsShapes', 'linear')
    cubic = _MoDelSEnum('DynamicsShapes', 'cubic')
    sinusoidal = _MoDelSEnum('DynamicsShapes', 'sinusoidal')
    step = _MoDelSEnum('DynamicsShapes', 'step')

    @classmethod
    def name(cls):
        return cls._name

    @classmethod
    def by_name(cls, name: str):
        if hasattr(cls, name):
            return _MoDelSEnum('DynamicsShapes', name)


class e_DynamicsDimension:
    """ Enum for DynamicsDimension
    """
    _name = "ReferenceContext"

    rate = _MoDelSEnum('DynamicsDimension', 'rate')
    time = _MoDelSEnum('DynamicsDimension', 'time')
    distance = _MoDelSEnum('DynamicsDimension', 'distance')

    @classmethod
    def name(cls):
        return cls._name

    @classmethod
    def by_name(cls, name: str):
        if hasattr(cls, name):
            return _MoDelSEnum('DynamicsDimension', name)

# ------------------------------------------------------------


class CloudState:
    """ Enum for CloudState
    """
    skyOff = _MoDelSEnum('CloudState', 'skyOff')
    free = _MoDelSEnum('CloudState', 'free')
    cloudy = _MoDelSEnum('CloudState', 'cloudy')
    overcast = _MoDelSEnum('CloudState', 'overcast')
    rainy = _MoDelSEnum('CloudState', 'rainy')


class ConditionEdge():
    """ Enum for ConditionEdge
    """
    rising = _MoDelSEnum('ConditionEdge', 'rising')
    falling = _MoDelSEnum('ConditionEdge', 'falling')
    risingOrFalling = _MoDelSEnum('ConditionEdge', 'risingOrFalling')
    none = _MoDelSEnum('ConditionEdge', 'none')


class FollowMode():
    """ Enum for FollowMode
    """
    position = _MoDelSEnum('FollowMode', 'position')
    follow = _MoDelSEnum('FollowMode', 'follow')


class MiscObjectCategory():
    """ Enum for MiscObjectCategory
    """

    none = _MoDelSEnum('MiscObjectCategory', 'none')
    obstacle = _MoDelSEnum('MiscObjectCategory', 'obstacle')
    pole = _MoDelSEnum('MiscObjectCategory', 'pole')
    tree = _MoDelSEnum('MiscObjectCategory', 'tree')
    vegetation = _MoDelSEnum('MiscObjectCategory', 'vegetation')
    barrier = _MoDelSEnum('MiscObjectCategory', 'barrier')
    building = _MoDelSEnum('MiscObjectCategory', 'building')
    parkingSpace = _MoDelSEnum('MiscObjectCategory', 'parkingSpace')
    patch = _MoDelSEnum('MiscObjectCategory', 'patch')
    railing = _MoDelSEnum('MiscObjectCategory', 'railing')
    grafficIsland = _MoDelSEnum('MiscObjectCategory', 'grafficIsland')
    crosswalk = _MoDelSEnum('MiscObjectCategory', 'crosswalk')
    streetLamp = _MoDelSEnum('MiscObjectCategory', 'streetLamp')
    gantry = _MoDelSEnum('MiscObjectCategory', 'gantry')
    soundBarrier = _MoDelSEnum('MiscObjectCategory', 'soundBarrier')
    wind = _MoDelSEnum('MiscObjectCategory', 'wind', max_minor_version=0)
    roadMark = _MoDelSEnum('MiscObjectCategory', 'roadMark')


class ObjectType():
    """ Enum for ObjectType
    """
    pedestrian = _MoDelSEnum('ObjectType', 'pedestrian')
    vehicle = _MoDelSEnum('ObjectType', 'cf_vehicle')
    miscellaneous = _MoDelSEnum('ObjectType', 'miscellaneous')
    external = _MoDelSEnum('ObjectType', 'external', min_minor_version=1)


class ParameterType():
    """ Enum for ParameterType
    """
    integer = _MoDelSEnum('ParameterType', 'integer')
    double = _MoDelSEnum('ParameterType', 'double')
    string = _MoDelSEnum('ParameterType', 'string')
    unsighedInt = _MoDelSEnum('ParameterType', 'unsighedInt')
    unsighedShort = _MoDelSEnum('ParameterType', 'unsighedShort')
    boolean = _MoDelSEnum('ParameterType', 'boolean')
    dateTime = _MoDelSEnum('ParameterType', 'dateTime')


class PedestrianCategory():
    """ Enum for PedestrianCategory
    """
    pedestrian = _MoDelSEnum('PedestrianCategory', 'pedestrian')
    wheelchair = _MoDelSEnum('PedestrianCategory', 'wheelchair')
    animal = _MoDelSEnum('PedestrianCategory', 'animal')


class PrecipitationType():
    """ Enum for PercipitationType
    """
    dry = _MoDelSEnum('PrecipitationType', 'dry')
    rain = _MoDelSEnum('PrecipitationType', 'rain')
    snow = _MoDelSEnum('PrecipitationType', 'snow')


class Priority():
    """ Enum for Priority
    """
    overwrite = _MoDelSEnum('Priority', 'overwrite')
    skip = _MoDelSEnum('Priority', 'skip')
    parallel = _MoDelSEnum('Priority', 'parallel')


class ReferenceContext():
    """ Enum for ReferenceContext
    """
    relative = _MoDelSEnum('ReferenceContext', 'relative')
    absolute = _MoDelSEnum('ReferenceContext', 'absolute')


class RelativeDistanceType():
    """ Enum for RelativeDistanceType
    """
    longitudinal = _MoDelSEnum('RelativeDistanceType', 'longitudinal')
    lateral = _MoDelSEnum('RelativeDistanceType', 'lateral')
    cartesianDistance = _MoDelSEnum('RelativeDistanceType', 'cartesianDistance', max_minor_version=0)
    euclidianDistance = _MoDelSEnum('RelativeDistanceType', 'euclidianDistance', min_minor_version=1)


class RouteStrategy():
    """ Enum for RouteStrategy
    """
    fastest = _MoDelSEnum('RouteStrategy', 'fastest')
    shortest = _MoDelSEnum('RouteStrategy', 'shortest')
    leastIntersections = _MoDelSEnum('RouteStrategy', 'leastIntersections')
    random = _MoDelSEnum('RouteStrategy', 'random')


class Rule():
    """ Enum for Rule
    """
    greaterThan = _MoDelSEnum('Rule', 'greaterThan')
    lessThan = _MoDelSEnum('Rule', 'lessThan')
    equalTo = _MoDelSEnum('Rule', 'equalTo')
    greaterOrEqual = _MoDelSEnum('Rule', 'greaterOrEqual', min_minor_version=1)
    lessOrEqual = _MoDelSEnum('Rule', 'lessOrEqual', min_minor_version=1)
    notEqualTo = _MoDelSEnum('Rule', 'notEqualTo', min_minor_version=1)


class SpeedTargetValueType():
    """ Enum for SpeedTargetValueType
    """
    delta = _MoDelSEnum('SpeedTargetValueType', 'delta')
    factor = _MoDelSEnum('SpeedTargetValueType', 'factor')


class StoryboardElementState():
    """ Enum for StoryboardElementState
    """
    startTransition = _MoDelSEnum('StoryboardElementState', 'startTransition')
    endTransition = _MoDelSEnum('StoryboardElementState', 'endTransition')
    stopTransition = _MoDelSEnum('StoryboardElementState', 'stopTransition')
    skipTransition = _MoDelSEnum('StoryboardElementState', 'skipTransition')
    completeState = _MoDelSEnum('StoryboardElementState', 'completeState')
    runningState = _MoDelSEnum('StoryboardElementState', 'runningState')
    standbyState = _MoDelSEnum('StoryboardElementState', 'standbyState')


class StoryboardElementType():
    """ Enum for StoryboardElementType
    """
    story = _MoDelSEnum('StoryboardElementType', 'story')
    act = _MoDelSEnum('StoryboardElementType', 'act')
    maneuver = _MoDelSEnum('StoryboardElementType', 'maneuver')
    event = _MoDelSEnum('StoryboardElementType', 'event')
    action = _MoDelSEnum('StoryboardElementType', 'action')
    maneuverGroup = _MoDelSEnum('StoryboardElementType', 'maneuverGroup')


class TriggeringEntitiesRule():
    """ Enum for TriggeringEntitiesRule
    """
    any = _MoDelSEnum('TriggeringEntitiesRule', 'any')
    all = _MoDelSEnum('TriggeringEntitiesRule', 'all')


class VehicleCategory():
    """ Enum for VehicleCategory
    """
    car = _MoDelSEnum('VehicleCategory', 'car')
    van = _MoDelSEnum('VehicleCategory', 'van')
    truck = _MoDelSEnum('VehicleCategory', 'truck')
    trailer = _MoDelSEnum('VehicleCategory', 'trailer')
    semitrailer = _MoDelSEnum('VehicleCategory', 'semitrailer')
    bus = _MoDelSEnum('VehicleCategory', 'bus')
    motorbike = _MoDelSEnum('VehicleCategory', 'motorbike')
    bicycle = _MoDelSEnum('VehicleCategory', 'bicycle')
    train = _MoDelSEnum('VehicleCategory', 'train')
    tram = _MoDelSEnum('VehicleCategory', 'tram')


class CoordinateSystem():
    """ Enum for CoordinateSystem
    """
    entity = _MoDelSEnum('CoordinateSystem', 'entity', min_minor_version=1)
    lane = _MoDelSEnum('CoordinateSystem', 'lane', min_minor_version=1)
    road = _MoDelSEnum('CoordinateSystem', 'road', min_minor_version=1)
    trajectory = _MoDelSEnum('CoordinateSystem', 'trajectory', min_minor_version=1)


class LateralDisplacement():
    any = _MoDelSEnum('LateralDisplacement', 'any', min_minor_version=1)
    leftToReferencedEntity = _MoDelSEnum('LateralDisplacement', 'leftToReferencedEntity', min_minor_version=1)
    rightToReferencedEntity = _MoDelSEnum('LateralDisplacement', 'rightToReferencedEntity', min_minor_version=1)


class LongitudinalDisplacement():
    any = _MoDelSEnum('LongitudinalDisplacement', 'any', min_minor_version=1)
    trailingReferencedEntity = _MoDelSEnum('LongitudinalDisplacement', 'trailingReferencedEntity', min_minor_version=1)
    leadingReferencedEntity = _MoDelSEnum('LongitudinalDisplacement', 'leadingReferencedEntity', min_minor_version=1)

