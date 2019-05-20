t = (5,'program', 13)

# t[1] = 'program'
print("t[1] = ", t[1])

# t[0:3] = (5, 'program', (13))
print("t[0:3] = ", t[0:3])

# Generates error
# Tuples are immutable
t[0] = 10
