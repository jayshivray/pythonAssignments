def myfunction(value1,value2):
  print("my function calling")
  print("parameter value1: "+value1)
  print("parameter value2: "+value2)

def displayInformation():
  print("displayInformation function calling")

def mutiargumentFunction(*param):
  print("parameter length: "+str(len(param)))
  print("parameter 1: "+param[0])
  print("parameter 1: "+param[1])
  print("parameter 1: "+param[2])

value1 = "value1"
value2 = "value2"
myfunction(value1,value2);  
displayInformation()
mutiargumentFunction("value1","value2","value4")
