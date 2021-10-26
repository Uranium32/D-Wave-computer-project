
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