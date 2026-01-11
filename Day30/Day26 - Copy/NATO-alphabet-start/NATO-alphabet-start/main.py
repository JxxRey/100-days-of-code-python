import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {
    row.letter: row.code for (index, row) in data.iterrows()
}


def generate_phonetic():
    word = input("Type your name: ").upper()
    try:
        the_list = [nato_dict[letter] for letter in word]
        print(the_list)
    except KeyError:
        print("Only letter entries allowed")
        generate_phonetic()

generate_phonetic()

