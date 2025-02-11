import sympy

# Step 1: Define p and q
p = 101
q = 127

# Compute n and φ(n)
n = p * q
phi_n = (p - 1) * (q - 1)

# Step 2: Choose public exponent e
e = 53  # Must be coprime with φ(n)

# Step 3: Compute private exponent d (modular inverse of e mod φ(n))
d = sympy.mod_inverse(e, phi_n)

# Step 4: Encryption function
def encrypt(message, e, n):
    return pow(message, e, n)

# Step 5: Decryption function
def decrypt(ciphertext, d, n):
    return pow(ciphertext, d, n)

# Message to encrypt
x = 217

# Encrypt message
ciphertext = encrypt(x, e, n)
print(f"Encrypted message: {ciphertext}")

# Decrypt message
decrypted_message = decrypt(ciphertext, d, n)
print(f"Decrypted message: {decrypted_message}")

# Verify if decryption is correct
assert decrypted_message == x, "Decryption failed!"
