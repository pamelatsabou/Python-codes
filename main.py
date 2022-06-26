##################### Normal Starting Project ######################
import datetime as dt
import random
import pandas
import smtplib

# 2. Check if today matches a birthday in the birthdays.csv
today_month = dt.datetime.now().month
today_day = dt.datetime.now().day
today = (today_month, today_day)

# HINT 2: Use pandas to read the birthdays.csv
birthday = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthday.iterrows()}

# HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:

if (today_month, today_day) in birthdays_dict:
    letter_list = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
    file = random.choice(letter_list)
    birthday_person = birthdays_dict[today]
    with open(file) as letter_file:
        letter = letter_file.read()
        contents = letter.replace("[NAME]", birthday_person["name"])
# 4. Send the letter generated in step 3 to that person's email address.
my_email = "name1"
password = "password"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(my_email, password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=birthday_person["email"],
        msg=f"Subject:Happy Birthday!\n\n{contents}"
    )


