import pandas as pd  # type: ignore

text = "Python is great. Python is easy to learn. Python is widely used."
word_to_count = "Python"

data = pd.Series(text.lower().split())

frequency = (data == word_to_count.lower()).sum()

print(f"The word '{word_to_count}' occurs {frequency} times.")
