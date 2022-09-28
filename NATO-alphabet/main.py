import pandas
import os

data = pandas.read_csv(f"{os.getcwd()}/NATO-alphabet/nato_phonetic_alphabet.csv")
codes = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Write a word: ").upper()

print([(codes[letter]) for letter in word])