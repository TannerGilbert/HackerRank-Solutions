import math


def cumulative_normal_distribution(x, mu, sigma):
    return 0.5 * (1 + math.erf((x - mu) / (sigma * math.sqrt(2))))


num_tickets = int(input())
num_students = int(input())
mean = float(input())
std = float(input())

print(round(cumulative_normal_distribution(num_tickets, mean * num_students, std * math.sqrt(num_students)), 4))
