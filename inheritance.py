"""this is the programme for inheritance"""

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)




class Student(Person):
  def __init__(self,fname,lname):
    Person.__init__(self,fname,lname)
    print(self.firstname)
    print(self.lastname)

student_buddha=Student("buddha","roy")

student_buddha.firstname
student_buddha.lastname