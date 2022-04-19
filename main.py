from module1import SampleClass

print('Hello World!')

keith = SampleClass('Keith Dorgan')

if keith.getName() != "Keith Morgan":
  keith.setName("Keith Morgan")

keith.greet()

print("Keith is a:")
keith.getSpecies()
