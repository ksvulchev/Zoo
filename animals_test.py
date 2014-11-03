import unittest
from animals import Animal

class TestAnimal(unittest.TestCase):

	def setUp(self):
		self.animals_test = Animal("bear", 7, "Paul", "male", 200)

	def test_init(self):
		self.assertEqual(self.animals_test.species, 'bear')
		self.assertEqual(self.animals_test.age, 7)
		self.assertEqual(self.animals_test.name, 'Paul')
		self.assertEqual(self.animals_test.gender, 'male')
		self.assertEqual(self.animals_test.weight, 200)






if __name__ == '__main__':
	unittest.main()