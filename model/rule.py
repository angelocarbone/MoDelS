from .factory import driving_error_to_action, driving_error_to_causal_factor


def get_driving_error_to_causal_factor_rule(val):
    g = driving_error_to_causal_factor.get_graph(force_regeneration=False)

    q = """
        prefix mds: <http://angelocarbone.com/rules/MoDelS#>
        SELECT ?x ?label ?c
        WHERE {
            ?x mds:isCausedBy mds:%s .
            OPTIONAL { ?x rdfs:comment ?c . }
        }
    """ % val

    # Apply the query to the graph and iterate through results
    #for r in g.query(q):
     #    print(r["x"])

    return g.query(q)


def get_driving_error_to_action_rule(driving_error, current_action):
    g = driving_error_to_action.get_graph(force_regeneration=False, print_turtle=False)

    q = """
            prefix mds: <http://angelocarbone.com/rules/MoDelS#>
            SELECT ?driving_error ?related_action
            WHERE {
                ?driving_error rdf:type mds:%s .
                ?driving_error mds:duringAction mds:%s .
                ?driving_error mds:errorTriggerAction ?related_action .                                               
            }
        """ % (driving_error, current_action)

    # Apply the query to the graph and iterate through results
    #for r in g.query(q):
        # print(r)
       # print(r["driving_error"] + " - " + r["related_action"])
    #
    return g.query(q)


# get_driving_error_to_causal_factor_rule("Distraction")
# get_driving_error_to_action_rule("SpeedViolation", "AbsoluteSpeedAction")

# Driver is distracted by internal second task
# re_d_01 -> LongitudinalAction or LateralAction

# Driver is distracted by external factor
# re_d_02 -> LongitudinalAction or LateralAction

# Did not realize concrete barrier
# re_rf_05 -> LongitudinalAction or LateralAction

# Exceeded safe speed but not speed limit
# de_sr_01 -> SpeedAction

# Driving slowly in relation to other traffic
# de_sr_02 -> SpeedAction

# Avoiding pedestrian ???
# de_ac_02

# Avoiding other cf_vehicle ???
# de_ac_03

# Sudden or improper braking
# de_isd_01 -> LongitudinalAction -> SpeedAction

# Sudden or improper stopping
# de_isd_02 -> LongitudinalAction -> SpeedAction

# Wrong side of road, not overtaking
# de_im_02 -> (ChangeLaneAction + SpeedAction)

# Driver did not accelerate enough
# pe_plong_01 -> SpeedAction

# Exceed speed limit
# v_sv_01 -> SpeedAction