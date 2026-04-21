def calculate_average(numbers):
    # This will cause a ZeroDivisionError if the list is empty
    total = sum(numbers)
    return total / len(numbers)

data = []
print(calculate_average(data))
