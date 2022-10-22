"""

List:
-----
Louis has been making good progress in Zortan and has made
new friends. All of them are meeting today and Louis wants
to write a program that can greet all of them.

In Zortan, people greet with saying "Zola"

Info:
-----
Lists are mutable data structures, that means the data inside can be mutated.
Index always starts from 0.
"""

# It's convenient to group all friends together using a `List`
# and then greet them
from operator import contains


friends: list[str] = ["Cece", "Roko", "Chiko", "Niko"]

# -------------------------------------------------------
# Time to greet freinds ysing a for-in loop
# -------------------------------------------------------

for friend in friends:
    print(f"Zola {friend}")

# -------------------------------------------------------
# Find the number of friends
# -------------------------------------------------------
print(f"Friends length: {len(friends)}")

# -------------------------------------------------------
# Louis had a fight with Niko and wants to unfriend him
# -------------------------------------------------------
unfriend = friends.pop()
print(f"Unfriend: {unfriend}")
print(f"Friends: {friends}")

# -------------------------------------------------------
# Louis makes a new friend "Ziko"
# -------------------------------------------------------
friends.append("Ziko")
print("Adding friend Ziko")
print(f"New friends list {friends}")

# -------------------------------------------------------
# Louis wants to know his 3rd friend
# -------------------------------------------------------
print(f"3rd friend in the list {friends[2]}")

# -------------------------------------------------------
# Oh no, Louis had a fight with Roko, wants to remove from the list
# -------------------------------------------------------

friends.remove("Roko")
print("Removing Roko")
print(f"New Friends list {friends}")

# -------------------------------------------------------
# Louis wants to add Roko back to his friends list
# -------------------------------------------------------

friends.insert(1, "Roko")
print("Adding back Roko")
print(f"New Friends list {friends}")


# -------------------------------------------------------
# Louis wants to confirm Roko in his friends list
# -------------------------------------------------------
if "Roko" in friends:
    print("Yay! Roko is in Friends list")
else:
    print("Oops! Roko is not in Friends list")


# -------------------------------------------------------
# Louis patches up with Niko, and he becames his no. 1 friend
# -------------------------------------------------------
friends.insert(0, "Niko")
print("Added Niko back as No.1 friend")
print(f"Friends:  {friends}")


# -------------------------------------------------------
# Louis wants to sort his friends alphabeticaly
# -------------------------------------------------------

friends.sort()
print("Louis wants to sort his friends alphabetically")
print(f"Friends: {friends}")

# -------------------------------------------------------
# Louis wants to reverse the sorting order of his friends
# -------------------------------------------------------

friends.reverse()
print("Louis wants to sort his friends alphabetically")
print(f"Friends: {friends}")

# -------------------------------------------------------
# Louis had fight with Niko and want to remove from his friend list
# -------------------------------------------------------

unfriend = friends.pop(2)
print(f"Luois got unfriedn with {unfriend}")
print(f"Friends: {friends}")
