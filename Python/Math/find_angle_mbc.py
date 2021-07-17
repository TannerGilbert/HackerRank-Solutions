import math

ab = int(input())
bc = int(input())

ac = math.sqrt(pow(ab, 2) + pow(bc, 2))
mc = ac / 2.
bc_2 = bc / 2.
print(str(round(math.degrees(math.acos(bc_2/mc)))) + "\N{DEGREE SIGN}")
