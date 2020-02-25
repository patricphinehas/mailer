import smtplib
#Next, log in to the server
#Send the mail
s=smtplib.SMTP_SSL("smtp.gmail.com", 465)
s.ehlo()
# s.starttls()
s.login("$$$$$$$$$$$$$@gmail.com", "**********")

msg = """
Hello!" # The /n separates the message from the headers"""
s.sendmail("sender", "rcv", msg)