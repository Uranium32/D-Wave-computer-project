
#Lib to generate random ID
import uuid
# Libs to generate random numbers in a range
from random import choice
# Libs to generate random numbers with the possibility to exclude some
from random import randint
import math

def generateGraph(nbSummits, nbEdges, isWeight = False, minWeight = -100000, maxWeight = -100000):
    '''
    Generate a graph in the form of a file

    :param nbSummits: number of summit of the graph wanted
    :param nbEdges: number of edges of the graph wanted
    :param isWeight: precise if the graph is wanted with weights
    :param minWeight: value of the minimum weight 
    :param maxWeight: value of the maximum weight

    :type nbSummits: integer between 2 and 10000
    :type nbEdges: integer between 1 and 100000
    :type isWeight: boolean
    :type maxWeight: integer
    :type minWeight: integer

    :return: the name of the file which contains the graph
    :rtype: string
    '''
    ## --------- Verify the parameters given --------- ##

    # Verify the type of nbEdge
    if(type(nbEdges) != type(1)):
        print("the nbEdges parameter must be an integer")
        return
    # Verify nbEdges is between 1 and 100000
    if(nbEdges <= 1 or nbEdges > 100000):
        print("the nbEdges parameter must be between 2 and 100000")
        return
    # Verify the type of nbSummit
    if(type(nbSummits) != type(1)):
        print("the nbSummit parameter must be an integer")
        return
    # Verify nbSummit is between 1 and 10000
    if(nbSummits <= 0 or nbSummits > 10000):
        print("the nbSummit parameter must be between 1 and 10000")
        return
    # Verify there is not less edges than summits
    if(nbEdges < nbSummits):
        print("It must not have more summit than edges")
        return
    # Verify isWeight is a boolean 
    if(type(isWeight) != type(True)):
        print("the parameter isWeight must be a boolean")
        return
    # Verfify if weight are asked minWeight and maxWeight are filled
    if(isWeight and (minWeight == -100000 or maxWeight == -100000)):
        print("minWeight and maxWeight must be filled because you put isWeight to True")
        return
    # Verfify  minWeight and maxWeight are integers
    if(type(minWeight) != type(1) or type(maxWeight) !=  type(1)):
        print("minWeight and maxWeight must be both integers")
        return
    # Verfify  minWeight and maxWeight are integers
    if(minWeight > maxWeight):
        print("minWeight must be lesser than maxWeight, but we inverted the values for the following calculations")
        tmp = maxWeight
        maxWeight = minWeight
        minWeight = tmp
    # Verify if it is possible to have as many edges as given in argument
    #if(nbEdges > math.comb(2, nbSummits)):
     #   print(f"There is to many edges for {nbSummits} summits {math.comb(2, nbSummits)}")


    ## ------- Creation of the edges radomly ------- ##
    # Creation of set to erase the duplicates of couple of edges (couple of summit)
    setSummitCouple = set()

    # To have the wanted number of edges without duplicates
    while(len(setSummitCouple) != nbEdges):
        firstSummit = randint(0, nbSummits) 
        secondSummit = choice([i for i in range(0,nbSummits) if i not in [firstSummit,]])
        #the edges are bidirectionnal so we need to avoid the duplicates in form of (a,b) => (b,a)
        if(firstSummit < secondSummit):
            setSummitCouple.add((firstSummit,secondSummit))
        else:
            setSummitCouple.add((secondSummit,firstSummit))


    ## ------- Write in the file ------- ##
    # Generate a unique name of file with the summit and edges informations + a unique ID made with the uuid lib
    fileName = "graphS"+ str(nbSummits) + "E" + str(nbEdges) + "W" + str(isWeight) + "ID" + str(uuid.uuid4()) + ".txt"

    # Create the file
    graph = open(fileName, "w")

    # If there the weigths are wanted
    if isWeight:
        # Write in the file the graph
        for couple in setSummitCouple:
            graph.write(str(couple)+":"+ str(randint(minWeight,maxWeight)) + ",")
    # In the case there is no weight needed
    else:
        # Fill the weigths with 1
        for couple in setSummitCouple:
            graph.write(str(couple)+ ":1,")

    # Close the file
    graph.close()

    # Return the name of the file
    return fileName

if __name__ == "__main__":
    print(generateGraph(18,50, False))
