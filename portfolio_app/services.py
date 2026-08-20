import logging

import sendgrid
from decouple import config
from django.template.loader import render_to_string
from django.utils import timezone
from sendgrid.helpers.mail import Email, Mail

logger = logging.getLogger(__name__)


def send_new_contact_email(contact):
    html_content = render_to_string(
        "email/contact-new.html",
        {
            "name": contact.name,
            "email": contact.email,
            "message": contact.message,
            "current_year": timezone.now().year,
            "website_url": config("FE_APP_URL"),
        },
    )

    mail = Mail(
        from_email=Email(config("SENDGRID_FROM_EMAIL")),
        to_emails=config("CONTACT_EMAIL"),
        subject="Portfolio - New Message",
        html_content=html_content,
    )

    try:
        client = sendgrid.SendGridAPIClient(config("SENDGRID_API_KEY"))
        client.send(mail)
    except Exception:
        logger.exception("Failed to send new contact email")
