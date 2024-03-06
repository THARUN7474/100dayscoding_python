import datetime as dt
import pandas
import smtplib
import random

MY_EMAIL = "mindthings.bnny@gmail.com"
MY_PASSWORD = "dctlnmjpkdssyfvk"

today = dt.datetime.now()
# print(today.weekday())
tdate = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
# print(data)  # heere we can cnovert to dict and use only req things by using orient = records
birthdays_dict = {(data_row["month"], data_row.day): data_row for (index, data_row) in data.iterrows()}
# print(birthdays_dict)
if tdate in birthdays_dict:
    birthday_person = birthdays_dict[tdate]
    # to choose lertter other way is to writing all file pass in a list and choosing one randomly
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("SMTP.GMAIL.COM") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"SUBJECT:HAPPY BIRTHDAY WISHES\n\n{contents}")
        