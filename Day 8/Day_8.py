# Ceaser cipher. Returns encoded or decoded value shift a specified number of steps.__package__

# Encryption. Forward step
def encrypt (text, step):
  crypt = ''
  for e in [l for l in text.lower()]:
    if (ord(e) + step > ord('z')):
      crypt += chr(ord(e) + step - ord('z') + ord('a')-1)
      continue
    crypt += chr(ord(e) + step)
  return crypt

# print(encrypt('Xyzz', 5))

# Decryption. Backward step
def decrypt (text, step):
  crypt = ''
  for e in [l for l in text.lower()]:
    if ((ord(e) - step) < ord('a')):
      crypt += chr(ord('z')+1 - (ord('a') - (ord(e) - step)))
      continue
    crypt += chr(ord(e) - step)
  return crypt

# print(decrypt('cdee', 5))

# Choose encryption (encode=True) or Decryption (encode=False)
def ceaser_cipher (text, step, encode=True):
  if encode:
    return encrypt(text, step)
  return decrypt(text, step)

# print(ceaser_cipher('xyzz', 5, encode=True))
