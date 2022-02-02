from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


class email:
    """ Email confirmation """

    def _send_confirmation_email(self, booking):
        """Send the user a confirmation email"""
        cust_email = booking.email
        subject = render_to_string(
            'complete/confirmation_emails/confirmation_email_subject.txt',
            {'booking': booking})
        body = render_to_string(
            'complete/confirmation_emails/confirmation_email_body.txt',
            {'booking': booking, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )
        self._send_confirmation_email(booking)
