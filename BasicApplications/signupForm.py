class BasicInformation:
  __name          = ""
  __lastName      = ""
  __emailId       = ""
  __mobileNumber  = ""
  __password      = ""

  def displayUserInfo(self):
    print("Name: "+self.__name)
    print("Last Name: "+self.__lastName)
    print("Email Address: "+self.__emailId)
    print("Mobile Number: "+self.__mobileNumber)
    print("Password: "+self.__password)    

  def validatePassword(self,fPass,sPass):
    if fPass.lower()!=sPass.lower() :
      return False
    else:
      return True

  def acceptUserInputs(self):
    print("*******SIGN-UP FORM for personal Details*******")
    self.__name         = input("Enter username:")
    self.__lastName     = input("Enter LastName:")
    self.__emailId      = input("Enter Email Address:")
    self.__mobileNumber = input("Enter Mobile Number:")
    password1 = input("Enter Password:")
    password2 = input("Re Enter Password:")    
    isPasswordCheck = self.validatePassword(password1,password2)
         
    if isPasswordCheck is False :          
      for x in range(2):
        print("password not match please enter correct password Attempt "+str(x+1))
        password1 = input("Enter Password:")
        password2 = input("Re Enter Password:")
        isPasswordCheck = self.validatePassword(password1,password2)    
        if isPasswordCheck is True :
          break   

    if isPasswordCheck is True :         
      self.__password = password1
      self.displayUserInfo()
    else :
      print("Terminating Application")
      return False

info = BasicInformation()
info.acceptUserInputs()
