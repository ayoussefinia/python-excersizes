for num in range(1,21):
    if num % 2 == 0:
        if num != 4:
            print(f"{num} is even")
        else :
            print(f"{num} is unlucky")
    elif num % 2 != 0:
        if num != 13:
            print(f"{num} is odd")
        else :
            print(f"{num} is unlucky")

