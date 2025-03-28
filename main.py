#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


names = []
with open('Input/Names/invited_names.txt', "r") as name_file:
    for line in name_file.readlines():
        names.append(line.strip())

with open('Input/Letters/starting_letter.txt') as letter_file:
    starting_letter = letter_file.read()

for name in names:
    personalized_letter = starting_letter.replace("[name]", name)
    with open(f'Output/ReadyToSend/{name}_invite.txt', "w") as output_file:
        output_file.write(personalized_letter)

