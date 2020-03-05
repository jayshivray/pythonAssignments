import os
import sys
import json

class BasicInformation:
  __name          = ""
  __lastName      = ""
  __emailId       = ""
  __mobileNumber  = ""
  __password      = ""

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
      data = self.getSignupJsonData() #get data in string format      
      if(len(data)!=0):
        self.saveSignupInfo(data)
    else :
      print("Terminating Application")
      return False

  def readSignupData(self):# this function read json string and convert into python object to read
    userInfoPath = os.path.join(self.getApplicationPath(),"userInfo.json")
    jsonfile = open(userInfoPath, "r")
    print(jsonfile.read())
 
  def displayUserInfo(self):# this function read userInfo.json from script path and read json string and display
    userInfoPath = os.path.join(self.getApplicationPath(),"userInfo.json")
    jsonfile     = open(userInfoPath, "r")
    jsondata     = jsonfile.read()
    pythonobject = json.loads(jsondata)              #convert string to python object 
    personalInfo = pythonobject.get('personalInfo')  #personalInfo type of object dict 

    print("Name: "+personalInfo.get('name'))
    print("Last Name: "+personalInfo.get('lastName'))
    print("Email Address: "+personalInfo.get('email'))
    print("Mobile Number: "+personalInfo.get('mobile'))
    print("Password: "+personalInfo.get('password'))  

  def getSignupJsonData(self):#this function create json using python object and convert into json string 
    data = {
          "personalInfo":{
            "name":self.__name,
            "lastName":self.__lastName,
            "email":self.__emailId,
            "mobile":self.__mobileNumber,
            "password":self.__password
            }
          }
    # refer https://realpython.com/python-json/
    #json.dumps(data,indent=4)
    return json.dumps(data)                        #convert python objects to json string         

  def getApplicationPath(self):    
    if getattr(sys, 'frozen', False):
      application_path = os.path.dirname(sys.executable)
    elif __file__:
      application_path = os.path.dirname(os.path.abspath( __file__ ))
      
    return os.path.join(application_path)    
    
  def saveSignupInfo(self,jsondata):
    userInfoPath = os.path.join(self.getApplicationPath(),"userInfo.json")
    signupData   = jsondata
    if os.path.exists(userInfoPath) is False : #save user info in json file here
      filetxt = open(userInfoPath,"wt")    
      filetxt.write(signupData)
      filetxt.close()
    
        
info = BasicInformation()
info.acceptUserInputs()
info.displayUserInfo()

'''
  This Application store User signup Information in .txt file

'''