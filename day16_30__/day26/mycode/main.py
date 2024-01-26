import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data.to_dict())
data_dict = {row.letter: row.code for (index,row) in data.iterrows()}
print(data_dict)

inp = input("enter the word").upper()
output = [data_dict[letter] for letter in inp ]
print(output)
