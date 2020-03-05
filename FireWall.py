import subprocess,ctypes,os,sys
from subprocess import Popen, DEVNULL

class Firewall:
  __ruleName = '' # rule name
  __dir      = '' # in/out
  __action   = '' # allow/block
  __program  = '' #'exe file path with exe name'
  __enable   = '' # yes
  __localPort= '' # add port to block specific port 

  def __init__(self,obj):
    self.__ruleName = obj.get('name')
    self.__dir      = obj.get('dir')
    self.__action   = obj.get('action')
    self.__program  = obj.get('program')
    self.__enable   = obj.get('enable')    
    self.__localPort= obj.get('localPort') 

  def check_admin(self):
    #Force to start application with admin rights
    try:
        isAdmin = ctypes.windll.shell32.IsUserAnAdmin()
    except AttributeError:
        isAdmin = False
    if not isAdmin:
        ctypes.windll.shell32.ShellExecuteW(None,'runas', sys.executable, __file__, None, 1)  

  def is_rule_present(self):    
    result = subprocess.call(
        f'netsh advfirewall firewall show rule name={self.__ruleName}', 
        shell=True, 
        stdout=DEVNULL, 
        stderr=DEVNULL
    ) 
    #if 1 return rule not present/ if 0 return then rule present
    return False if result == 1 else True  #Ternary Operator        
  
  def add_program_rule(self):
    if self.is_rule_present() is False :
      result = subprocess.call(
                  f'netsh advfirewall firewall add rule name={self.__ruleName} dir={self.__dir} action={self.__action} program={self.__program} enable={self.__enable}',                   
                  shell=True, 
                  stdout=DEVNULL, 
                  stderr=DEVNULL
              )
      if(result==0):
        print('[add_program_rule] rule:{self.__ruleName} added successfully')
      else :
        print('[add_program_rule] failed to add rule:{self.__ruleName}')
    else :  
      print(f'Rule {self.__ruleName} present try to modified rule')

  def remove_program(self):
    if self.is_rule_present() is True :
      result = subprocess.call(
                  f'netsh advfirewall firewall delete rule name={self.__ruleName} program={self.__program}',                   
                  shell=True, 
                  stdout=DEVNULL, 
                  stderr=DEVNULL
              )
      if(result==0):
        print('[remove_program] rule:{self.__ruleName} deleted successfully')
      else :
        print('[remove_program] failed to delete rule:{self.__ruleName}')     
    else :  
      print(f'Rule {self.__ruleName} not present')

  def add_port(self):
    if self.is_rule_present() is False :
      result = subprocess.call(
                  f'netsh advfirewall firewall add rule name={self.__ruleName} dir={self.__dir} action={self.__action} protocol=TCP localport={self.__localPort}',                   
                  shell=True, 
                  stdout=DEVNULL, 
                  stderr=DEVNULL
              )
      if(result==0):
        print('[add_port] rule:{self.__ruleName} added successfully')
      else :
        print('[add_port] failed to add rule:{self.__ruleName}')     
    else :  
      print(f'Rule {self.__ruleName} present try to modified rule')     

  def remove_port(self):
    if self.is_rule_present() is True :
      result = subprocess.call(
                  f'netsh advfirewall firewall delete rule name={self.__ruleName} protocol=TCP localport={self.__localPort}',                   
                  shell=True, 
                  stdout=DEVNULL, 
                  stderr=DEVNULL
              )
      if(result==0):
        print('[remove_port] rule:{self.__ruleName} deleted successfully')
      else :
        print('[remove_port] failed to delete rule:{self.__ruleName}')       
    else :  
      print(f'Rule {self.__ruleName} present try to modified rule')

  def modify_rule(self,rule_name, state):
    #Enable/Disable specific rule, 0 = Disable / 1 = Enable
    state, message = ('yes','Enabled') if state else ('no','Disabled')
    subprocess.call(
        f'netsh advfirewall firewall set rule name={rule_name} new enable={state}', 
        shell=True, 
        stdout=DEVNULL, 
        stderr=DEVNULL
    )
    print(f'Rule {rule_name} {message}')      

data = {"name":"deepak","dir":"in","action":"allow","program":"deepak","enable":"yes"} #add programm rule obj
#data = {"name":"deepak","dir":"in","action":"allow","localPort":"10443"} #add port rule obj
fw = Firewall(data)
fw.check_admin()
#fw.add_program_rule()      
#fw.remove_program()
#fw.add_port()
#fw.remove_port()

'''
usefull links
https://support.microsoft.com/en-in/help/947709/how-to-use-the-netsh-advfirewall-firewall-context-instead-of-the-netsh
'''