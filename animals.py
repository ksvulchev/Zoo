import random

class Animal:
	LIFE_EXPECTANCY = {"bear": 20, "wolf": 15, "monkey": 7}
	# rerprodukcionen period
	def __init__(self, species, age, name, gender, weight):
		self.species = species
		self.age = age
		self.name = name
		self.gender = gender
		self.weight = weight
		self.life_expectancy = self.age * 2

	def grow(self):
		self.age += 1
		self.weight += self.weight * 0.1 #the older the fatter each year

	def eat(self):
		self.weight += self.weight * 0.01

	def chance_to_die(self):
		if self.species in Animal.LIFE_EXPECTANCY:
			self.life_expectancy = Animal.LIFE_EXPECTANCY[self.species]
		return self.age / self.life_expectancy

	def is_dead(self):
		if random.random() < self.chance_to_die():
			return True
		return False
