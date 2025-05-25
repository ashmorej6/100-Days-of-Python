import pandas

# Load the NATO phonetic alphabet CSV file and convert it into a dictionary
# Format: {"A": "Alfa", "B": "Bravo", ...}
alpha_df = pandas.read_csv("nato_phonetic_alphabet.csv")
dictionary = {row.letter:row.code for (index, row) in alpha_df.iterrows()}
print(dictionary)

# Prompt user for their name and convert it to uppercase
user_input = input("What's your name?: ").upper()

# Convert each letter in the user's name to its corresponding NATO code
phon_list = [dictionary[letter] for letter in user_input]

# Display the list of phonetic codes
print(phon_list)