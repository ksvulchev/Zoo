from animals import Animal

class Zoo:

	def __init__(self, capacity, budget):
		self.capacity = capacity
		self.budget = budget
		self.animals = []

	def add_animal(self, animal):
		self.animals.append(animal)