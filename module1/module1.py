class SampleClass:
  
  __allowedSpecies = ['Human', 'Dog', 'Cat', 'Lion', 'Bird']
    
  def __init__(self, name, species):
#     assert str(name).replace(' ', '').isalpha() == True
#     assert str(species).isalpha() == True
#     assert species in SampleClass.__allowedSpecies == True
    self.__name = name
    self.__species = species
  
  def getSpecies(self):
    return self.__species

  def getName(self):
    return self.__name
  
  def setName(self, newName):
    if str(newName).isalpha():
      self.__name = str(newName)
      print("Name updated to {0}".format(newName))
    else:
      print("Numbers and special characters are not allowed!")
  
  def setSpecies(self, newSpecies):
    if str(newSpecies).isalpha():
      if newSpecies in SampleClass.__allowedSpecies:
        self.__name = str(newName)
        print("Species updated to {0}".format(newName))
      else:
        print("Not in the list of allowed species currently, sorry!")
    else:
      print("Numbers and special characters do not constitute a valid species!")
  
  def greet(self):
    if self.__species == 'Human':
      return print("Hello my name is {0}, hope you're having a nice day!".format(self.__name))
    elif self.__species == 'Dog':
      return print('Woof, woof!! [Tail wiggling rigorously]')
    elif self.__species == 'Cat':
      return print('Meow! (MIND YOUR OWN BUSINESS HUMAN!)')
    elif self.__species == 'Lion':
      return print('RAWRRR!!')
    elif self.__species == 'Bird':
      return print('CJIRP!! [DUTCH BIRD CHIRPING]')
  
