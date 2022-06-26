# import pandas
import datetime as dt
import smtplib
import random

my_email = "name1@gmail.com"
password = "password"
date = dt.datetime.now()
day = date.weekday()


if day == 3:
    with open("quotes.txt") as quotes:
        quote_list = quotes.readlines()
        monday_quote = random.choice(quote_list)
        # quote_list.remove(monday_quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="name2@yahoo.com",
            msg=f"Subject:Hello\n\n{monday_quote}"
        )

