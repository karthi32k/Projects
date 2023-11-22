import pandas

# TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic = {row.letter: row.code for (index, row) in data.iterrows()}
#print(nato_phonetic)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic():
    word = input("Enter the word:").upper()
    # Using exceptional handling
    try:
        output_list = [nato_phonetic[letter] for letter in word]
    except KeyError:
        print("Sorry, Only letters in the Alphabet please enter the string")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
