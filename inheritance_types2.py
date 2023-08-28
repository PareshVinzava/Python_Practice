# Multiple inheritance

class Student:
    def method1(self,sno,sname):
        self.sno = sno
        self.sname = sname

    def method2(self):
        print("student no : ",self.sno)
        print("student Name : ",self.sname)


class Marks:
    def setmarks(self,m1,m2):
        self.mark1 = m1
        self.mark2 = m2

    def putmarks(self):
        print("mark1 :", self.mark1)
        print("mark2 :" , self.mark2)

class result(Marks,Student): 
    def calc(self):
        self.total = self.mark1 + self.mark2

    def puttotal(self):
        print("Total :", self.total)


r = result()

r.method1(60,"Lucky")
r.setmarks(50,60)
r.calc()
r.method2()
r.putmarks()
r.puttotal()

