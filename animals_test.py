import unittest
from animals import Animal

class TestAnimal(unittest.TestCase):

	def setUp(self):
		self.animals_test = Animal("bear", 5, "Paul", "male", 200)

	def test_init(self):
		self.assertEqual(self.animals_test.species, 'bear')
		self.assertEqual(self.animals_test.age, 5)
		self.assertEqual(self.animals_test.name, 'Paul')
		self.assertEqual(self.animals_test.gender, 'male')
		self.assertEqual(self.animals_test.weight, 200)

	def test_animal_grow(self):
		self.animals_test.grow()
		self.assertEqual(self.animals_test.age, 6)
		self.assertEqual(self.animals_test.weight, 220)

	def test_animal_eat(self):
		self.animals_test.eat()
		self.assertEqual(self.animals_test.weight, 202)

	def test_chance_to_die(self):
		self.assertEqual(self.animals_test.chance_to_die(), 0.25)

	def test_is_dead(self):
		result = []
		for x in range(100):
			result.append(self.animals_test.is_dead())
		self.assertTrue(True in result)
		self.assertTrue(False in result)



if __name__ == '__main__':
	unittest.main()