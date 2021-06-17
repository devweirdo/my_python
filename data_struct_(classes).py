from typing import List,Union

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
    def __init__(self, name : str, grade : int, class_members : List[Union[Teacher,Student]]) -> None:
        self.name = name
        self.grade = grade
        self.class_members = {}
        
        for mem in class_members:
            if type(mem) is Student:
                self.class_members[mem.id] = mem
            elif type(mem) is Teacher:
                self.class_members[mem.subject] = mem
    
    def get_name_by_id(self,id):
        for st_id, st in self.class_members.items():
            if id == st_id:
                return st.name

    def get_teacher_by_subject(self, subject):
        for t_subject, teacher in self.class_members.items():
            if t_subject == subject:
                return teacher.name

classA = Class("math",12,[
    Student("A","male",1),
    Student("B","male",2),
    Student("X","female",3),
    Student("C","female",4),
    Teacher("H","male","math")
])

target_st = classA.get_name_by_id(3)    
print(target_st)
target_teacher = classA.get_teacher_by_subject("math")
print(target_teacher)

