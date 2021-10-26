import pandas as pd 
import os
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


def getStudentsFromXls(fileXls, numberProjects, numberStudents):
    '''
    Get the list of student and their options from a xls file

    :param fileXls: the name of the file to get the option of each students
    :param numberProjects: the number of projects
    :param numberStudent: the number of students

    :type fileXls: string
    :type numberProjects: int
    :type numberStudents: int
    

    :return students: list of students with their choce of options
    :return studentsID: list of the name of the students

    :rtype students: table of Student
    :rtype studentsID: table of string 
    '''
    # Read the xls file
    df = pd.read_excel(r'' + fileXls)

    # Initialisationof the list of students and their IDs
    studentsID = []
    students = []

    i = 0
    while(i < numberStudents):
        # Get the name of the student in xls and appends it in the list of IDs
        studentsID.append(df.iloc[i,3])
        indice = 7
        option1 = ""
        option2 = ""
        option3 = ""
        option4 = ""
        option5 = ""
        # Initialisation of the variable to check if the student has not made a mistake when he filled the form
        testError = 0

        # Get each options
        while(indice < numberProjects*3 + 7):
            if df.iloc[i,indice] == "Option 1":
                option1 = int((indice - 7)/3) 
                testError += 100
            if df.iloc[i,indice] == "Option 2":
                option2 = int((indice - 7)/3)
                testError += 5
            if df.iloc[i,indice] == "Option 3":
                option3 = int((indice - 7)/3)
                testError += 3
            if df.iloc[i,indice] == "Option 4":
                option4 = int((indice - 7)/3)
                testError += 30
            if df.iloc[i,indice] == "Option 5":
                option5 = int((indice - 7)/3)
                testError += 1000
            indice = indice + 1

        # if a student made a mistake when he filled the form, an error is displayed in the console and the program exits
        if testError != 1138:
            print("Erreur : l'étudiant n°" + str(i) + ", " + str(studentsID[i]) + " ne sait pas remplir un formulaire...")
            # exit()
        # Add the student in the list of students
        students.append(Student(i, option1, option2, option3, option4, option5))
        i = i + 1
    # return the list of students and their IDs
    return [students, studentsID]
    

if __name__ == "__main__":
    [students, studentsID] = getStudentsFromXls("test.xls", 20, 7)
    print(students[0].option1)