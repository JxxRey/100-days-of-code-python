import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    def __init__(self):
        self.my_email = os.getenv("MY_EMAIL")
        self.my_password = os.getenv("MY_PASSWORD")  # Yahoo App Password

    def send_notification(self, message):
        with smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465) as smtp:
            smtp.set_debuglevel(1)
            smtp.ehlo()
            smtp.login(self.my_email, self.my_password)
            smtp.sendmail(
                self.my_email,
                self.my_email,
                f"Subject: Flight Deal Alert!\n\n{message}"
            )
