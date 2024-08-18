from .mailtrap_config import client, sender
from .emailTemplets import VERIFICATION_EMAIL_TEMPLATE, WELCOME_EMAIL_TEMPLATE, PASSWORD_RESET_REQUEST_TEMPLATE, PASSWORD_RESET_SUCCESS_TEMPLATE
from jinja2 import Template
import mailtrap as mt

def send_verification_email(email, verification_token):
    
    email_data = {
        "verificationCode": verification_token
    }
    # print("before rendering")
    
    jinja_template = Template(VERIFICATION_EMAIL_TEMPLATE)
    rendered_content = jinja_template.render(email_data)
    
    # print("after rendering")
    
    recipient = [email]
    
    # print(recipient)
    
    mail = mt.Mail(
        sender=sender,
        to=[mt.Address(email=email)],
        subject="Verify your email",
        html=rendered_content,
        category="Email Verification"
    )
    
    
    try:
        response = client.send(mail)
        
        print("Email sent successfully", response)
    except Exception as e:
        print("Error sending verification email", e)
        return False
    return True

def send_welcome_email(email, name):
    recipient = [email]
    
    # mail = mt.Mail(
    #     sender=sender,
    #     to=[mt.Address(email=email)],
    #     template_uuid="62a3e430-f655-4e14-b93b-995603852ade",
    #     template_variables={
    #         "company_info_name": "jo company",
    #         "name": name
    #     }
    # )
    
    try:
        email_data = {
            "company_info_name": "jo company",
            "name": name
        }
        
        
        jinja_template = Template(WELCOME_EMAIL_TEMPLATE)
        rendered_content = jinja_template.render(email_data)
        
        # Send email
        mail = mt.Mail(
            sender=sender,
            to=[mt.Address(email=email)],
            subject="Welcome to Our Service!",
            html=rendered_content
        )
        
        response = client.send(mail)
        # print("Email sent successfully", response)
    except Exception as e:
        print("Error sending welcome email", e)
        return False
    return True

def send_reset_password_email(email, resetURL):
    email_data = {
        "resetURL": resetURL
    }
    
    jinja_template = Template(PASSWORD_RESET_REQUEST_TEMPLATE)
    rendered_content = jinja_template.render(email_data)
    
    recipient = [email]
    
    mail = mt.Mail(
        sender=sender,
        to=[mt.Address(email=email)],
        subject="Password Reset Request",
        html=rendered_content,
        category="Password Reset"
    )
    
    try:
        response = client.send(mail)
        print("Email sent successfully", response)
    except Exception as e:
        print("Error sending password reset email", e)
        return False
    return True

def send_reset_success_email(email, name):
    email_data = {
        "name": name
    }
    
    jinja_template = Template(PASSWORD_RESET_SUCCESS_TEMPLATE)
    rendered_content = jinja_template.render(email_data)
    recipient = [email]
    
    mail = mt.Mail(
        sender=sender,
        to=[mt.Address(email=email)],
        subject="Password Reset Successful",
        html=rendered_content,
        category="Password Reset"
    )
    
    try:
        response = client.send(mail)
        print("Email sent successfully", response)
    except Exception as e:
        print("Error sending password reset email", e)
        return False
    return True
        


