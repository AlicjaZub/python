with open('files/my_file.txt') as file:
  contents = file.read()
  print(contents)
with open('files/my_file.txt', "a") as file:
  file.write("more text")
