class ParentInfo:
  __identity = "BaseClass"
  name = "Parent"
  lastName = "Class"
  
  def __init__(self):
    print("Parent class constructor invoke")
    print("Name: "+self.name)
    print("LastName: "+self.lastName)
    print("Identity: "+self.__identity)

class ChildInfo(ParentInfo):
 
  def displayInfo(self):    
    print("Parent Name: "+self.name)
    print("Parent LastName: "+self.lastName)    

child = ChildInfo()
child.name = "Deepak"
child.lastName = "Parab"
child.displayInfo()


'''
Note :
In python, we can also perform data hiding by adding the double underscore (___) as a prefix 
to the attribute which is to be hidden. 
After this, the attribute will not be visible outside of the class through the object.
'''