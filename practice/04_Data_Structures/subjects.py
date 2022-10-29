"""

Tuple:
------
Time for Louis to go to school, and its time for him to
choose subjects. School doesn't want students to change
subjects after they are chosen, so they use Tuple.

Tuple is like a stricter brother of List. Once a Tuple is
created, it cannot be edited.

Info:
-----
Tuple also start from index 0
"""
subjects: tuple[str, str, str] = ("Math", "Science", "History")

# ---------------------------------------------------------------------
# Louis wants to count his subjects
# ---------------------------------------------------------------------
print(f"\nNo of Subjects {len(subjects)}")


# ---------------------------------------------------------------------
# Louis wants to know all the subjects name
# ---------------------------------------------------------------------
print(f"\nAvailalbe subjects are {subjects}")
for subject in subjects:
    print(subject)

# ---------------------------------------------------------------------
# Louis wants to know his second subject name
# ---------------------------------------------------------------------
print(f"\nSecond subject is: {subjects[1]}")

# ---------------------------------------------------------------------
# School wants Louis to take another 3 subject to get gull credits
# ---------------------------------------------------------------------
additionalSubjects: tuple[str, str, str] = ("English", "Python", "Physics")
allSubjects = subjects + additionalSubjects
print(f"\nAll Subjects: {allSubjects}")
