# FileNotFound
'''
try:
    file = open("my_file.txt")
    a_dictionary = {'key': "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("my_file.txt", "w")
    file.write("Something")
except KeyError as error_answer:
    print(f"The key {error_answer} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    raise KeyError("This is an error that I made")
'''

###########    BMI      ###########

'''
height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
'''

#########     Coding challenge1     ######

'''
fruits = ["Apple", "Pear", "Orange"]


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        fruit = "Fruit"
    print(fruit + " pie")


make_pie(4)

'''

#########     Coding challenge2     ######

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3},
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        post['Likes'] = 0
        total_likes = total_likes + post['Likes']

print(total_likes)
