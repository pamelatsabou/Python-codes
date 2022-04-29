SPACEHOLDER = "[name]"

with open("/home/pamela/Documents/Python projects/Day 24/7.4 mail-merge-project-start/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("/home/pamela/Documents/Python projects/Day 24/7.4 mail-merge-project-start/Input/Letters/starting_letter.docx") as letter_file:
    each_letter = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        letter = each_letter.replace(SPACEHOLDER, stripped_name)
        print(letter)
        with open(f"/home/pamela/Documents/Python projects/Day 24/7.4 mail-merge-project-start/Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as completed_letter:
            completed_letter.write(letter)
