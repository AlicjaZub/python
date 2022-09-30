import pandas
import os

data = pandas.read_csv(f"{os.getcwd()}/NATO-alphabet/nato_phonetic_alphabet.csv")
codes = {row.letter: row.code for (index, row) in data.iterrows()}

def generate_phonetic():
  word = input("Write a word: ").upper()
  try:
    print([(codes[letter]) for letter in word])
  except KeyError:
    print("Please enter a valid word with letters from english alphabet")
    generate_phonetic()
      
generate_phonetic()