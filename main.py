from module1import SampleClass

print('Hello World!')

keith = SampleClass('Keith Dorgan', 'Human')

if keith.getName() != "Keith Morgan":
  keith.setName("Keith Morgan")

keith.greet()

print("Keith is a: {0}".format(keith.getSpecies()))
