
q_001 = '''
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX mds: <http://www.angelocarbone.com/ontologies/MoDelS#>
        PREFIX : <http://www.angelocarbone.com/rules/MoDelS#>
        PREFIX md: <http://www.w3.org/ns/md#>
        
        SELECT ?cf_driver ?action ?causalFactor ?cf_vehicle
        WHERE {
          ?cf_driver mds:driverIsImpaired ?causalFactor ;
                  mds:driverIsOnVehicle ?cf_vehicle .
          ?cf_vehicle mds:performsAction ?action .
        }
'''
q_002 = '''
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX mds: <http://www.angelocarbone.com/ontologies/MoDelS#>
        PREFIX : <http://www.angelocarbone.com/rules/MoDelS#>
        PREFIX md: <http://www.w3.org/ns/md#>

        SELECT ?nextAction  
        WHERE {
            ?d  :driverIsImpaired :Distraction ;
                :performsAction :DrivingStraight ;
                :nextAction ?nextAction .
        }        
    '''