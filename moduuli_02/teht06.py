import random

three_digit_code = f"{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}"
four_digit_code = f"{random.randint(1,6)}{random.randint(1,6)}{random.randint(1,6)}{random.randint(1,6)}"
print(f"Kolmen numero koodi: {three_digit_code}")
print(f"Neljän numero koodi: {four_digit_code}")