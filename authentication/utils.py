from django.core.mail import EmailMessage
from django.core import mail
from django.core.mail import send_mail,EmailMultiAlternatives,send_mass_mail

import threading
from django.conf import settings


class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


class Util:
    @staticmethod
    def send_email(data):

        connection = mail.get_connection()
        connection.open()
        from_email="cessinideveloper@gmail.com"
        print(from_email)
        email = mail.EmailMessage(
            subject=data['email_subject'], body=data['email_body'],from_email=from_email,to=[data['to_email']],connection=connection)

        connection.send_messages([email])
        connection.close()
        '''
        email = EmailMessage(
            subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
        EmailThread(email).start()
        '''
        print("sent successfully")
