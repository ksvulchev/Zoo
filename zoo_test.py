import unittest
from animals import Animal
from zoo import Zoo

class TestZoo(unittest.TestCase):

	def setUp(self):
		self.zoo_test = Zoo(50, 100000)
		self.bear_male = Animal("bear", 5, "Paul", "male", 200)
		self.bear_female = Animal("bear", 4, "Lucy", "female", 170)
		self.monkey = Animal("monkey", 2, "John", "male", 20)
		self.monkey_female = Animal("monkey", 2, "Molly", "female", 15)

	def test_init(self):
		self.assertEqual(self.zoo_test.capacity, 50)
		self.assertEqual(self.zoo_test.budget, 100000)		

	def test_add_animal(self):
		self.zoo_test.add_animal(self.bear_male)
		self.zoo_test.add_animal(self.monkey)
		self.assertIn(self.bear_male, self.zoo_test.animals)
		self.assertIn(self.monkey, self.zoo_test.animals)

	def test_daily_income(self):
		self.zoo_test.add_animal(self.bear_male)
		self.zoo_test.add_animal(self.bear_female)
		self.zoo_test.add_animal(self.monkey)
		self.assertEqual(self.zoo_test.daily_income(), 180)

	def test_daily_outcome(self):
		self.zoo_test.add_animal(self.bear_male)
		self.zoo_test.add_animal(self.bear_female)
		self.assertEqual(self.zoo_test.daily_outcome(), 74)

	def test_is_not_pregnant(self):
		self.zoo_test.add_animal(self.bear_male)
		self.zoo_test.add_animal(self.bear_female)
		self.zoo_test.male_female_couple("bear")
		self.assertIn(self.bear_female, self.zoo_test.pregnant_animals)

	def test_pass_months(self):
		self.zoo_test.add_animal(self.bear_male)
		self.zoo_test.add_animal(self.bear_female)
		self.zoo_test.male_female_couple("bear")
		self.zoo_test.add_animal(self.monkey)
		self.zoo_test.add_animal(self.monkey_female)
		self.zoo_test.male_female_couple("monkey")
		self.zoo_test.pass_months(14)

		self.zoo_test.show_animals()

	def test_male_female_couple(self):
		self.zoo_test.add_animal(self.monkey)
		self.zoo_test.add_animal(self.bear_male)
		self.zoo_test.add_animal(self.bear_female)
		self.assertTrue(self.zoo_test.male_female_couple("bear"))


if __name__ == '__main__':
	unittest.main()