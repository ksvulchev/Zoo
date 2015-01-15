from animals import Animal

class Zoo:

	def __init__(self, capacity, budget):
		self.capacity = capacity
		self.budget = budget
		self.animals = []
		self.income_per_animal = 60
		self.months = 0
		self.pregnant_animals = {}
		self.animals_given_birth = {}

	def add_animal(self, animal):
		self.animals.append(animal)

	def animals_in_zoo(self):
		return len(self.animals)

	def daily_income(self):
		return self.income_per_animal * self.animals_in_zoo()

	def daily_outcome(self):
		total_outcome = 0
		for animal in self.animals:
			total_outcome += animal.cost_of_food()
		return total_outcome

	def is_not_pregnant(self, animal):
		if animal in self.pregnant_animals:
				return False
		return True

	def male_female_couple(self, species):
		is_male = False
		is_female = False

		for animal in self.animals:
			if animal.species == species:
				if animal.gender == "male":
					is_male = True
				elif animal.gender == "female" and self.is_not_pregnant(animal):
					is_female = True
					self.pregnant_animals[animal] = 0	
		return is_female and is_male

	def has_given_birth(self, animal):
		print(self.animals_in_zoo())
		if self.pregnant_animals[animal] >= animal.gestation_period():
			months_sunce_birth = self.pregnant_animals[animal] - animal.gestation_period()
			self.add_to_given_birth(animal, months_sunce_birth)
			self.add_animal_child(animal)
		else:
			print ("{} has not given birth".format(animal.name))
		print(self.animals_in_zoo())

	def add_animal_child(self, parent):
		baby_species = parent.species
		baby_name = "{} Jr".format(parent.name)

		baby = Animal(baby_species, 0, baby_name, "male", 5)
		self.add_animal(baby)
		
	def add_to_given_birth(self, animal, months):
		if animal not in self.animals_given_birth:
			self.animals_given_birth[animal] = months

	def pass_months(self, months):
		self.months += months
		for animal, pregnancy_months in self.pregnant_animals.items():
			self.pregnant_animals[animal] += months
			self.has_given_birth(animal)
		self.clear_animals_given_birth()
		self.clear_animals_from_given_birth()

	def clear_animals_given_birth(self):
		for animal in self.animals_given_birth:
			self.pregnant_animals.pop(animal, None)

	def clear_animals_from_given_birth(self):
		to_be_cleared = []

		for animal in self.animals_given_birth:
			if self.animals_given_birth[animal] >= 6:
				to_be_cleared.append(animal)

		for not_pregnant_animal in to_be_cleared:
			self.animals_given_birth.pop(not_pregnant_animal)








	def show_animals(self):
		print(self.animals_given_birth)
		print(self.pregnant_animals)


