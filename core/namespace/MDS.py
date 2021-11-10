from rdflib.term import URIRef
from rdflib.namespace import DefinedNamespace, Namespace


class MDS(DefinedNamespace):
    """
        Moral Deliberation Scenes (MoDelS -> MDS) vocabulary

        Moral Deliberation Scenes (MDS) RDF vocabulary, described using W3C RDF Schema and the Web Ontology Language.

        Generated from:
        Date: 2020-05-26 14:20:01.597998

    """
    _fail = True

    # Classes
    # http://www.angelocarbone.com/ontologies/MoDO#
    AggressiveDriving: URIRef
    AvoidingConflict: URIRef
    ImproperManeuver: URIRef
    ImproperStoppingOrDecelerating: URIRef
    SpeedRelatedError: URIRef
    PoorLateralControl: URIRef
    PoorLongitudinalControl: URIRef
    DistractionError: URIRef
    RecognitionFailure: URIRef
    IllegalManeuver: URIRef
    IntentionalIntersectionViolation: URIRef
    SpeedViolation: URIRef
    UnintentionalIntersectionViolation: URIRef

    # LateralAction -> {LaneChangeAction, LateralDistanceAction}
    LateralAction: URIRef
    # + LaneChangeAction
    LaneChangeAction: URIRef
    ShortDistanceLaneChangeAction: URIRef
    LongDistanceLaneChangeAction: URIRef
    ShortTimeLaneChangeAction: URIRef
    LongTimeLaneChangeAction: URIRef
    # + LateralDistanceAction
    LateralDistanceAction: URIRef
    IncreaseLateralDistanceAction: URIRef
    ReduceLateralDistanceAction: URIRef
    SameLateralDistanceAction: URIRef

    # LongitudinalAction -> {LongitudinalDistanceAction, SpeedAction}
    LongitudinalAction: URIRef
    # + LongitudinalDistanceAction
    LongitudinalDistanceAction: URIRef
    IncreaseLongitudinalDistanceAction: URIRef
    ReduceLongitudinalDistanceAction: URIRef
    SameLongitudinalDistanceAction: URIRef
    # + SpeedAction
    SpeedAction: URIRef
    IncreaseSpeedAction: URIRef
    OvertakeSpeedAction: URIRef
    ReduceSpeedAction: URIRef
    SameSpeedAction: URIRef
    ZeroSpeedAction: URIRef

    # TeleportAction
    TeleportAction: URIRef

    # Properties
    # http://www.angelocarbone.com/ontologies/MoDO#
    isCausedBy: URIRef
    errorTriggerAction: URIRef
    duringAction: URIRef
    errorTriggerAction: URIRef

    # Individuals

    # Decision Error -> Avoiding Collision
    de_ac_01: URIRef
    de_ac_02: URIRef
    de_ac_03: URIRef
    de_ac_04: URIRef
    # Decision Error -> Improper Maneuver
    de_im_01: URIRef
    de_im_02: URIRef
    de_im_03: URIRef
    de_im_04: URIRef
    de_im_05: URIRef
    de_im_06: URIRef
    de_im_07: URIRef
    # Decision Error -> Improper Stopping or Decelerating
    de_isd_01: URIRef
    de_isd_02: URIRef
    # Decision Error -> Speed Related Error
    de_sr_01: URIRef
    de_sr_02: URIRef
    de_sr_03: URIRef
    # Performance Error -> Poor Lateral Control
    pe_plc_01: URIRef
    pe_plc_02: URIRef
    # Performance Error -> Poor Longitudinal Control
    pe_plongc_01: URIRef
    # Recognition Error -> Distraction Error
    re_d_01: URIRef
    re_d_02: URIRef
    # Recognition Error -> Recognition Failure
    re_rf_01: URIRef
    re_rf_02: URIRef
    re_rf_03: URIRef
    re_rf_04: URIRef
    re_rf_05: URIRef
    re_rf_06: URIRef
    re_rf_07: URIRef
    re_rf_08: URIRef
    # Violation -> Intentional Intersection Violation
    v_iiv_01: URIRef
    v_iiv_02: URIRef
    v_iiv_03: URIRef
    v_iiv_04: URIRef
    v_iiv_05: URIRef
    # Violation -> Illegal Maneuver
    v_im_01: URIRef
    v_im_02: URIRef
    # Violation -> Speed Violation
    v_sv_01: URIRef
    # Violation -> Unintentional Intersection Violation
    v_uiv_01: URIRef

    # Human Factor -> Experience Factor
    DrivingExperience: URIRef
    RoadAreaUnfamiliarity: URIRef
    VehicleUnfamiliarity: URIRef
    # Human Factor -> Mental or Emotional Factor
    Distraction: URIRef
    EmotionalUpset: URIRef
    Frustration: URIRef
    InHurry: URIRef
    Panic: URIRef
    PressureOrStrain: URIRef
    SelfConfidence: URIRef
    Uncertainty: URIRef
    # Human Factor -> Physical or Physiological Factor
    AlcoholImpairment: URIRef
    Deafness: URIRef
    Drowsy: URIRef
    DrugImpairment: URIRef
    Fatigued: URIRef
    ReducedVision: URIRef
    # Vehicle Factor
    BrakeProblem: URIRef
    EngineSystemFailure: URIRef
    FunctionalFailure: URIRef
    LightingProblem: URIRef
    SensorFailure: URIRef
    SteeringProblem: URIRef
    TireWheelProblem: URIRef
    VisionObscured: URIRef

    _NS = Namespace("http://angelocarbone.com/rules/MoDelS#")
