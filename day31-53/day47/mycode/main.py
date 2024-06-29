import requests
import lxml
import smtplib
from bs4 import BeautifulSoup

MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "mindthings.bnny@gmail.com"
MY_PASSWORD = "dctlnmjpkdssyfvk"

URL = "https://www.amazon.in/Apple-2022-10-9-inch-iPad-Wi-Fi/dp/B0BJMSFMHH/ref=sr_1_1_sspa?crid=6C2N03ICQLTR&dib=eyJ2IjoiMSJ9.iKOwXr2WsIw3vDGNmi5GTU-BEiPYYXPDdTqeOeb835hJQ1VfEWQag3ekAbTnKFVxVQLVQeIhDnqx7tJ2M5WwtCOjVRQ_F7czh7FBypDuDMoraCreAlVhshITOdcFkGiXsZqTjFasap_iDY5zEkU0M7eR1sYYmDmA2WCVa2wntzdQfF_YC4Zj65XXnH8t1wyQGPtL68_BtYyC-EWR9aElf3rmaA7op4YuSOzF1tzy1z8.F27nek2mCGbkXF2A3rmaXIHlU2LCwUbR0X0rmfcExFI&dib_tag=se&keywords=ipad+10th+generation&qid=1709960073&sprefix=ipad+%2Caps%2C230&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
headers = { 'Accept-Language' : "en-US,en;q=0.9,en-IN;q=0.8",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"}

resp = requests.get(url=URL, headers=headers)
# print(resp.text)
raw_html_page = resp.text

soup_page_html = BeautifulSoup(raw_html_page,"lxml")

print(soup_page_html.prettify())


price = soup_page_html.find(class_="a-price-whole").get_text()
price_as_float = float(price.replace(",", ""))
print(price_as_float)

title = soup_page_html.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 32000

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )

