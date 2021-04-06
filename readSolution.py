#lru_cache

# Library to sort    
import operator

class Project:
    students = []
    room = 0

    def __init__(self, id, students):
        self.id = id
        self.students = students
    
    def addStudent(self, student):
        self.students.append(student)

    
def readSolution(fileName):
    '''
    Interfaces the solutions from the result of lp file after using glpk

    :parameter fileName: Name of the file to interface
    :type fileName: String
    '''

    solutionFile = open(fileName + ".txt", "r")

    header = solutionFile.read(150)

    nummberConstraints = int(header[25:28])

    numberResult = int(header[41:45])

    tableHeaderConstraints = solutionFile.read(130)

    constraints = []
    for i in range(nummberConstraints):
        constraints.append(solutionFile.read(66))

    tableHeader = solutionFile.read(130)

    results = []
    for i in range(numberResult):
        results.append(solutionFile.read(66))

    interestingResults = []
    i = -1

    projects = []

    tmp = {}
    for line in results:
        if line[36] == '1':
            i += 1
            interestingResults.append(line)
            index = interestingResults[i].find('.')
            projectId = interestingResults[i][index + 1 : index + 4]
            index2 = interestingResults[i].find('x')
            studentId = interestingResults[i][index2 + 1 : index]
            # tmp.append((int(projectId), ))
            key = int(projectId)
            if key not in tmp:
                tmp[key] = [int(studentId)]
            else:
                tmp[key].append(int(studentId))
            # print(str(int(projectId)) + " & " + str(int(studentId)))

    sorted_x = sorted(tmp.items(), key=operator.itemgetter(0))

    for pr in sorted_x:
        projects.append(Project(pr[0],pr[1]))
    
    return projects


def interface(projects :Project):
    getOut = False
    while(not getOut):
            
        print("Si vous voulez voir le nombre d'étudiants pour chaque projet, appuyez sur A")
        print("Si vous voulez voir le nom des étudiants pour tous les projets, appuyez sur Z")
        print("Si vous voulez voir le nombre d'étudiants pour un projet particulier, appuyez sur E")
        print("Si vous voulez quitter, appuyer sur Q")

        value = input()

        if (value == 'A'):
            for projet in projects:
                print("Pour le projet " + str(projet.id) + " il y a " + str(len(projet.students)) + " étudiants\n")

        if (value == 'Z'):
            for projet in projects :
                print("Pour le projet " + str(projet.id) )
                for student in projet.students:
                    print(" etudiant :" + str(student))

        if (value == 'E'):
            print("Veuillez entrer le numéro du projet pour lequel vous voulez la liste des étudiants\n")
            nProject = input()
            for projet in projects:
                if(projet.id == int(nProject)):
                    print("Pour le projet " + str(projet.id) + " il y a " + str(len(projet.students)) + " étudiants\n")
                    for student in projet.students:
                        print("   étudiant :" + str(student))
                    

        if(value == 'Q'):
            getOut = True


if __name__ == "__main__":
    projects = readSolution("output")
    interface(projects)
