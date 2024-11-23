import math

ndeg = float(input('Enter Angle<degree> = '))
nrad = ndeg * (math.pi / 180)
print(ndeg, 'degree =', nrad, 'rad')

s = math.sin(nrad)

print('Angle <degree>', ndeg, 'sine is', s)
