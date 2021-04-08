#lru_cache

# Library to sort    
import operator

from lp import Student

class ProjectSolved:
    '''
    Project class corresponding to the project divided by student according to their choices 

    :member id: identifiant of the project
    :member students: list of the students for this project
    :member room: room planned for this project
    '''
    # Initialisation of the list of student
    students = []

    # Room planned for the project
    room = 0

    # Initialisation of the id and the list of student for the instance of the project
    def __init__(self, id, students, room):
        self.id = id
        self.students = students
        self.room = room 

    # Method to add one student to the list
    def addStudent(self, student):
        self.students.append(student)

  
def readSolution(fileName, nbStudents, nbProjects):
    '''
    Interfaces the solutions from the result of lp file after using glpk

    :parameter fileName: Name of the file to interface
    :type fileName: String
    '''

    # Open the solution file given in argument
    solutionFile = open(fileName, "r")

    text = solutionFile.read()
    # Get the header of the solution file
    indexHeader = text.find("mum") + 4
    
    # Get the number of constraints of the solution file
    numberConstraints = int(nbProjects) + int(nbStudents)

    # Get the number of results
    numberResult = int(nbProjects) * int(nbStudents)

    # Get the header of the constraints
    indexFirst = text.find("   No.")
    indexOne = text.find('Activity') + 10
    indexLast = text.find('Upper bound') + 12
    indexResult = text.find("  No. Column name") + 2 * (indexLast - indexFirst + 2)
    
    # Get the constraints lines
    constraints = []
    for i in range(numberConstraints):
        constraints.append(text[indexLast + 1 + (i + 1) * (indexLast + 2 - indexFirst): indexLast + (indexLast - indexFirst + 2) * (i + 2)])

    # Get the header of the results
    tableHeader = text[0]


    # Get the result lines
    results = []
    for i in range(numberResult):
        results.append(text[indexResult + 3 + i * (indexLast - indexFirst + 2): (indexLast - indexFirst ) * (i + 1) + indexResult - 2] )

    # Creation of the table of interesting result (only the one attribuated)
    interestingResults = []

    i = -1
    tmpProjects = {}
    for line in results:
        test = line.find("         1             0       ")
        # Keep only the attributed projects
        if test != -1 :
            i += 1
            interestingResults.append(line)

            # Get the index to get the id for the project
            index = interestingResults[i].find('.')
            projectId = interestingResults[i][index + 1 : index + 4]
            
            # Get the index to get the id for the student
            index2 = interestingResults[i].find('x')
            studentId = interestingResults[i][index2 + 1 : index]

            # Create the table of projects associated with a list of students
            key = int(projectId)

            # If the project already exists in the table, create the project and add its first student
            if key not in tmpProjects:
                tmpProjects[key] = [int(studentId)]
            # if it already exists, add the student
            else:
                tmpProjects[key].append(int(studentId))

    # Sort the table of project
    sortedTableOfProjects = sorted(tmpProjects.items(), key=operator.itemgetter(0))

    # Create a table of Project 
    projects = []
    i = 0
    for project in sortedTableOfProjects:
        projects.append(ProjectSolved(project[0],project[1], constraints[i][-4]))
        i += 1
    # Return the table of project
    return projects


def interface(projects :ProjectSolved, fileName, students: Student, studentID):
    '''
    Interfaces the results of the division of projects by students

    :param projects: list of the projects
    :param fileName: name of the file to save the results
    :param students: list of the students with the options

    :type projects: class Porject
    :type fileName: String 

    :return files: the display in files saved 
    '''
    # Boolean allowing to quit the program
    getOut = False
    while(not getOut):
        # Display allowing the user to choose what he wants to display
        print("\nSi vous voulez voir le nombre d'étudiants pour chaque projet, appuyez sur A")
        print("Si vous voulez voir le nom des étudiants pour tous les projets, appuyez sur Z")
        print("Si vous voulez voir le nombre d'étudiants pour un projet particulier, appuyez sur E")
        print("Si vous voulez voir le taux de satisfaction, appuyez sur R")
        print("Si vous voulez quitter, appuyer sur Q")

        # Get the choice of the user
        value = input()

        # Display and save the number of student per project
        if (value == 'A'):
            fileNbStudent = open(fileName + "nbStudent.txt","w")
            fileNbStudent.write("------------ Résultat ------------")
            for projet in projects:
                print("Pour le projet " + str(projet.id) + " il y a " + str(len(projet.students)) + " étudiants pour " + str(projet.room) + " places prévues\n")
                fileNbStudent.write("\nProjet " + str(projet.id) + " : " + str(len(projet.students)) + " étudiants/" + str(projet.room) + "\n")
            fileNbStudent.close()
            print("Le fichier "+ fileName + "nbStudent.txt a été créé")
            
        # Display the name of the students for each projects      
        elif (value == 'Z'):
            fileAll = open(fileName + "all.txt","w")
            fileAll.write("------------ Résultat ------------\n")
            # Write the number of the projet in the consol and in the file
            for projet in projects :
                fileAll.write("\n\nPour le projet " + str(projet.id) + " (" + str(len(projet.students)) + "/" + str(projet.room) + ")")
                print("Pour le projet " + str(projet.id)+ " (" + str(len(projet.students)) + "/" + str(projet.room) + ")")
                # Write the students for each projects
                for student in projet.students:
                    fileAll.write( "\n   étudiant : " + str(student)+ " => " + studentID[student])
                    print("   étudiant : " + str(student) + " => " + studentID[student])
            fileAll.close()
            print("Le fichier "+ fileName + "all.txt a été créé")


        # Allow the user to print the information of one particular project
        elif (value == 'E'):
            # Ask to choose one particular project
            print("Veuillez entrer le numéro du projet pour lequel vous voulez la liste des étudiants\n")
            nProject = input()
            # Write in the console the information for one specific project
            for projet in projects:
                if(projet.id == int(nProject)):
                    print("Pour le projet " + str(projet.id) + " il y a " + str(len(projet.students)) + " étudiants")
                    # Write in the consol the students for this project
                    for student in projet.students:
                        print("   étudiant : " + str(student) + " => " + studentID[student])
                    
        # If the user wants to quit, getOut is put to True
        elif(value == 'Q'):
            getOut = True

        # If the user wants the info of the satisfaction of the students
        elif(value == 'R'):
            tabSatisfation = calculateProba(projects, students)
            i = 0
            for pourcentage in tabSatisfation:
                i += 1
                print("Pour l'option " + str(i) + " : " + str(pourcentage))


        # If the choice does not correspond to a possibility ask to choose again
        else:
            print("Le choix que vous avez fait n'existe pas, Veuillez recommencer\n")

def calculateProba(projects : ProjectSolved, students):
    option1Nb = 0
    option2Nb = 0
    option3Nb = 0
    option4Nb = 0
    option5Nb = 0

    for pr in projects :
        for st in pr.students :
            for stu in students :
                if(st == stu.id):
                    if(stu.option1 == pr.id):
                        option1Nb += 1
                    if(stu.option2 == pr.id):
                        option2Nb += 1
                    if(stu.option3 == pr.id):
                        option3Nb += 1
                    if(stu.option4 == pr.id):
                        option4Nb += 1
                    if(stu.option5 == pr.id):
                        option5Nb += 1

    return [option1Nb/len(students) * 100, option2Nb/len(students) * 100, option3Nb/len(students) * 100, option4Nb/len(students) * 100, option5Nb/len(students) * 100]
