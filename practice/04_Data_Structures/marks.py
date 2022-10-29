"""

Dictionary:
-----------

Louis has given his exams and received marks. Let's check
out how did he fare.

Dictionary makes it easy to have key-value pairs.

Info:
-----
Lookups are very fast!!!
"""
from typing import Optional

marks: dict[str, int] = {
    "Math": 80,
    "Science": 82,
    "History": 78,
    "English": 35,
    "Python": 98,
    "Physics": 63,
}
print(f"Marks: {marks}\n")

# ---------------------------------------------------------------------
# Louis wants to check out all the subjects (Keys)
# ---------------------------------------------------------------------

for subject in marks.keys():
    print(subject)

# ---------------------------------------------------------------------
# Louis wants to check all the marks
# ---------------------------------------------------------------------
for score in marks.values():
    print(score)

# ---------------------------------------------------------------------
# Louis wants to check all the subject and marks
# ---------------------------------------------------------------------
for subject, score in marks.items():
    print(f"Subject: {subject}, Score: {score}")

# ---------------------------------------------------------------------
# Louis wants to check if he passed and passing marks is 50
# ---------------------------------------------------------------------
for subject, score in marks.items():
    if score >= 50:
        print(f"Subject: {subject}, Score: {score} PASSED!!")
    else:
        print(f"Subject: {subject}, Score: {score} FAILED!!")

# ----------------------------------------------------------------------
# Louis requests revaluation of his English paper, there was a totalling
# mistake and right marks are 70
# ----------------------------------------------------------------------
marks["English"] = 70
print(f"\nLouis scored {marks['English']} in English!!")

# ----------------------------------------------------------------------
# Louis also took Geography and scored 78
# ----------------------------------------------------------------------

marks["Geography"] = 78

# ---------------------------------------------------------------------
# Louis wants to check if he passed and passing marks is 50
# ---------------------------------------------------------------------
for subject, score in marks.items():
    if score >= 50:
        print(f"Subject: {subject}, Score: {score} PASSED!!")
    else:
        print(f"Subject: {subject}, Score: {score} FAILED!!")

# ----------------------------------------------------------------------
# Friends on Zortan want's to know how much Louis scored in Python
# ----------------------------------------------------------------------

# Alternative 1
# --------------
pythonScore: Optional[int] = marks["Python"]
print(f"Louis, scored {pythonScore} in Python")

# Alternative 2
# --------------
pythonScore = marks.get("Python")
print(f"Louis, scored {pythonScore} in Python")

# ----------------------------------------------------------------------
# Friends on Earth want's to know how much Louis scored in Java
# ----------------------------------------------------------------------
# Alternative 1 -- Will throw an error
# --------------
# javaScore = marks["Java"]
# print(f"Louis, scored {javaScore} in Java")

# Alternative 1
# --------------
javaScore = marks.get("Java")
print(f"Louis, scored {javaScore} in Java")

if javaScore is None:
    print("Louis didn't studied Java")
else:
    print(f"Louis scored {javaScore} in Java")

# ----------------------------------------------------------------------
# Deleting an element from Dictionary
# ----------------------------------------------------------------------
del marks["English"]
print(f"Marks: {marks}")
