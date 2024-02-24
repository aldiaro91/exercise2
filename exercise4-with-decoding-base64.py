import string
import base64

def decode(x):
  for i in range(97):
    calculated = pow(i, 101, 97)
    if calculated == x:
      return i
  return 0

def string_to_utf8_codes(s):
    return [ord(c) for c in s]

# Przykład użycia
s = '''UBY5GFQUOEE4Bzo5YFcNCjYOTlVZGUo9SRolYCA3CCUPSR0HJxMUIlkVCxIgUTsNTU0nDCVWIwsMEFpYXQdGVwI6TwpdBEZNHzwEVEMBKgNbJVYEPQVgJwAUWBYQMVMJKRFKPVcRAFszJkxWMhE3Bg8jK1g+KwgEPRgIHSQ0AUxWIzAjDkxaYB5LST0jK1wEQRoXNkZfEl4tEAM+Dy5PMh8bQiIdEUE5IVkVYEo2MCg5Sg5SVD4rFVkZHiNaJVMpPSQ0SAspKxhFYEc/MFsAOk0fRzkIJSYiT0hGFStBVTtHAgkKMyIyYC0TUVhWUFA4Ly4ePisSL0hVPzAWRTcFPgMqNgMqLk1FDjlKRWAAEF1OG1U/YFcNTUo9TDUyCAscIBoaVyNQOw06Eh5YFg5DO0dAIT8bPEwSNUhAADY4BgsSXhFEDk5ZFQkESBAkLUo9TBtGKRY0Sj0wWSI0PAMjBycaQzFaWC8yEUFgHzZVPFFeWk4lKSxXU0RcKEJZDGAiTFpDLhMTME9bADo5JwwIQjgHNEYpBxpXB0okMFkMEDIiLlkPIwsmX1ZDKVMZOQkKNgcnRS9QPFQZFCJSGFcNGgBWRF1FLQATNRc+HyQmXy9MWiIWHSQ3QgIeU0REDj9XU1Y9JTA2PSsRSxFUCBgICTsKEQNJPUwMR18OCRYHAkAlKSAeIz0+LSI7Rz9gG08KUEI7Rx4fJF5LJDMbLFcDW0gQDkxaE00nExMvSTQ/NUhZQTgIC1M/GRExDhdJNRcmJwBWSxgVT1VZVw0aAFZeLRBTEmAZEQUpQgA6PA0ZODNfJik9Dk4sCCU5R182Bg9bVQFSGA8rXFJdDgE6EDIbDRlXBTcjMEkaXw4+XUk9FjQpLTxQNABRXi4KWzUHClMSHiM2B0MOQx1aWDAOOhIUSEBNKRY0LRUUJz0YFVVMNQtCHRFXDSwVVUg='''

s = base64.b64decode(s).decode('utf-8')
print(s)
def convert_and_shift(indexes):
    # List to hold the shifted strings
    shifted_strings = []

    for i in range(0,100):
        # Add i to every index
        shifted_indexes = [((index) + i) for index in indexes]

        # Convert back to string, taking care of bounds
        shifted_string = ''.join(string.printable[index % 97] for index in shifted_indexes)

        # Add the shifted string to the list
        shifted_strings.append(shifted_string)

    return shifted_strings

utf8_codes = string_to_utf8_codes(s)
results_before_shift = []
num_to_carry = 0

# Oto lista odwrotności dla liczb od 1 do 96 w modulo 97 (wygenerowana z pomocą gpt-4):
c_values = [1, 49, 65, 73, 39, 81, 14, 85, 54, 68, 53, 89, 15, 7, 13, 91, 40, 27, 46, 34, 37, 75, 38, 93, 66, 56, 18, 52, 87, 55, 72, 94, 50, 20, 61, 62, 21, 23, 5, 17, 71, 67, 88, 86, 69, 19, 64, 95, 2, 33, 78, 28, 11, 9, 30, 26, 80, 92, 74, 76, 35, 36, 77, 47, 3, 25, 42, 10, 45, 79, 41, 31, 4, 59, 22, 60, 63, 51, 70, 57, 6, 84, 90, 82, 8, 44, 29, 43, 12, 83, 16, 58, 24, 32, 48, 96]

for c in c_values:
    print(c)
    for code in utf8_codes:
        partial_result = (((decode(code) - num_to_carry)) * c) % 97
        num_to_carry = code
        results_before_shift.append(partial_result)

    results = convert_and_shift(results_before_shift)
    with open('results9.txt', 'w') as file:
        for text in results:
            for key, value in my_dict.items():
                text = text.replace(key, value)
            file.write(text)
