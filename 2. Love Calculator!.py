"""
This code is when a user inputs two names, it can see how
many "true love" letters occur in the names and see how well are they
going on.
Easy python practice.
"""


print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")
combined_name = name1 + name2
lowered_name = combined_name.lower()

t = (lowered_name.count("t"))
r = (lowered_name.count("r"))
u = (lowered_name.count("u"))
e = (lowered_name.count("e"))
l = (lowered_name.count("l"))
o = (lowered_name.count("o"))
v = (lowered_name.count("v"))

true = str(t + r + u + e)
love = str(l + o + v + e)
true_love = int(true + love)

if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love >= 40 or true_love <= 50:
    print(f"Your score is {true_love}, you are alright together!")
else:
    print(f"Your score is {true_love}")


