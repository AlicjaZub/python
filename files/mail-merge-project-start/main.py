#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
with open('/Users/alicjazubel/Documents/python/files/mail-merge-project-start/Input/Letters/starting_letter.txt') as file:
  contents = file.read()
#   print(file.readlines())
  
with open('/Users/alicjazubel/Documents/python/files/mail-merge-project-start/Input/Names/invited_names.txt') as file:
  names = file.readlines()

for name in names:
    with open('/Users/alicjazubel/Documents/python/files/mail-merge-project-start/Input/Letters/starting_letter.txt') as file:
        contents = file.read()
        name = name.strip()
        text = contents.replace("[name]", name)
        new_letter = open(f"/Users/alicjazubel/Documents/python/files/mail-merge-project-start/Input/Letters/letter_to_{name}.txt", "w")
        new_letter.write(text)