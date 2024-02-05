# Variabel
types_of_people = 10

# Variablen x / String bruger tidligere nævnt variabel
x = f"There are {types_of_people} types of people." 

# 2 variabler
binary = "binary"
do_not = "don't"

# Variabel y / String bruger tidligere nævnt variabler 
y = f"Those who know {binary} and those who {do_not}." 

# 2 tidligere nævnte variabler bliver printet 
print(x)
print(y)

# 2 tidligere nævnte variabler bliver printet med string, som kontekst
print(f"I said: {x}")
print(f"I also said: '{y}'") 

# Variabel med boolian værdi
hilarious = False

# Variabel / String uden benyttelse af variabel i {}
joke_evaluation = "Isn't that joke so funny?! {}" # string

# print af tidligere nævnt variabel, som benytter sig af variabel, der indholder boolian værdi
print(joke_evaluation.format(hilarious)) # string

# 2 variabler som er strings
w = "This is the left side of..." # string 
e = "a string with a right side." # string

# Dette danner en længere string, grundet variablerne w og e indeholder en string
print(w + e)
