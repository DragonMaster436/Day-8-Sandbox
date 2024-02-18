# def greet(n):
#     print(f"Hello!! {n}.")
#     print("My friend,")
#     print("how are you doing today?")

# name = input("what is your name? ")
# greet(name)

def greet(name, location):
    print(f"Hello!! {name}.")
    print(f"How's the weather in {location}? ")

thing1 = input("what's your name? ")
thing2 = input("Where are you? ")

greet(name=thing1, location=thing2)
