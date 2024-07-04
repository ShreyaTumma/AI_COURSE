from logpy import *
from logpy.core import lall

people = var()

# Define the rules
rules = lall(
    # Four people
    (eq, (var(), var(), var(), var()), people),
    
    # Steve has a blue car
    (membero, ('Steve', var(), 'blue', var()), people),
    
    # Person who owns a cat lives in Canada
    (membero, (var(), 'cat', var(), 'Canada'), people),
    
    # Matthew lives in USA
    (membero, ('Matthew', var(), var(), 'USA'), people),
    
    # Jack has a cat
    (membero, ('Jack', 'cat', var(), var()), people),

    # Person with black car lives in Austrailia
    (membero, (var(), var(), 'black', 'Austrailia'), people),

    # Alfred lives in Austrailia
    (membero, ('Alfred', var(), var(), 'Austrailia'), people),

    # Person who has a dog lives in France
    (membero, (var(), 'dog', var(), 'France'), people),

    # Who has a rabbit?
    (membero, (var(), 'rabbit', var(), var()), people)
)

solutions = run(0, people, rules)
output = [house for house in solutions[0] if 'rabbit' in house][0][0]

# Print output
print('\n' + output + ' is the owner of the rabbit')
print('All details for each person:')
attributes = ['Name', 'Pet', 'Color', 'Country']
print('\n' + '\t\t'.join(attributes))
print('=' * 57)
for item in solutions[0]:
    print('')
    print('\t\t'.join([str(x) for x in item]))
