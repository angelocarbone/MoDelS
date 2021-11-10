from os.path import exists
from rdflib import Graph, Literal, RDF, RDFS, URIRef
from core.namespace.MDS import MDS
from config import RULE_DIR

# Create a Graph
g = Graph()

base_uri = "http://angelocarbone.com/rules/MoDelS#"
file_path = RULE_DIR + 'driving_error_to_action.ttl'
# LateralAction
# g.add((re_d_01, MDS.errorTriggerAction, MDS.ShortDistanceLaneChangeAction))
# g.add((re_d_01, MDS.errorTriggerAction, MDS.LongDistanceLaneChangeAction))
# g.add((re_d_01, MDS.errorTriggerAction, MDS.ShortTimeLaneChangeAction))
# g.add((re_d_01, MDS.errorTriggerAction, MDS.LongTimeLaneChangeAction))
#
# g.add((re_d_01, MDS.errorTriggerAction, MDS.IncreaseLateralDistanceAction))
# g.add((re_d_01, MDS.errorTriggerAction, MDS.ReduceLateralDistanceAction))
# g.add((re_d_01, MDS.errorTriggerAction, MDS.SameLateralDistanceAction))
#
#
# LongitudinalAction
# Following factory will be activated in scenarios when an entity follow other one.
# g.add((re_d_01, MDS.errorTriggerAction, MDS.LongitudinalDistanceAction))
# g.add((re_d_01, MDS.errorTriggerAction, MDS.IncreaseLongitudinalDistanceAction))
# g.add((re_d_01, MDS.errorTriggerAction, MDS.ReduceLongitudinalDistanceAction))
# g.add((re_d_01, MDS.errorTriggerAction, MDS.SameLongitudinalDistanceAction))
#
# g.add((re_d_01, MDS.errorTriggerAction, MDS.IncreaseSpeedAction))
# g.add((re_d_01, MDS.errorTriggerAction, MDS.OvertakeSpeedAction))
# g.add((re_d_01, MDS.errorTriggerAction, MDS.ReduceSpeedAction))
# g.add((re_d_01, MDS.errorTriggerAction, MDS.SameSpeedAction))
# g.add((re_d_01, MDS.errorTriggerAction, MDS.ZeroSpeedAction))


