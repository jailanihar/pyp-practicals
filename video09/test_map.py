from map import map
from pirate import pirate

m = map(7, 8)
print(m)

m.add_pirate(0, 1, pirate())
print(m)

m.add_pirate(0, 2, pirate('ABC', 2))
print(m)

m.move_pirate(0, 1, 0, 2)
print(m)

m.move_pirate(0, 1, 0, 2)
print(m)