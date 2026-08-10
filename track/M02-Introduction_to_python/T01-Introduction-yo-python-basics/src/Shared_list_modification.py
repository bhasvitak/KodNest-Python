# Read three original scores into a list
original_scores = []
for _ in range(3):
    original_scores.append(int(input()))

# Create an alias pointing to the same list object
alias_scores = original_scores

# Read replacement score and additional score
replacement_score = int(input())
additional_score = int(input())

# Modify the shared list through alias_scores
alias_scores[0] = replacement_score
alias_scores.append(additional_score)

# Display both variables and check whether they share the same object
print(f"Original: {original_scores}")
print(f"Alias: {alias_scores}")
print(f"Shared Object: {original_scores is alias_scores}")