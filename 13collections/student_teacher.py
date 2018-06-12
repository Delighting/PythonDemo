#!/usr/bin/env python3

import sys
from collections import Counter

class Person(object):
    """
    返回具有给定名称的 Person 对象
    """

    def __init__(self, name):
        self.name = name

    def get_details(self):
        """
        返回包含人名的字符串
        """
        return self.name


class Student(Person):
    """
    返回 Student 对象，采用 name, branch, year 3 个参数
    """

    def __init__(self, name, branch, year, grade):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year
        self.grade = grade

    def get_details(self):
        """
        返回包含学生具体信息的字符串
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)

    def get_grade(self):
        c = Counter(self.grade)
        l = c.most_common()
        p = 0
        f = 0
        for x,n in l:
            if x == 'A' or x == 'B' or x == 'C':
                p += n
            if x == 'D':
                f += n

        return 'Pass: {}, Fail: {}'.format(p, f)


class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """
    def __init__(self, name, papers,grade):
        Person.__init__(self, name)
        self.papers = papers
        self.grade = grade

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))

    def get_grade(self):
        c = Counter(self.grade)
        l = c.most_common()
        o = []
        for x,n in l:
            o.append('{}: {}'.format(x, n))
        return ', '.join(o)


# person1 = Person('Sachin')
# student1 = Student('Kushal', 'CSE', 2005)
# teacher1 = Teacher('Prashad', ['C', 'C++'])

# print(person1.get_details())
# print(student1.get_details())
# print(teacher1.get_details())

if __name__ == '__main__':
    if len(sys.argv) > 1:
        a1 = sys.argv[1]
        if a1 == 'techer':
            t = Teacher('tt',[],sys.argv[2])
            print(t.get_grade())
        if a1 == 'student':
            s = Student('s', 'CSE', 2005,sys.argv[2])
            print(s.get_grade())
