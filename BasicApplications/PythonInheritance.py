class ParentInfo:
  name      = "deepak"            # fields
  lastName  = "parab"
  age       = 28
  email     = "9664895285"
    
  def displayParentInfo(self): # self refers to the current class object
    print(type(self))    
    print("Display Parent Information")    
    print("Name: "+ParentInfo.name)
    print("Last Name : "+ParentInfo.lastName)
    print("Age: "+str(ParentInfo.age))
    print("Email Address: "+ParentInfo.email)


class ChildInfo(ParentInfo):      # inherit base class
  name      = "deepak"            # fields
  lastName  = "parab"
  age       = 28
  email     = "9664895285"
  
  def __init__(self,name,lastName,age,email): #parameterise constructor
    self.name = name
    self.lastName = lastName
    self.age = age
    self.email = email

  def displayChildInfo(self): # self refers to the current class object
    print("Display Child Information")
    print("Name: "+self.name)
    print("Last Name : "+self.lastName)
    print("Age: "+str(self.age))
    print("Email Address: "+self.email)

child = ChildInfo("Amol","Dadas",26,"amol@escanav.com")
child.displayParentInfo()  
child.displayChildInfo()  