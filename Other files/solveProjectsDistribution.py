import readSolution
import fromExcelToPython
import findSolution
import lp
import random

print("-------------------------------------------------------------------------------")
print("|                                 Bienvenue                                    |")
print("-------------------------------------------------------------------------------\n")

print("Ce programme a pour but de résoudre le problème de répartition des projets à partir des choix d'étudiants sous format xls")

print("\n----------------- Etape 1 : Récupération des données -------------------")

print("Entrez le nombre de projets :")
#nbProject = input()
nbProject = 120
# TODO CHANGE THE PATH
[students, studentID] = fromExcelToPython.getStudentsFromXls("C:/Users/julia/Downloads/Nouveau dossier/test.xls", int(nbProject))


itsOK = True

while(itsOK):
    projects = []

    typeOk = True
        
    if(type(nbProject) == type(1)):
        typeOk = False

    print("Entrez le nombre de place par projet :")

    for pr in range(int(nbProject)):
        print("Pour le projet " + str(pr) + ": ")
        #nbStudent = input()
        nbStudent = 1
        projects.append(lp.Project(pr, 5))

    model = lp.Model(students, projects)

    print("Voici le modèle que vous avez entré :\n")
    lp.printModel(model)

    get = True
    while(get):
        print("Vous convient-il ? (y/n)")
        good = input()

        if(good == 'y' or good == 'Y'):
            itsOK = False
            get = False
        elif(good == 'n' or good == 'N'):
            itsOK = True
            get = False
        else:
            print("Votre input n'est pas correct")
    
print("\n----------------- Etape 2 : Création du fichier Linear Program -------------------")

fileLp = lp.lp(model, "lpFileTest")
 
fileLpE = fileLp + '.lp'

print("\n----------------- Etape 3 : Calcul de la solution avec glpk -------------------")

solution = findSolution.findSolution(fileLpE, "solutionTest.txt")

print("\n----------------- Etape 4 : Récupération de la solution -------------------")

projects = readSolution.readSolution(solution, nbStudent, nbProject)

print("\n----------------- Etape 5 : Lecture des résultats -------------------")
print("Entrez le nom du fichier à exporter :")
fileName = input()


readSolution.interface(projects, fileName, students, studentID)
 
