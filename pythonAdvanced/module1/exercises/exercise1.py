#   determine without a computer what the script will execute
#   a) print([x**x for x in [1, 2, 3, 4]]) 
#   I quess: it will be => pow(x, 2) [exponent]
#   CHECK: 
print([x**x for x in [1, 2, 3, 4]])
#   RESULT: FALSE it's pow(x,x)

#   b) print([x/2 if x%2 else "Nope" for x in range(10, 16)]) 
#   I guess: it will be => [5, "Nope", 6, "Nope", 7, "Nope", 8]
#   CHECK:
print([x/2 if x%2 else "Nope" for x in range(10, 16)])
#   RESULT: False it's ["Nope", 5.5, "Nope", 6.5, "Nope", 7.5]
#   WHY: 10%2 => 1 for 'IF' it's TRUE