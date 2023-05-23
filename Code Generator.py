import random
import string

def generate_code(length):
    characters = string.ascii_letters + string.digits
    code = ''.join(random.choice(characters) for _ in range(length))
    return code

code_length = 10
generated_code = generate_code(code_length)
print("Generated code:", generated_code)