animals_tuple = 'Cat', 'Turtle', 'Snake', 'Dog',
print(animals_tuple)

cat, turtle, snake, dog = animals_tuple  # 'Cat', 'Turtle', 'Snake', 'Dog'
print(cat, turtle, snake, dog)

cat, turtle, snake, dog = ('Cat', 'Turtle', 'Snake', 'Dog')

pet_1 = 'Cat'
pet_2 = 'Dog'

pet_1, pet_2 = (pet_2, pet_1,)
print(f"Теперь pet_1 это {pet_1}")
print(f"Теперь pet_2 это {pet_2}")
