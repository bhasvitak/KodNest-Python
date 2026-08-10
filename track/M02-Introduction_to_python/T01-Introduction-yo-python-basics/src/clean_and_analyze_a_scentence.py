sentence = input()
position = int(input())

# Remove leading/trailing spaces and convert to lowercase
cleaned_text = sentence.strip().lower()

# Replace punctuation marks with spaces
for punctuation in ".,!?;:":
    cleaned_text = cleaned_text.replace(punctuation, " ")

# Split into words and rebuild the single-spaced sentence
words = cleaned_text.split()
cleaned_sentence = " ".join(words)

# Extract word count and specific words
count = len(words)
fw = words[0]
lw = words[-1]
wap = words[position - 1]

# Extract prefixes and suffixes
a = fw[:3]
b = lw[-3:]

# Display the complete analysis
print(f"Cleaned Sentence: {cleaned_sentence}")
print(f"Word Count: {count}")
print(f"First Word: {fw}")
print(f"Last Word: {lw}")
print(f"Selected Word: {wap}")
print(f"First Word Prefix: {a}")
print(f"Last Word Suffix: {b}")