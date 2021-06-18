from typing import List,Union
from collections import namedtuple

class Teacher:
    def __init__(self, name : str, gender : str, subject : str):
        self.name = name
        self.gender = gender
        self.subject = subject

class Student:
    def __init__(self, name : str, gender : str, id : int) -> None:
        self.name = name
        self.gender = gender
        self.id = id

class Class:
    def __init__(self, name : str, grade : int, class_members : List[Student]) -> None:
        self.name = name
        self.grade = grade
        self.class_members = {}
        # Create a class members dict with student info namedtuple
        for mem in class_members:
                self.class_members[mem.name] = {
                    'name' : mem.name,
                    'gender': mem.gender,
                    'id': mem.id,
                    'Class': self.name
                    }
                self.dict_to_tuple = namedtuple(self.name, self.class_members[mem.name])
                self.class_members[mem.name] = self.dict_to_tuple(**self.class_members[mem.name])

    def get_name_by_id(self,id):
        for st in self.class_members.values(): #Search in students namedtuples
            if st.id == id:
                return st.name

class School:
    def __init__(self, name : str, classes : List[Class], teachers : List[Teacher]) ->None:
        self.name = name
        self.classes = classes
        self.teachers = {}
        
        for mem in teachers:
            self.teachers[mem.subject] = mem

    def get_teacher_by_subject(self,subject):
        for te_subject, teacher in self.teachers.items():
            if te_subject == subject:
                return teacher.name
    
    def search_st_info(self, name):
        for cls in self.classes: #In school search classes
            for st_name in cls.class_members: #in class search student's name(dict keys)
                if st_name == name:
                    return cls.class_members[st_name] #return dict values (namedtuple)

classA = Class("Math",12,[
    Student("A1","male",1),
    Student("B1","male",2),
    Student("X1","female",3),
    Student("C1","female",4),
])

classB = Class("Physics",11,[
    Student("D2","male",1),
    Student("E2","female",2),
    Student("H2","male",3),
    Student("Z2","female",4),
])

classC = Class("English",10,[
    Student("D3","male",1),
    Student("Y3","female",2),
    Student("L3","male",3),
    Student("N3","female",4),
])

BKU = School("BK",[classA,classB,classC],[
    Teacher("John","male","Math"),
    Teacher("Kyle","male","Physics"),
    Teacher("David","male","English"),
])


# target_st = classB.get_name_by_id(2)
# print(target_st)

# search_teacher = BKU.get_teacher_by_subject("English")
# print(search_teacher)

st_info = BKU.search_st_info("D2")
print(st_info)
print(st_info.name)
print(st_info.Class)