def generate_rules():
    # ***
    # Driver is distracted by internal secondary task or factor.
    # ***
    re_d_01 = URIRef(base_uri + "re_d_01")
    # Add triples using store's add() method.
    g.add((re_d_01, RDF.type, MDS.DistractionError))
    g.add((re_d_01, RDFS.comment, Literal("Driver is distracted by internal secondary task or factor.", lang="en")))
    g.add((re_d_01, MDS.duringAction, MDS.LongitudinalAction))
    # LateralAction
    g.add((re_d_01, MDS.errorTriggerAction, MDS.ShortDistanceLaneChangeAction))
    g.add((re_d_01, MDS.errorTriggerAction, MDS.LongDistanceLaneChangeAction))
    g.add((re_d_01, MDS.errorTriggerAction, MDS.ShortTimeLaneChangeAction))
    g.add((re_d_01, MDS.errorTriggerAction, MDS.LongTimeLaneChangeAction))
    #
    g.add((re_d_01, MDS.errorTriggerAction, MDS.IncreaseLateralDistanceAction))
    g.add((re_d_01, MDS.errorTriggerAction, MDS.ReduceLateralDistanceAction))
    g.add((re_d_01, MDS.errorTriggerAction, MDS.SameLateralDistanceAction))
    #
    # LongitudinalAction
    g.add((re_d_01, MDS.errorTriggerAction, MDS.IncreaseSpeedAction))
    g.add((re_d_01, MDS.errorTriggerAction, MDS.OvertakeSpeedAction))
    g.add((re_d_01, MDS.errorTriggerAction, MDS.ReduceSpeedAction))
    g.add((re_d_01, MDS.errorTriggerAction, MDS.SameSpeedAction))

    # ***
    # Driver is distracted by external factor.
    #
    re_d_02 = URIRef(base_uri + "re_d_02")
    # Add triples using store's add() method.
    g.add((re_d_02, RDF.type, MDS.DistractionError))
    g.add((re_d_02, RDFS.comment, Literal("Driver is distracted by external factor.", lang="en")))
    g.add((re_d_02, MDS.duringAction, MDS.LongitudinalAction))
    # LateralAction
    g.add((re_d_02, MDS.errorTriggerAction, MDS.ShortDistanceLaneChangeAction))
    g.add((re_d_02, MDS.errorTriggerAction, MDS.LongDistanceLaneChangeAction))
    g.add((re_d_02, MDS.errorTriggerAction, MDS.ShortTimeLaneChangeAction))
    g.add((re_d_02, MDS.errorTriggerAction, MDS.LongTimeLaneChangeAction))
    #
    g.add((re_d_02, MDS.errorTriggerAction, MDS.IncreaseLateralDistanceAction))
    g.add((re_d_02, MDS.errorTriggerAction, MDS.ReduceLateralDistanceAction))
    g.add((re_d_02, MDS.errorTriggerAction, MDS.SameLateralDistanceAction))
    #
    # LongitudinalAction
    g.add((re_d_02, MDS.errorTriggerAction, MDS.IncreaseSpeedAction))
    g.add((re_d_02, MDS.errorTriggerAction, MDS.SameSpeedAction))

    # ***
    # Did not realize concrete barrier.
    #
    re_rf_05 = URIRef(base_uri + "re_rf_05")
    # Add triples using store's add() method.
    g.add((re_rf_05, RDF.type, MDS.RecognitionFailure))
    g.add((re_rf_05, RDFS.comment, Literal("Did not realize concrete barrier.", lang="en")))
    g.add((re_rf_05, MDS.duringAction, MDS.LongitudinalAction))
    # LateralAction
    g.add((re_rf_05, MDS.errorTriggerAction, MDS.ShortDistanceLaneChangeAction))
    g.add((re_rf_05, MDS.errorTriggerAction, MDS.LongDistanceLaneChangeAction))
    g.add((re_rf_05, MDS.errorTriggerAction, MDS.ShortTimeLaneChangeAction))
    g.add((re_rf_05, MDS.errorTriggerAction, MDS.LongTimeLaneChangeAction))
    #
    g.add((re_rf_05, MDS.errorTriggerAction, MDS.IncreaseLateralDistanceAction))
    g.add((re_rf_05, MDS.errorTriggerAction, MDS.ReduceLateralDistanceAction))
    g.add((re_rf_05, MDS.errorTriggerAction, MDS.SameLateralDistanceAction))
    #
    # LongitudinalAction
    g.add((re_rf_05, MDS.errorTriggerAction, MDS.IncreaseSpeedAction))
    g.add((re_rf_05, MDS.errorTriggerAction, MDS.OvertakeSpeedAction))
    g.add((re_rf_05, MDS.errorTriggerAction, MDS.ReduceSpeedAction))
    g.add((re_rf_05, MDS.errorTriggerAction, MDS.ZeroSpeedAction))

    # ***
    # Exceeded safe speed but not speed limit.
    #
    de_sp_01 = URIRef(base_uri + "de_sr_01")
    # Add triples using store's add() method.
    g.add((de_sp_01, RDF.type, MDS.SpeedRelatedError))
    g.add((de_sp_01, RDFS.comment, Literal("Exceeded safe speed but not speed limit.", lang="en")))
    g.add((de_sp_01, MDS.duringAction, MDS.LongitudinalAction))
    g.add((de_sp_01, MDS.errorTriggerAction, MDS.IncreaseSpeedAction))

    # ***
    # Driving slowly in relation to other traffic.
    #
    de_sr_02 = URIRef(base_uri + "de_sr_02")
    # Add triples using store's add() method.
    g.add((de_sr_02, RDF.type, MDS.SpeedRelatedError))
    g.add((de_sr_02, RDFS.comment, Literal("Driving slowly in relation to other traffic.", lang="en")))
    g.add((de_sr_02, MDS.duringAction, MDS.LongitudinalAction))
    g.add((de_sr_02, MDS.errorTriggerAction, MDS.ReduceSpeedAction))
    g.add((de_sr_02, MDS.errorTriggerAction, MDS.SameSpeedAction))
    g.add((de_sr_02, MDS.errorTriggerAction, MDS.ZeroSpeedAction))

    # ***
    # Sudden or improper braking.
    #
    de_isd_01 = URIRef(base_uri + "de_isd_01")
    # Add triples using store's add() method.
    g.add((de_isd_01, RDF.type, MDS.ImproperStoppingOrDecelerating))
    g.add((de_isd_01, RDFS.comment, Literal("Sudden or improper braking.", lang="en")))
    g.add((de_isd_01, MDS.duringAction, MDS.LongitudinalAction))
    g.add((de_isd_01, MDS.errorTriggerAction, MDS.ReduceSpeedAction))

    # ***
    # Sudden or improper stopping.
    #
    de_isd_02 = URIRef(base_uri + "de_isd_02")
    # Add triples using store's add() method.
    g.add((de_isd_02, RDF.type, MDS.ImproperStoppingOrDecelerating))
    g.add((de_isd_02, RDFS.comment, Literal("Sudden or improper stopping.", lang="en")))
    g.add((de_isd_02, MDS.duringAction, MDS.LongitudinalAction))
    g.add((de_isd_02, MDS.errorTriggerAction, MDS.ZeroSpeedAction))

    # ***
    # Wrong side of road, not overtaking.
    #
    de_im_02 = URIRef(base_uri + "de_im_02")
    # Add triples using store's add() method.
    g.add((de_im_02, RDF.type, MDS.ImproperManeuver))
    g.add((de_im_02, RDFS.comment, Literal("Wrong side of road, not overtaking.", lang="en")))
    g.add((de_im_02, MDS.duringAction, MDS.LongitudinalAction))
    g.add((de_im_02, MDS.errorTriggerAction, MDS.ShortDistanceLaneChangeAction))
    g.add((de_im_02, MDS.errorTriggerAction, MDS.LongDistanceLaneChangeAction))
    g.add((de_im_02, MDS.errorTriggerAction, MDS.ShortTimeLaneChangeAction))
    g.add((de_im_02, MDS.errorTriggerAction, MDS.LongTimeLaneChangeAction))
    g.add((de_im_02, MDS.errorTriggerAction, MDS.IncreaseSpeedAction))
    g.add((de_im_02, MDS.errorTriggerAction, MDS.OvertakeSpeedAction))
    g.add((de_im_02, MDS.errorTriggerAction, MDS.SameSpeedAction))

    # ***
    # Driver did not accelerate enough
    #
    pe_plong_01 = URIRef(base_uri + "pe_plong_01")
    # Add triples using store's add() method.
    g.add((pe_plong_01, RDF.type, MDS.PoorLongitudinalControl))
    g.add((pe_plong_01, RDFS.comment, Literal("Driver did not accelerate enough.", lang="en")))
    g.add((pe_plong_01, MDS.duringAction, MDS.LongitudinalAction))
    g.add((pe_plong_01, MDS.errorTriggerAction, MDS.ReduceSpeedAction))
    g.add((pe_plong_01, MDS.errorTriggerAction, MDS.SameSpeedAction))

    # ***
    # Exceed speed limit
    #
    v_sv_01 = URIRef(base_uri + "v_sv_01")
    # Add triples using store's add() method.
    g.add((v_sv_01, RDF.type, MDS.SpeedViolation))
    g.add((v_sv_01, RDFS.comment, Literal("Exceed speed limit.", lang="en" )))
    g.add((v_sv_01, MDS.duringAction, MDS.LongitudinalAction))
    g.add((v_sv_01, MDS.errorTriggerAction, MDS.IncreaseSpeedAction))
    g.add((v_sv_01, MDS.errorTriggerAction, MDS.OvertakeSpeedAction))

    # Bind the MDS namespace to a prefix for more readable output
    g.bind("mds", MDS)
    g.bind("rdf", RDF)
    g.bind("rdfs", RDFS)


def print_raw_triples():
    # Iterate over triples in store and print them out.
    print("--- printing raw triples ---")
    for s, p, o in g:
        print((s, p, o))


def print_turtle_format():
    # print all the data in the Turtle format
    print("--- printing mboxes ---")
    print(g.serialize())


def save_file():
    with open(file_path, 'w') as file:
        file.write(g.serialize())


def get_graph(force_regeneration=False, print_turtle=False):
    if not exists(file_path) or force_regeneration:
        generate_rules()
        if print_turtle:
            print_turtle_format()
        save_file()

    return Graph().parse(file_path)
