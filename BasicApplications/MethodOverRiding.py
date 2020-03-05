class ParentInfo:
  def displayInfo(self):
    print("display parent info")  

class ChildInfo(ParentInfo):
  def displayInfo(self):
    print("display child info")  

pi = ParentInfo()
ci = ChildInfo()
pi.displayInfo()
ci.displayInfo()