means = list(map(float, input().split()))

print(round(160 + 40 * (means[0] + means[0]**2), 3))
print(round(128 + 40 * (means[1] + means[1]**2), 3))
