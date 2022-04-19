class SampleClass {
  
  __species = 'Homo Sapien'
  
  def __init__(self, name):
    self.__name = name
  
  def getSpecies(self):
    print(SampleClass.__species)

  def getName(self):
    return self.__name
  
  def setName(self, newName):
    if (str(newName).isalpha())
      self.__name = str(newName)
      print("Name updated to {0}".format(newName))
    else:
      print("Numbers and special characters are not allowed!")
  
  def greet(self):
    return print("Hello my name is {0}, hope you're having a nice day!".format(self.__name))
