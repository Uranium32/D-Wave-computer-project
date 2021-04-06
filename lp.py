from random import randint


class Student:
    '''
    Student class corresponding to the student in M1 at ISEN 

    :member id: identifiant of the student
    :member option1: first choice of the student
    :member option2: second choice of the student
    :member option3: third choice of the student
    :member option4: fourth choice of the student
    :member option5: fifth choice of the student

    '''
    def __init__(self, id, option1, option2, option3, option4, option5):
        self.id = id
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.option5 = option5

class Project:
    '''
    Project class corresponding to the project proposed by ISEN 

    :member id: identifiant of the project
    :member numberofStudentAllowed: number of student allowed for this project
    '''
    def __init__(self, id, numberStudentAllowed):
        self.id = id
        self.numberStudentAllowed = numberStudentAllowed

class Model:
    '''
    Model class constructed with a list of students and a list of projects

    :member students: list of students from class Student
    :member projects: list of projects from class Project
    '''
    students = []
    projects = []
    def __init__(self, students, projects):
        self.students = students
        self.projects = projects

def printModel(model):
    '''
    Print the information of a model 

    :parameter model: model corresponding to the current problem
    :type model: class Model
    '''
    # Display the infomation of a student
    for student in model.students:
        print("Student:")
        print(student.id)
        print("Options:")
        print(student.option1)
        print(student.option2)
        print(student.option3)
        print(student.option4)
        print(student.option5)

    # Display the information of a project
    for project in model.projects:
        print("\nProject:")
        print(project.id)
        print("Room:")
        print(project.numberStudentAllowed)

def lp(model :Model, fileName):
    '''
    Transform a model into a lp file

    :parameter model: model corresponding to the current problem
    :type model: class Model

    :parameter fileName: name of the lp file to be written
    :type fileName: string

    :return lpFile: lpFile corresponding to the current problem
    :rtype lpFile: file (.lp => Linear Program)
    '''
    # Open the file
    lpFile = open(fileName + ".lp", "w")

    # First step : Objective function written in the lp file
    lpFile.write("Minimize \n\tobj: ")

    for student in model.students:
        for project in model.projects:
            if(project.id == student.option1):
                lpFile.write("- 1 ")
            elif(project.id == student.option2):
                lpFile.write("+ 2 ") 
            elif(project.id == student.option3):
                lpFile.write("+ 5 ")
            elif(project.id == student.option3):
                lpFile.write("+ 10 ")
            elif(project.id == student.option3):
                lpFile.write("+ 20 ")
            else :
                lpFile.write("+ 0 ")
            lpFile.write("x" + str(student.id) + "." + str(project.id) + " ")

    
    # Second step : Constraint written in the lp file
    lpFile.write("\nSubject To\n")

    # Number of constraints initialize to 0
    numConstraint = 0;

    # Constraints of number of student allowed in each project  
    for project in model.projects:
        lpFile.write("\tc"+ str(numConstraint) + ":")
        numConstraint += 1
        for student in model.students:
            lpFile.write(" + x" + str(student.id) + "." + str(project.id))
        lpFile.write(" <= " + str(project.numberStudentAllowed) + "\n")
    
    # Constraints forcing all the students to have only one project
    for student in model.students:
        lpFile.write("\tc"+ str(numConstraint) + ":")
        numConstraint += 1
        for project in model.projects:
            lpFile.write(" + x" + str(student.id) + "." + str(project.id))
        lpFile.write(" = 1\n")

    '''# Third step : Bounds written in the lp file    
    lpFile.write("Bounds\n")
    
    # Bounds forcing the value of the summit (xij) to be binary
    for project in model.projects:
        for student in model.students:
            lpFile.write("\tx" + str(student.id) + "." + str(project.id) + " = 0-1\n")
    '''
    # Fourth step : Binary declaration of the variables
    lpFile.write("Binary\n")
    for student in model.students:
        for project in model.projects:
            lpFile.write("\tx" + str(student.id) + "." + str(project.id) + "\n")
    
    # Last step : End written in the lp file
    lpFile.write("End\n")
    
    lpFile.close()

if __name__ == "__main__":
    '''
    # Initialisation of the problem :
    students = []
    projects = []

    students.append(Student(0, 0, 1))
    students.append(Student(1, 1, 0))

    projects.append(Project(0, 1))
    projects.append(Project(1, 1))

    model = Model(students, projects)

    lp(model, "aSimpleExample")

    '''
    # Initialisation of the problem :
    students = []
    projects = []
    # 9 students are created with random choices
    for numStudent in range(110):
        o1 = randint(0, 29)
        o2 = randint(0, 29)
        # Let's assure option 1 and option 2 are different (else add 1 or 2 mod 3)
        if (o1 == o2):
            o2 = (o2 + randint(1, 29)) % 30
        
        # Creation of the list of students
        students.append(Student(numStudent, o1, o2, 2, 7, 10))

    # Definitions of 30 projects with 2 to 6 students allowed respectively
    for i in range(30):
        projects.append(Project(i, randint(2,6)))



    # Creation of the model from the list of students and the list of projects
    model = Model(students=students, projects=projects)
    # Display the model 
    printModel(model)

    # Creation of lp file from the model with the filename given
    lp(model,"test6")
