import random

def generate_random_number(start, end):
    return random.randint(start, end)

start_range = 1  # Start of the range
end_range = 100  # End of the range

random_number = generate_random_number(start_range, end_range)
print("Random number:", random_number)