import math

sample_size = int(input())
mean = int(input())
std = int(input()) / math.sqrt(sample_size)
distribution_percentage = float(input())
z_value = float(input())

print(round(mean - z_value * std, 2))
print(round(mean + z_value * std, 2))
