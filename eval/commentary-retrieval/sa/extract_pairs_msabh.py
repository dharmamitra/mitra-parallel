import pandas as pd
import re

# Function to extract verses and commentaries
def extract_verses_and_commentaries(file_path):
    verses = []
    commentaries = []
    current_verse = None
    current_commentary = []

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            # Check if the line is a verse
            if line.endswith('|') and i + 1 < len(lines) and re.search(r'\|\| amsa_[^ ]+ \|\|', lines[i + 1]):
                # If there's a current verse, save it with its commentary
                if current_verse and current_commentary:
                    verses.append(current_verse)  # Append the current verse
                    commentaries.append(' '.join(current_commentary))
                
                # Start a new verse
                current_verse = line + ' ' + lines[i + 1].strip()  # Append the amsa part to the verse
                current_commentary = []
                i += 1  # Skip the amsa line in the next iteration
            elif current_verse:
                # Check if the line is not an amsa line before adding to commentary
                if not re.search(r'\|\| amsa_[^ ]+ \|\|', line):
                    current_commentary.append(line)
            i += 1

    # Add the last verse and commentary if they exist
    if current_verse and current_commentary:
        verses.append(current_verse)
        commentaries.append(' '.join(current_commentary))

    # Post-hoc check to filter verses
    valid_verses = []
    valid_commentaries = []
    pattern = re.compile(r'^[^|]+ \| [^|]+ \|\| amsa_[^ ]+ \|\|$')
    for verse, commentary in zip(verses, commentaries):
        if pattern.match(verse):
            valid_verses.append(verse)
            valid_commentaries.append(commentary)

    return valid_verses, valid_commentaries

# Extract data
file_path = 'msabh.txt'
verses, commentaries = extract_verses_and_commentaries(file_path)

# Create a DataFrame
df = pd.DataFrame({
    'verse': verses,
    'commentary': commentaries
})

# Filter out entries without commentary
df = df[df['commentary'].str.strip() != '']

# Write to JSON with pretty print
df.to_json('msabh_verses_with_commentary.json', orient='records', lines=True, force_ascii=False, indent=4)

print("Extraction and JSON writing complete.")
