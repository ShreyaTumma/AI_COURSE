from logpy import run, fact, eq, Relation, var

# Initialize relationships
adjacent = Relation()
coastal = Relation()

# Define input files to load the data from
file_coastal = 'coastal_states.txt'
file_adjacent = 'adjacent_states.txt'

# Load data from input files
with open(file_coastal, 'r') as f:
    line = f.read()
    coastal_states = line.split(',')

for state in coastal_states:
    fact(coastal, state)

with open(file_adjacent, 'r') as f:
    adjlist = [line.strip().split(',') for line in f if line and line[0].isalpha()]

for L in adjlist:
    head, tail = L[0], L[1:]
    for state in tail:
        fact(adjacent, head, state)

x = var()
y = var()

# Is Nevada adjacent to Louisiana?
output = run(0, x, adjacent('Nevada', 'Louisiana'))
print('\nIs Nevada adjacent to Louisiana? ')
print('Yes' if len(output) else 'No')

# States adjacent to Mississippi that are coastal
output = run(0, x, adjacent('Mississippi', x), coastal(x))
print('\nList states adjacent to Mississippi that are coastal: ')
for item in output:
    print(item)

# States adjacent to Oregon
output = run(0, x, adjacent('Oregon', x))
print('\nList states adjacent to Oregon: ')
for item in output:
    print(item)

# List of n states that border a coastal state
n = 7
output = run(n, x, coastal(y), adjacent(x, y))
print('\nList of ' + str(n) + ' states bordering a coastal state: ')
for item in output:
    print(item)

# States adjacent to Arkansas and Kentucky
output = run(0, x, adjacent('Arkansas', x), adjacent('Kentucky', x))
print('\nList states adjacent to Arkansas and Kentucky: ')
for item in output:
    print(item)