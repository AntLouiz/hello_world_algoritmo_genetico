import string

# alfabeto com letras maiusculas
ascii_uppercase = list(string.ascii_uppercase)

# alfabeto om letras minusculas
ascii_lowercase = list(string.ascii_lowercase)

ALPHABET = ascii_lowercase + [' ']

MASTER_SOLUTION = 'hello world'
MASTER_SOLUTION_FITNESS = 0

for w in MASTER_SOLUTION:
    MASTER_SOLUTION_FITNESS += ord(w)

MAX_ITERATIONS = 200000
INITIAL_POPULATION = 100