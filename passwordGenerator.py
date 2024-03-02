import random, string

def generate_pass(lenght=12, upper=True, lower=True, digit=True, special=True):
    char = ''
    if upper:
        char += string.ascii_uppercase
    if lower:
        char += string.ascii_lowercase
    if digit:
        char += string.digits
    if special:
        char += string.punctuation
    
    
    if not char:
        print("Atleast one character type must be selected")
        return None
    
    password = ''.join(random.choice(char) for _ in range(lenght))
    return password

print("Welcome to pass generator")
len = int(input("Enter lenght of the password: "))
upper = input("Need to include uppercase? (y/n): ").lower() == 'y'
lower = input("Need to include lower? (y/n): ").lower() == 'y'
digit = input("Need to include digit? (y/n): ").lower() == 'y'
special = input("Need to include special? (y/n): ").lower() == 'y'
result = generate_pass(len, upper, lower, digit, special)
print(f"You generated password is: {result}")
