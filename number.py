def counts_two_positive(r, y, a):
    positive_count = 0

    if r > 0:
        positive_count += 1
    if y > 0:
        positive_count += 1
    if a > 0:
        positive_count += 1

    if positive_count == 2:
        return True
    else:
        return False

result = counts_two_positive(1, -2, -3)
print(result)


