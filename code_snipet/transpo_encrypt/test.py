from mod.encrypt import encrypt
from mod.decrypt import decrypt

cText = encrypt('CN is not my favorite', '1234', '?')
print(cText)

cText = decrypt(cText, '4123', '?')
print(cText)