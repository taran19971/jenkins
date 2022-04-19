import unittest
from module1 import SampleClass

class AllUnitTests(unittest.TestCase):
  
  def setUp(self):
    a = str(input('Enter a name'))
    b = str(input('Enter a species'))
    try:
      self.sampleinstance = SampleClass(a, b)
    except:
      print('Creating sample instance')
      self.sampleinstance = SampleClass('John Doe', 'Human')
      
  def test_string(self):
    self.assertTrue(self.sampleinstance.getName().isalpha())
    self.assertTrue(self.sampleinstance.getSpecies().isalpha())
    
  def test_valid_species(self):
    self.assertTrue(self.sampleinstance.getSpecies() in self.sampleinstance._SampleClass__allowedSpecies)
    
  def valid_return_type(self):
    self.assertTrue(self.sampleinstance.getName() != None)
    self.assertTrue(self.sampleinstance.getSpecies() != None)
    self.assertTrue(self.sampleinstance.greet() != None)
    
  def tearDown(self):
    self.sampleinstance.dispose()
   
if __name__ == '__main__':
  unittest.main()
    
