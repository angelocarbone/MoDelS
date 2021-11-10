from os.path import exists
from rdflib import Graph, Literal, RDF, RDFS, URIRef
from core.namespace.MDS import MDS
from config import RULE_DIR

# Create a Graph
g = Graph()

base_uri = "http://angelocarbone.com/rules/MoDelS#"
file_path = RULE_DIR + 'driving_error_to_causal_factor.ttl'


def generate_rules():
    # Driver is distracted by internal factor
    re_d_01 = URIRef(base_uri + "re_d_01")
    # Add triples using store's add() method.
    g.add((re_d_01, RDF.type, MDS.DistractionError))
    g.add((re_d_01, RDFS.comment, Literal("Driver is distracted by internal factor.", lang="en")))
    g.add((re_d_01, MDS.isCausedBy, MDS.DrivingExperience))
    g.add((re_d_01, MDS.isCausedBy, MDS.VehicleUnfamiliarity))
    g.add((re_d_01, MDS.isCausedBy, MDS.Distraction))
    g.add((re_d_01, MDS.isCausedBy, MDS.SelfConfidence))
    g.add((re_d_01, MDS.isCausedBy, MDS.AlcoholImpairment))
    g.add((re_d_01, MDS.isCausedBy, MDS.DrugImpairment))

    # Driver is distracted by external factor
    re_d_02 = URIRef(base_uri + "re_d_02")
    # Add triples using store's add() method.
    g.add((re_d_02, RDF.type, MDS.DistractionError))
    g.add((re_d_02, RDFS.comment, Literal("Driver is distracted by external factor.", lang="en")))
    g.add((re_d_02, MDS.isCausedBy, MDS.DrivingExperience))
    g.add((re_d_02, MDS.isCausedBy, MDS.RoadAreaUnfamiliarity))
    g.add((re_d_02, MDS.isCausedBy, MDS.Distraction))
    g.add((re_d_02, MDS.isCausedBy, MDS.Frustration))
    g.add((re_d_02, MDS.isCausedBy, MDS.PressureOrStrain))
    g.add((re_d_02, MDS.isCausedBy, MDS.SelfConfidence))
    g.add((re_d_02, MDS.isCausedBy, MDS.Fatigued))

    # Did not see other cf_vehicle during merging
    re_rf_01 = URIRef(base_uri + "re_rf_01")
    # Add triples using store's add() method.
    g.add((re_rf_01, RDF.type, MDS.RecognitionFailure))
    g.add((re_rf_01, RDFS.comment, Literal("Did not see other cf_vehicle during merging.", lang="en")))
    g.add((re_rf_01, MDS.isCausedBy, MDS.ReducedVision))

    # Did not see other cf_vehicle during lane changing
    re_rf_02 = URIRef(base_uri + "re_rf_02")
    # Add triples using store's add() method.
    g.add((re_rf_02, RDF.type, MDS.RecognitionFailure))
    g.add((re_rf_02, RDFS.comment, Literal("Did not see other cf_vehicle during lane changing.", lang="en")))
    g.add((re_rf_02, MDS.isCausedBy, MDS.ReducedVision))

    # Did not see other pedestrian during merging
    re_rf_03 = URIRef(base_uri + "re_rf_03")
    # Add triples using store's add() method.
    g.add((re_rf_03, RDF.type, MDS.RecognitionFailure))
    g.add((re_rf_03, RDFS.comment, Literal("Did not see other pedestrian during merging.", lang="en")))
    g.add((re_rf_03, MDS.isCausedBy, MDS.ReducedVision))

    # Did not see other pedestrian during lane changing
    re_rf_04 = URIRef(base_uri + "re_rf_04")
    # Add triples using store's add() method.
    g.add((re_rf_04, RDF.type, MDS.RecognitionFailure))
    g.add((re_rf_04, RDFS.comment, Literal("Did not see other pedestrian during lane changing.", lang="en")))
    g.add((re_rf_04, MDS.isCausedBy, MDS.ReducedVision))

    # Did not realize concrete barrier
    re_rf_05 = URIRef(base_uri + "re_rf_05")
    # Add triples using store's add() method.
    g.add((re_rf_05, RDF.type, MDS.RecognitionFailure))
    g.add((re_rf_05, RDFS.comment, Literal("Did not realize concrete barrier.", lang="en")))
    g.add((re_rf_05, MDS.isCausedBy, MDS.DrivingExperience))
    g.add((re_rf_05, MDS.isCausedBy, MDS.RoadAreaUnfamiliarity))
    g.add((re_rf_05, MDS.isCausedBy, MDS.Distraction))
    g.add((re_rf_05, MDS.isCausedBy, MDS.AlcoholImpairment))
    g.add((re_rf_05, MDS.isCausedBy, MDS.Fatigued))
    g.add((re_rf_05, MDS.isCausedBy, MDS.DrugImpairment))
    g.add((re_rf_05, MDS.isCausedBy, MDS.ReducedVision))

    # Exceeded safe speed but not speed limit
    de_sr_01 = URIRef(base_uri + "de_sr_01")
    # Add triples using store's add() method.
    g.add((de_sr_01, RDF.type, MDS.SpeedRelatedError))
    g.add((de_sr_01, RDFS.comment, Literal("Exceeded safe speed but not speed limit.", lang="en")))
    g.add((de_sr_01, MDS.isCausedBy, MDS.DrivingExperience))
    g.add((de_sr_01, MDS.isCausedBy, MDS.Uncertainty))

    # Driving slowly in relation to other traffic
    de_sr_02 = URIRef(base_uri + "de_sr_02")
    # Add triples using store's add() method.
    g.add((de_sr_02, RDF.type, MDS.SpeedRelatedError))
    g.add((de_sr_02, RDFS.comment, Literal("Driving slowly in relation to other traffic.", lang="en")))
    g.add((de_sr_02, MDS.isCausedBy, MDS.DrivingExperience))
    g.add((de_sr_02, MDS.isCausedBy, MDS.RoadAreaUnfamiliarity))
    g.add((de_sr_02, MDS.isCausedBy, MDS.VehicleUnfamiliarity))
    g.add((de_sr_02, MDS.isCausedBy, MDS.Frustration))
    g.add((de_sr_02, MDS.isCausedBy, MDS.Panic))
    g.add((de_sr_02, MDS.isCausedBy, MDS.Uncertainty))
    g.add((de_sr_02, MDS.isCausedBy, MDS.Fatigued))
    g.add((de_sr_02, MDS.isCausedBy, MDS.ReducedVision))

    # Avoiding animal
    de_ac_01 = URIRef(base_uri + "de_ac_01")
    # Add triples using store's add() method.
    g.add((de_ac_01, RDF.type, MDS.AvoidingConflict))
    g.add((de_ac_01, RDFS.comment, Literal("Avoiding animal.", lang="en")))
    g.add((de_ac_01, MDS.isCausedBy, MDS.DrivingExperience))
    g.add((de_ac_01, MDS.isCausedBy, MDS.Distraction))
    g.add((de_ac_01, MDS.isCausedBy, MDS.Fatigued))
    g.add((de_ac_01, MDS.isCausedBy, MDS.Panic))

    # Avoiding pedestrian
    de_ac_02 = URIRef(base_uri + "de_ac_02")
    # Add triples using store's add() method.
    g.add((de_ac_02, RDF.type, MDS.AvoidingConflict))
    g.add((de_ac_02, RDFS.comment, Literal("Avoiding pedestrian.", lang="en")))
    g.add((de_ac_02, MDS.isCausedBy, MDS.DrivingExperience))
    g.add((de_ac_02, MDS.isCausedBy, MDS.Distraction))
    g.add((de_ac_02, MDS.isCausedBy, MDS.Fatigued))
    g.add((de_ac_02, MDS.isCausedBy, MDS.Panic))

    # Avoiding other cf_vehicle
    de_ac_03 = URIRef(base_uri + "de_ac_03")
    # Add triples using store's add() method.
    g.add((de_ac_03, RDF.type, MDS.AvoidingConflict))
    g.add((de_ac_03, RDFS.comment, Literal("Avoiding other cf_vehicle.", lang="en")))
    g.add((de_ac_03, MDS.isCausedBy, MDS.DrivingExperience))
    g.add((de_ac_03, MDS.isCausedBy, MDS.Distraction))
    g.add((de_ac_03, MDS.isCausedBy, MDS.Fatigued))
    g.add((de_ac_03, MDS.isCausedBy, MDS.Panic))

    # Avoiding other object or parked cf_vehicle
    de_ac_04 = URIRef(base_uri + "de_ac_04")
    # Add triples using store's add() method.
    g.add((de_ac_04, RDF.type, MDS.AvoidingConflict))
    g.add((de_ac_04, RDFS.comment, Literal("Avoiding other object or parked cf_vehicle.", lang="en")))
    g.add((de_ac_04, MDS.isCausedBy, MDS.DrivingExperience))
    g.add((de_ac_04, MDS.isCausedBy, MDS.Distraction))
    g.add((de_ac_04, MDS.isCausedBy, MDS.Fatigued))
    g.add((de_ac_04, MDS.isCausedBy, MDS.Panic))

    # Sudden or improper braking
    de_isd_01 = URIRef(base_uri + "de_isd_01")
    # Add triples using store's add() method.
    g.add((de_isd_01, RDF.type, MDS.ImproperStoppingOrDecelerating))
    g.add((de_isd_01, RDFS.comment, Literal("Sudden or improper braking.", lang="en")))
    g.add((de_isd_01, MDS.isCausedBy, MDS.DrivingExperience))
    g.add((de_isd_01, MDS.isCausedBy, MDS.RoadAreaUnfamiliarity))
    g.add((de_isd_01, MDS.isCausedBy, MDS.VehicleUnfamiliarity))
    g.add((de_isd_01, MDS.isCausedBy, MDS.Distraction))
    g.add((de_isd_01, MDS.isCausedBy, MDS.Panic))
    g.add((de_isd_01, MDS.isCausedBy, MDS.Uncertainty))
    g.add((de_isd_01, MDS.isCausedBy, MDS.ReducedVision))

    # Sudden or improper stopping
    de_isd_02 = URIRef(base_uri + "de_isd_02")
    # Add triples using store's add() method.
    g.add((de_isd_02, RDF.type, MDS.ImproperStoppingOrDecelerating))
    g.add((de_isd_02, RDFS.comment, Literal("Sudden or improper stopping.", lang="en")))
    g.add((de_isd_02, MDS.isCausedBy, MDS.DrivingExperience))
    g.add((de_isd_02, MDS.isCausedBy, MDS.RoadAreaUnfamiliarity))
    g.add((de_isd_02, MDS.isCausedBy, MDS.VehicleUnfamiliarity))
    g.add((de_isd_02, MDS.isCausedBy, MDS.Distraction))
    g.add((de_isd_02, MDS.isCausedBy, MDS.Panic))
    g.add((de_isd_02, MDS.isCausedBy, MDS.Uncertainty))
    g.add((de_isd_02, MDS.isCausedBy, MDS.ReducedVision))

    # Following too closely
    de_im_01 = URIRef(base_uri + "de_im_01")
    # Add triples using store's add() method.
    g.add((de_im_01, RDF.type, MDS.ImproperManeuver))
    g.add((de_im_01, RDFS.comment, Literal("Following too closely.", lang="en")))
    g.add((de_im_01, MDS.isCausedBy, MDS.DrivingExperience))
    g.add((de_im_01, MDS.isCausedBy, MDS.InHurry))
    g.add((de_im_01, MDS.isCausedBy, MDS.PressureOrStrain))
    g.add((de_im_01, MDS.isCausedBy, MDS.SelfConfidence))
    g.add((de_im_01, MDS.isCausedBy, MDS.AlcoholImpairment))
    g.add((de_im_01, MDS.isCausedBy, MDS.DrugImpairment))

    # Wrong side of road, not overtaking
    de_im_02 = URIRef(base_uri + "de_im_02")
    # Add triples using store's add() method.
    g.add((de_im_02, RDF.type, MDS.ImproperManeuver))
    g.add((de_im_02, RDFS.comment, Literal("Wrong side of road, not overtaking.", lang="en")))
    g.add((de_im_02, MDS.isCausedBy, MDS.DrivingExperience))
    g.add((de_im_02, MDS.isCausedBy, MDS.SelfConfidence))
    g.add((de_im_02, MDS.isCausedBy, MDS.AlcoholImpairment))
    g.add((de_im_02, MDS.isCausedBy, MDS.DrugImpairment))

    # Cutting in, too close behind of other cf_vehicle
    de_im_03 = URIRef(base_uri + "de_im_03")
    # Add triples using store's add() method.
    g.add((de_im_03, RDF.type, MDS.ImproperManeuver))
    g.add((de_im_03, RDFS.comment, Literal("Cutting in, too close behind of other cf_vehicle.", lang="en")))
    g.add((de_im_03, MDS.isCausedBy, MDS.DrivingExperience))
    g.add((de_im_03, MDS.isCausedBy, MDS.VehicleUnfamiliarity))
    g.add((de_im_03, MDS.isCausedBy, MDS.InHurry))
    g.add((de_im_03, MDS.isCausedBy, MDS.SelfConfidence))
    g.add((de_im_03, MDS.isCausedBy, MDS.AlcoholImpairment))
    g.add((de_im_03, MDS.isCausedBy, MDS.DrugImpairment))
    g.add((de_im_03, MDS.isCausedBy, MDS.ReducedVision))

    # Cutting in, too in front of other cf_vehicle
    de_im_04 = URIRef(base_uri + "de_im_04")
    # Add triples using store's add() method.
    g.add((de_im_04, RDF.type, MDS.ImproperManeuver))
    g.add((de_im_04, RDFS.comment, Literal("Cutting in, too in front of other cf_vehicle.", lang="en")))
    g.add((de_im_04, MDS.isCausedBy, MDS.DrivingExperience))
    g.add((de_im_04, MDS.isCausedBy, MDS.VehicleUnfamiliarity))
    g.add((de_im_04, MDS.isCausedBy, MDS.InHurry))
    g.add((de_im_04, MDS.isCausedBy, MDS.SelfConfidence))
    g.add((de_im_04, MDS.isCausedBy, MDS.AlcoholImpairment))
    g.add((de_im_04, MDS.isCausedBy, MDS.DrugImpairment))
    g.add((de_im_04, MDS.isCausedBy, MDS.ReducedVision))

    # Driving in other cf_vehicle's blind zone
    de_im_05 = URIRef(base_uri + "de_im_05")
    # Add triples using store's add() method.
    g.add((de_im_05, RDF.type, MDS.ImproperManeuver))
    g.add((de_im_05, RDFS.comment, Literal("Driving in other cf_vehicle's blind zone.", lang="en")))
    g.add((de_im_05, MDS.isCausedBy, MDS.DrivingExperience))
    g.add((de_im_05, MDS.isCausedBy, MDS.Panic))
    g.add((de_im_05, MDS.isCausedBy, MDS.Uncertainty))
    g.add((de_im_05, MDS.isCausedBy, MDS.ReducedVision))

    # Improper turn, cut corner on left turn
    de_im_06 = URIRef(base_uri + "de_im_06")
    # Add triples using store's add() method.
    g.add((de_im_06, RDF.type, MDS.ImproperManeuver))
    g.add((de_im_06, RDFS.comment, Literal("Improper turn, cut corner on left turn.", lang="en")))
    g.add((de_im_06, MDS.isCausedBy, MDS.DrivingExperience))
    g.add((de_im_06, MDS.isCausedBy, MDS.RoadAreaUnfamiliarity))
    g.add((de_im_06, MDS.isCausedBy, MDS.Distraction))
    g.add((de_im_06, MDS.isCausedBy, MDS.Panic))
    g.add((de_im_06, MDS.isCausedBy, MDS.PressureOrStrain))
    g.add((de_im_06, MDS.isCausedBy, MDS.Uncertainty))
    g.add((de_im_06, MDS.isCausedBy, MDS.AlcoholImpairment))
    g.add((de_im_06, MDS.isCausedBy, MDS.DrugImpairment))

    # Improper turn, cut corner on right turn
    de_im_07 = URIRef(base_uri + "de_im_07")
    # Add triples using store's add() method.
    g.add((de_im_07, RDF.type, MDS.ImproperManeuver))
    g.add((de_im_07, RDFS.comment, Literal("Improper turn, cut corner on right turn.", lang="en")))
    g.add((de_im_07, MDS.isCausedBy, MDS.DrivingExperience))
    g.add((de_im_07, MDS.isCausedBy, MDS.RoadAreaUnfamiliarity))
    g.add((de_im_07, MDS.isCausedBy, MDS.Distraction))
    g.add((de_im_07, MDS.isCausedBy, MDS.Panic))
    g.add((de_im_07, MDS.isCausedBy, MDS.PressureOrStrain))
    g.add((de_im_07, MDS.isCausedBy, MDS.Uncertainty))
    g.add((de_im_07, MDS.isCausedBy, MDS.AlcoholImpairment))
    g.add((de_im_07, MDS.isCausedBy, MDS.DrugImpairment))

    # Improper turn, wide left turn
    pe_plc_01 = URIRef(base_uri + "pe_plc_01")
    # Add triples using store's add() method.
    g.add((pe_plc_01, RDF.type, MDS.PoorLateralControl))
    g.add((pe_plc_01, RDFS.comment, Literal("Improper turn, wide left turn.", lang="en")))
    g.add((pe_plc_01, MDS.isCausedBy, MDS.DrivingExperience))
    g.add((pe_plc_01, MDS.isCausedBy, MDS.Uncertainty))
    g.add((pe_plc_01, MDS.isCausedBy, MDS.Fatigued))
    g.add((pe_plc_01, MDS.isCausedBy, MDS.RoadAreaUnfamiliarity))
    g.add((pe_plc_01, MDS.isCausedBy, MDS.AlcoholImpairment))
    g.add((pe_plc_01, MDS.isCausedBy, MDS.DrugImpairment))

    # Driver did not accelerate enough
    pe_plong_01 = URIRef(base_uri + "pe_plong_01")
    # Add triples using store's add() method.
    g.add((pe_plong_01, RDF.type, MDS.PoorLateralControl))
    g.add((pe_plong_01, RDFS.comment, Literal("Driver did not accelerate enough.", lang="en")))
    g.add((pe_plong_01, MDS.isCausedBy, MDS.DrivingExperience))
    g.add((pe_plong_01, MDS.isCausedBy, MDS.VehicleUnfamiliarity))
    g.add((pe_plong_01, MDS.isCausedBy, MDS.Uncertainty))
    g.add((pe_plong_01, MDS.isCausedBy, MDS.Fatigued))

    # Illegal u-turn
    v_im_01 = URIRef(base_uri + "v_im_01")
    # Add triples using store's add() method.
    g.add((v_im_01, RDF.type, MDS.IllegalManeuver))
    g.add((v_im_01, RDFS.comment, Literal("Illegal u-turn.", lang="en")))
    g.add((v_im_01, MDS.isCausedBy, MDS.DrivingExperience))
    g.add((v_im_01, MDS.isCausedBy, MDS.RoadAreaUnfamiliarity))
    g.add((v_im_01, MDS.isCausedBy, MDS.Distraction))
    g.add((v_im_01, MDS.isCausedBy, MDS.InHurry))
    g.add((v_im_01, MDS.isCausedBy, MDS.SelfConfidence))
    g.add((v_im_01, MDS.isCausedBy, MDS.Uncertainty))
    g.add((v_im_01, MDS.isCausedBy, MDS.AlcoholImpairment))
    g.add((v_im_01, MDS.isCausedBy, MDS.DrugImpairment))

    # Illegal passing
    v_im_02 = URIRef(base_uri + "v_im_02")
    # Add triples using store's add() method.
    g.add((v_im_02, RDF.type, MDS.IllegalManeuver))
    g.add((v_im_02, RDFS.comment, Literal("Illegal passing.", lang="en")))
    g.add((v_im_02, MDS.isCausedBy, MDS.DrivingExperience))
    g.add((v_im_02, MDS.isCausedBy, MDS.RoadAreaUnfamiliarity))
    g.add((v_im_02, MDS.isCausedBy, MDS.Distraction))
    g.add((v_im_02, MDS.isCausedBy, MDS.InHurry))
    g.add((v_im_02, MDS.isCausedBy, MDS.SelfConfidence))
    g.add((v_im_02, MDS.isCausedBy, MDS.AlcoholImpairment))
    g.add((v_im_02, MDS.isCausedBy, MDS.DrugImpairment))

    # Exceed speed limit
    v_sv_01 = URIRef(base_uri + "v_sv_01")
    # Add triples using store's add() method.
    g.add((v_sv_01, RDF.type, MDS.SpeedViolation))
    g.add((v_sv_01, RDFS.comment, Literal("Exceed speed limit.", lang="en")))
    g.add((v_sv_01, MDS.isCausedBy, MDS.DrivingExperience))
    g.add((v_sv_01, MDS.isCausedBy, MDS.EmotionalUpset))
    g.add((v_sv_01, MDS.isCausedBy, MDS.InHurry))
    g.add((v_sv_01, MDS.isCausedBy, MDS.PressureOrStrain))
    g.add((v_sv_01, MDS.isCausedBy, MDS.SelfConfidence))
    g.add((v_sv_01, MDS.isCausedBy, MDS.AlcoholImpairment))
    g.add((v_sv_01, MDS.isCausedBy, MDS.DrugImpairment))

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
