from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
  result = ''

  if direction == 'decode':
      shift *= -1
  elif direction != 'encode':
    return print("Wrong directions")

  letters = [t for t in text]
  for l in letters:
    if l not in alphabet:
      result += l
      continue
    index = alphabet.index(l)

    position = index + shift

    if position >= 26:
      position = position % 26
    result += alphabet[position]
  
  print(f"\nYour {direction}d word is {result}\n")

should_end = False

while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(text, shift, direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
  if restart != "yes":
    should_end = True
    print("Goodbye")
    