import pandas as pd
import re

# Function to extract verses and commentaries
def extract_verses_and_commentaries(file_path):
    verses = []
    commentaries = []
    current_verse = None
    current_commentary = []
    is_verse = False

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            line = lines[i].rstrip()            
            # Check if the line is the start of a verse
            if line.endswith(' |'):
                # Start a new verse
                current_verse = line
                is_verse = True                
            elif is_verse and line.endswith('||'):
                # Append the second line of the verse
                current_verse += ' ' + line
                is_verse = False                                
            elif current_verse:
                # Add non-empty lines to commentary                
                if line == '--*--' or line == ' o)0(o':                    
                    # If there's a current verse, save it with its commentary
                    if current_verse and current_commentary:
                        print("Current verse:", current_verse)
                        print("Current commentary:", current_commentary)
                        verses.append(current_verse)  # Append the current verse
                        commentaries.append(' '.join(current_commentary))
                    # Reset for the next verse
                    current_verse = None
                    current_commentary = []
                elif line:
                    current_commentary.append(line)
            i += 1

    # Add the last verse and commentary if they exist
    if current_verse and current_commentary:
        verses.append(current_verse)
        commentaries.append(' '.join(current_commentary))

    return verses, commentaries

# Extract data
file_path = 'gita-ramanuja.txt'
verses, commentaries = extract_verses_and_commentaries(file_path)

# Filter verses and commentaries to keep only those with the pattern ||[0-9]+||
pattern = re.compile(r'\|\|\d+\|\|')
filtered_verses = []
filtered_commentaries = []

for verse, commentary in zip(verses, commentaries):
    if pattern.search(verse):
        filtered_verses.append(verse)
        filtered_commentaries.append(commentary)

# Create a DataFrame with filtered data
df = pd.DataFrame({
    'verse': filtered_verses,
    'commentary': filtered_commentaries
})

# Convert the 'commentary' column to strings to avoid AttributeError
df['commentary'] = df['commentary'].astype(str)

# Filter out entries without commentary
df = df[df['commentary'].str.strip() != '']

# Posthoc check for pattern ||[0-9]+|| in verses
pattern = re.compile(r'\|\|\d+\|\|')
for verse in verses:
    if pattern.search(verse):
        print(f"Pattern found in verse: {verse}")

# Write to JSON with pretty print
df.to_json('gita-ramanuja_verses_with_commentary.json', orient='records', lines=True, force_ascii=False, indent=4)

print("Extraction and JSON writing complete.")
