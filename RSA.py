import math
import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    a, b = e, phi
    x0, x1 = 0, 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    return x1 % phi

def encrypt(message, e, n):
    return pow(message, e, n)  


def decrypt(ciphertext, d, n):
    return pow(ciphertext, d, n) 

def check_prime(number):
    if not number.isnumeric():
        # print("hey")
        return False
    number = int(number)    
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            # print("hey2")
            return False
    return True 

def get_e(phi):
    while True:
        e = random.randrange(3, phi_n, 2)  
        if gcd(e, phi_n) == 1: 
            return e

prime = True
while prime:
    p = input("Give me a prime number for P")
    prime = not check_prime(p)
   
prime = True
while prime:
    q = input("give me another prime number for Q")
    prime = not check_prime(q)
x = ""
while not x.isnumeric():
    x = input("give me any number for our message")
p = int(p)
q = int(q)
x = int(x)
n = p * q
phi_n = (p - 1) * (q - 1)
e = get_e(phi_n)  
d = mod_inverse(e, phi_n)

ciphertext = encrypt(x, e, n)
print(f"Encrypted message: {ciphertext}")


decrypted_message = decrypt(ciphertext, d, n)
print(f"Decrypted message: {decrypted_message}")

# Verify if decryption is correct
assert decrypted_message == x, "Decryption failed!"
