import math


def cumulative_normal_distribution(x, mu, sigma):
    return 0.5 * (1 + math.erf((x - mu) / (sigma * math.sqrt(2))))


max_weight = int(input())
num_boxes = int(input())
mean = int(input())
std = int(input())

print(round(cumulative_normal_distribution(max_weight, mean * num_boxes, std * math.sqrt(num_boxes)), 4))
