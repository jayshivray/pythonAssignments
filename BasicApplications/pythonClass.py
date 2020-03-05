class PersonInfo:
  name = "deepak"            # fields
  lastName = "parab"
  age = 28
  email = "9664895285"
  
  #def __init__(self): non parameterise constructore
  def __init__(self,name,lastName,age,email): #parameterise constructor
    self.name = name
    self.lastName = lastName
    self.age = age
    self.email = email

  def displayInformation(self): # self refers to the current class object
    print("Name: "+self.name)
    print("Last Name : "+self.lastName)
    print("Age: "+str(self.age))
    print("Email Address: "+self.email)

bs = PersonInfo("Amol","Dadas",26,"amol@escanav.com")  #creating object of class
print(bs.displayInformation())
