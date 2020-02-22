from random import randint

i = 0

while True:
    rand = randint(1, 10)
    i += 1
    if rand == 5:
        break
print(i)