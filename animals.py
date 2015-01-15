import random

class Animal:
	LIFE_EXPECTANCY = {"bear": 240, "wolf": 180, "monkey": 84, "panda": 120}
	FOOD_PRICE_ANIMAL = {	
					"bananas":	[1,				#price
								["monkey"]],	#animals which eat this food

					"bamboo": 	[2,
								["panda"]],

					"meat": 	[4,
								["wolf","bear"]]
				}
	ANIMAL_GESTATION_PERIOD = {"bear": 7, "monkey": 9} #the gestation period in months
	# rerprodukcionen period SQL lite
	def __init__(self, species, age, name, gender, weight):
		self.species = species
		self.age = age
		self.name = name
		self.gender = gender
		self.weight = weight
		self.life_expectancy = self.age * 2
		self.pregnant = False

	def grow(self):
		self.age += 1
		self.weight += self.weight * 0.1 #the older the fatter each year

	def food_to_eat(self):
		for food, value in Animal.FOOD_PRICE_ANIMAL.items():
			if self.species in value[1]:
				#print (food)
				return food

	def amount_of_food(self):
		return self.weight * 0.05  #0.05 kilos of food per animal kilo
	
	def cost_of_food(self):
		food_price = Animal.FOOD_PRICE_ANIMAL[self.food_to_eat()][0]
		kilos_of_food = self.amount_of_food()
		#print (food_price * kilos_of_food)
		return food_price * kilos_of_food

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

	def gestation_period(self):
		if self.species in Animal.ANIMAL_GESTATION_PERIOD:
			return Animal.ANIMAL_GESTATION_PERIOD[self.species]
