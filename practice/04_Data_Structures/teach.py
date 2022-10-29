"""

Set:
----
Louis has graduated from school and now wants to teach Zortans
how to talk in English. But English is complicated, so lets try
to simplify it using Sets.

Set is all about being `unique`, it's very useful for certain operations.

Info:
-----
In a Set all values are unique
"""

# ---------------------------------------------------------------------
# Louis wants to impress by showing some English magic, but Zortans are
# confused, they want him to first shows unique alphabets in his magic.
# ---------------------------------------------------------------------

magicWord: str = "abracadabra"
uniqueAlphabets: set[str] = set(magicWord)
print(f"My Unique Alphabets {uniqueAlphabets}")

sentence: str = "the big blue sky and the big blue ocean"
uniqueAlphabets = set(sentence)
print(f"\nMy Unique Alphabets {uniqueAlphabets}")

# what happens if we want to see unique list of words
wordList: list[str] = sentence.split()
print(f"Word List {wordList}")
uniqueWords: set[str] = set(wordList)
print(f"\nUnique Word {uniqueWords}")

# ---------------------------------------------------------------------
# Zortans are impressed and they want to add more words to the set
# ---------------------------------------------------------------------
uniqueWords.update(["big", "blue", "sky"])
print(f"\nUnique Word {uniqueWords}")  # Nothing is happening

uniqueWords.update(["green", "grass"])
print(f"\nUnique Updated Word {uniqueWords}")  # Something does happen

# ---------------------------------------------------------------------
# Zortans don't like the word grass and wants to remove it
# ---------------------------------------------------------------------

uniqueWords.remove("green")
print(f"\nUnique Updated Word {uniqueWords}")  # Geen removed from the list
