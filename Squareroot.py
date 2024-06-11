import math
def sqrroot():
    first = int(input("What number do you want to square root?"))
    answer = math.sqrt(first)
    print(f"The square root of {first} is {answer}")

if __name__ == "__main__":
    sqrroot()