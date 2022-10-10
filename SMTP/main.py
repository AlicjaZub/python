import smtplib
import datetime as dt

my_email = "test@gmail.com"
password = "password"

with smtplib.SMTP("smtp.gmail.com")as connection:
  connection.starttls()
  connection.login(user=my_email, password=password)
  # lower the security in mail settings
  connection.sendmail(from_addr=my_email, to_addrs="alicja@madebyon.com", msg="Subject:Hello\n\nThis is the body")
  connection.close()


now = dt.datetime.now()
weekday = now.weekday()
