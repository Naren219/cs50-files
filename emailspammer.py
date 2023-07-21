import smtplib
import ssl

emailid = "betaspammer420@gmail.com"
password = "betaspammer69"
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
  server.login(emailid, password)
  for i in range(20):
    server.sendmail("villagecookingchannel@betaji.vela", "tcdixon3@students.wcpss.net", "a l i")
print("Sent email")