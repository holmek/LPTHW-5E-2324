formatter = "{} {} {} {}"

# Print som er formateret med 4 {} {} {} {}, 5 print benytter sig alle af maks 4 datayper hinanden
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))

# formatter 4*4 som bliver til 16 {}
print(formatter.format(formatter, formatter, formatter, formatter)) 
print(formatter.format(
    "Øvelse 1",
    "Øvelse 2",
    "Øvelse 3",
    "Øvelse 4"
))
