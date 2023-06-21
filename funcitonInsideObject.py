# This is the code to put function inside object
class student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def func1(self):
        print(self.name)
        print(20+self.age)


student_obj = student("buddha",20)
student_obj.func1()