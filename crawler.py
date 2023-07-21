import requests
import time
import smtplib
import ssl
import schedule
import time
from bs4 import BeautifulSoup


isthere = 0
# Remember to format the name with caps as the first letters of each word
selected_school = "Research Triangle High School"

def isitthere():
  url = 'https://jordandriving.com/driver-education-fee-class-schedules-fee/'
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')
  request = soup.find("div", class_="entry-content")
  system = request.findAll("a", class_="a1")
  schools_file = open("schools.txt", 'a')
  for schools in system:
      schools_file.write(f"{schools.text}\n\n")
      schools_url = schools["href"]
      schools_response = requests.get(schools_url)
      schools_soup = BeautifulSoup(schools_response.content, 'html.parser')
      schools_list = schools_soup.find("div", class_="entry-content")
      for school in schools_list.findAll('a'):
          if "high" in school.text.lower() or "academy" in school.text.lower():
              if school.text == selected_school:
                  schools_file.write(f"{selected_school}\n\n")
                  isthere = 1
              else:
                  schools_file.write(f"{school.text}\n")
  schools_file.close()

  if isthere == 1:
    emailid = "nmanikandan219@gmail.com"
    password = "naren2007"
    with open("schools.txt", "r") as f:
      data = f.read()
    message = 'Subject: {}\n\n{}'.format("It\'s time for you to drive!", f"{selected_school} has an open slot for Jordan Driving school! Look at the list below. Your school name will have a space under it.\n{data}")
    context = ssl.create_default_context()
    print("Starting to send")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
      server.login(emailid, password)
      server.sendmail("donotreply@gmail.com", emailid, message)
    print("Sent email")
  else:
    file = open("schools.txt","r+")
    file.truncate(0)
    file.close()
schedule.every(25).seconds.do(isitthere)
# Choose when you want the program to be run each day. You can replace the .day with .what every day you want. This uses military time.
#schedule.every().day.at("7:00").do(isitthere)
while 1:
  if isthere == 0:
    schedule.run_pending()
    time.sleep(1)
  else:
    schedule.run_pending()
    time.sleep(1)
    break

