import random
import string


c = string.ascii_lowercase
c += string.ascii_uppercase
c += string.digits
c += string.punctuation
c += string.ascii_letters

p = ""

for i in range(8):
    p += random.choice(c)

print(p)