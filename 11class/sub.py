#!/usr/bin/env python3

class Person:
  def __init__(self, name):
    self.name = name

  def get_detail(self):
    return self.name

class Student(Person):
  def __init__(self, name, branch, year):
    Person.__init__(self, name)
    self.branch = branch
    self.year = year

  def get_detail(self):
    return 'name {}, branch {}, year {}'.format(self.name, self.branch, self.year)

class Teacher(Person):
  def __init__(self, name, paper):
    Person.__init__(self,name)
    self.paper = paper

  def get_detail(self):
    return 'name {}, paper {}'.format(self.name, self.paper)

class Man():
  def __init__(self):
    self.sex = 'male'

class ManTecher(Teacher, Man):
  def __init__(self, name , paper):
    Teacher.__init__(self,name,paper)
    Man.__init__(self)

  def get_detail(self):
    return 'name {}, paper {}, sex {}'.format(self.name, self.paper, self.sex)

s = Student('ll', 'br', '2014')
t = Teacher('llt', 'pa')
mt = ManTecher('llmt','pam')

print(s.get_detail())
print(t.get_detail())
print(mt.get_detail())

del s
