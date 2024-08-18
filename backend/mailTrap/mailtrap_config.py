import mailtrap as mt
from dotenv import load_dotenv
import os
# import verificationCode.html as ver
from jinja2 import Template
from .emailTemplets import VERIFICATION_EMAIL_TEMPLATE

load_dotenv()

TOKEN = os.getenv("TOKEN")

email_data = {
    "verificationCode": 124456  # Make sure this key matches the placeholder in your template
}

jinja_template = Template(VERIFICATION_EMAIL_TEMPLATE)
rendered_content = jinja_template.render(email_data)

# sender=mt.Address(email="mailtrap@demomailtrap.com", name="youssef elmelegy")
sender=mt.Address(email="mailtrap@joopro.tech", name="youssef elmelegy")

# mail = mt.Mail(
#     sender=mt.Address(email="mailtrap@demomailtrap.com", name="Mailtrap Test"),
#     to=[mt.Address(email="youssefelmelegy999@gmail.com")],
#     subject="You are awesome!",
#     html=rendered_content ,
#     category="Integration Test",
# )

client = mt.MailtrapClient(token=TOKEN)
# client.send(mail)