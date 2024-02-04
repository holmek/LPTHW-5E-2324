# Dette er variablen biler
cars = 100

# Dette er variablen som indeholder pladsen i bilen
space_in_a_car = 4.0

# Dette er variablen som indeholder antal som kan køre
drivers = 30

# Dette er variablen som indeholder hvor mange personer der skal med
passengers = 90

# Dette er hvor mange biler tilbage efter hver person der kører har fået en bil
cars_not_driven = cars - drivers

# Dette er antallet er biler, som er kørende
cars_driven = drivers

# Dette er den samlet plads i bilerne, som er kørende
carpool_capacity = cars_driven * space_in_a_car

# Dette er gennemsnitet er folk som er i de kørende biler
average_passengers_per_car = passengers / cars_driven

# Dette er prints med strings, som benytter sig af de tidligere beskrevet variabler
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")

# Det har ingen betydningen om du skriver int 4 eller float 4.0, kun hvis float har en større værdi, såsom 4.5
# Det skal skrives som en float, hvis det er 4.5, pga. præcision, men ikke når det bare er heltal som 4
