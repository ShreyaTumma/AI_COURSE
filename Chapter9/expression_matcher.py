from kanren import run, var, fact
import kanren.assoccomm as la

add = 'addition'
mult = 'multiplication'

# Declare operators as commutative and associative
fact(la.commutative, mult)
fact(la.commutative, add)
fact(la.associative, mult)
fact(la.associative, add)

# Define variables
a = var('a')
b = var('b')
c = var('c')

# Generate expressions
# expression_og = 3 * -2 + (1 + 2 * 3) * (-1)
expression_og = (add, (mult, 3, -2), (mult, (add, 1, (mult, 2, 3)), -1))
expression1 = (add, (mult, (add, 1, (mult, 2, a)), b), (mult, 3, c))
expression2 = (add, (mult, c, 3), (mult, b, (add, (mult, 2, a), 1)))
expression3 = (add, (add, (mult, (mult, 2, a), b), b), (mult, 3, c))


# Compare expressions
print(run(0, (a, b, c), la.eq_assoccomm(expression1, expression_og)))
print(run(0, (a, b, c), la.eq_assoccomm(expression2, expression_og)))

# Expression 3 will return nothing because it is structurally different
print(run(0, (a, b, c), la.eq_assoccomm(expression3, expression_og)))


