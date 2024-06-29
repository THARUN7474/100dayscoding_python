#Monday Motivation Project
import smtplib
import datetime as dt
import random

MY_EMAIL = "mindthings.bnny@gmail.com"
MY_PASSWORD = "dctlnmjpkdssyfvk"

now = dt.datetime.now()
print(now)
weekday = now.weekday()#here 0 1 2 3 4 5 6 are weekdays so monday is 0
if weekday == 6:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        print(all_quotes)
        print(type(all_quotes))
        # print(type(all_quotes))
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )



## Sending Email with Python
# import smtplib
#
# my_email = "appbreweryinfo@gmail.com"
# password = "abcd1234()"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:#smae as files here
#     connection.starttls()#protection added here
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="appbrewerytesting@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )
##or here connection.close()


## Working with date and time in Python
# import datetime as dt
#
# now = dt.datetime.now()
# print(now)
# print(type(now))
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)#to set date as our wish
# print(date_of_birth)#try type too
