import unittest
from animals import Animal

class TestAnimal(unittest.TestCase):

	def setUp(self):
		self.bear_test = Animal("bear", 60, "Paul", "male", 200)
		self.panda_test = Animal("panda", 3, "Puff", "male", 50)

	def test_init(self):
		self.assertEqual(self.bear_test.species, 'bear')
		self.assertEqual(self.bear_test.age, 60)
		self.assertEqual(self.bear_test.name, 'Paul')
		self.assertEqual(self.bear_test.gender, 'male')
		self.assertEqual(self.bear_test.weight, 200)

	def test_animal_grow(self):
		self.bear_test.grow()
		self.assertEqual(self.bear_test.age, 61)
		self.assertEqual(self.bear_test.weight, 220)

	def test_animal_eat(self):
		self.bear_test.eat()
		self.assertEqual(self.bear_test.weight, 202)

	def test_chance_to_die(self):
		self.assertEqual(self.bear_test.chance_to_die(), 0.25)

	def test_is_dead(self):
		result = []
		for x in range(100):
			result.append(self.bear_test.is_dead())
		self.assertTrue(True in result)
		self.assertTrue(False in result)

	def test_food_to_eat(self):
		self.assertEqual(self.bear_test.amount_of_food(), 10)

	def test_cost_of_food(self): 
		self.assertEqual(self.bear_test.cost_of_food(), 40)

	def test_gestation_period(self):
		self.assertEqual(self.bear_test.gestation_period(), 7)

if __name__ == '__main__':
	unittest.main()