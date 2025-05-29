import re

# Input string
text = ("You didn't meet me today that's why I am sad. It seem like you don't care anymore because you showed less attention to me, "
        "thus,  I feel like nobody loves me anymore. You gave me lots of heartaches and problems, therefore, I hate you so much.")

print("TEXT TO ANALYZE:\n")
print(text)
print("\n--- Pattern Search Tool ---")
print("====================================")
# Ask the user for a pattern or group of patterns (comma-separated)
user_input = input("Enter word or group of words to search (comma-separated):\n> ")

# Convert to list of patterns
patterns = [pattern.strip() for pattern in user_input.split(',') if pattern.strip()]

# Search each pattern
print("\nSearch Results:")
match_count = 0

for pattern in patterns:
    regex = re.escape(pattern)
    matches = re.findall(regex, text, re.IGNORECASE)
    if matches:
        print(f"Pattern found: \"{pattern}\"")
        for match in matches:
            print(f" - Match: {match}")
        match_count += len(matches)
    else:
        print(f"Pattern not found: \"{pattern}\"")
print("==================================")
# Sentiment score and message
print("\nOverall Negative Emotion Level:", match_count)

#print names for group
def team_group():
    print("")
    print("Group :")
    print("Pecious Grace Bagaforo")
    print("Japhet V. Esco")
    print("Glenn Franco")

if match_count >= 5:
    print("Precaution: High negative emotion detected. Consider taking supportive action.")
    team_group()
elif match_count >= 2:
    print("Note: Some negative sentiment detected.")
    team_group()
else:
    print("Sentiment is generally positive, neutral, or not listed.")
    team_group()