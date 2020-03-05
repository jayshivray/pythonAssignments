class BaseClass1:
  def showBaseClass1(self):
    print("BaseClass1")
class BaseClass2:
  def showBaseClass2(self):
    print("BaseClass2")  
class ChildClass(BaseClass1,BaseClass2):
  def showChildInfo(self):
    print("show child class info")

cs = ChildClass()
cs.showChildInfo()
cs.showBaseClass1()      
cs.showBaseClass2()