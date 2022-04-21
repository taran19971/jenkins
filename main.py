from module1.module1 import SampleClass

print('Hello World!')

keith = SampleClass('Keith Dorgan', 'Human')

if keith.getName() != "Keith Morgan":
  keith.setName("Keith Morgan")

print("Keith is a: {0}".format(keith.getSpecies()))
  
keith.greet()
