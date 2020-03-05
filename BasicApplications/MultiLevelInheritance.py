class ParentInfo:
  name      = "Bala"            # fields
  lastName  = "parab"
  age       = 28
  email     = "9664861224"
    
  def displayParentInfo(self): # self refers to the current class object   
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
    print("Name: "+ChildInfo.name)
    print("Last Name : "+ChildInfo.lastName)
    print("Age: "+str(ChildInfo.age))
    print("Email Address: "+ChildInfo.email)

class SecondChildInfo(ChildInfo):      # inherit base class
  name      = ""            # fields
  lastName  = ""
  age       = 0
  email     = ""
  
  def __init__(self,name,lastName,age,email): #parameterise constructor
    self.name = name
    self.lastName = lastName
    self.age = age
    self.email = email

  def displaySecondChildInfo(self): # self refers to the current class object
    print("Display Second Child Information")
    print("Name: "+self.name)
    print("Last Name : "+self.lastName)
    print("Age: "+str(self.age))
    print("Email Address: "+self.email)

sc = SecondChildInfo("Durva","Parab",26,"durva@escanav.com")
sc.displayParentInfo()  
sc.displayChildInfo()  
sc.displaySecondChildInfo()