import unittest
from animals import Animal
from zoo import Zoo

class TestZoo(unittest.TestCase):

	def setUp(self):
		self.zoo_test = Zoo(50, 100000)
		self.bear = Animal("bear", 5, "Paul", "male", 200)
		self.monkey = Animal("monkey", 2, "John", "male", 20)

	def test_init(self):
		self.assertEqual(self.zoo_test.capacity, 50)
		self.assertEqual(self.zoo_test.budget, 100000)		

	def test_add_animal(self):
		self.zoo_test.add_animal(self.bear)
		self.zoo_test.add_animal(self.monkey)
		self.assertIn(self.bear, self.zoo_test.animals)
		self.assertIn(self.monkey, self.zoo_test.animals)
		


if __name__ == '__main__':
	unittest.main()