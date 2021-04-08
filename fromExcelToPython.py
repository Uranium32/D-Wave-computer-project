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

""" Pour ouvri un fichier xlsx mais probleme pour l'instant, colones manquantes lors de l'ouverture 
df = pd.read_excel (os.path.join('/home/axel/Téléchargements/test.xlsx'), engine='openpyxl')
print (df)
print(type(df))
"""
def getStudentsFromXls(fileXls, numberProject):

    df = pd.read_excel(r'' + fileXls)
    #print(df.head())
    ID = pd.read_excel(r'' + fileXls,index_col=0)
    nombre_de_projets = numberProject
    nombre_d_etudiants = 1


    studentID = []
    students = []


    i = 0
    while(i < nombre_d_etudiants):
        studentID.append(df.iloc[i,3])
        indice = 7
        option1 = ""
        option2 = ""
        option3 = ""
        option4 = ""
        option5 = ""
        while(indice < nombre_de_projets):
            if df.iloc[i,indice] == "Option 1":
                option1 = indice - 6
            if df.iloc[i,indice] == "Option 2":
                option2 = indice - 6
            if df.iloc[i,indice] == "Option 3":
                option3 = indice - 6
            if df.iloc[i,indice] == "Option 4":
                option4 = indice - 6
            if df.iloc[i,indice] == "Option 5":
                option5 = indice - 6
            indice = indice + 1
        students.append(Student(i, option1, option2, option3, option4, option5))
        i = i + 1
    
    return [students, studentID]
    

if __name__ == "__main__":
    [students, studentsID] = getStudentsFromXls("test.xls", 20)
    print(students[0].option1)