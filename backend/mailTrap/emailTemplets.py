VERIFICATION_EMAIL_TEMPLATE ="""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Verify Your Email</title>
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; padding: 20px;">
  <div style="background: linear-gradient(to right, #4CAF50, #45a049); padding: 20px; text-align: center;">
    <h1 style="color: white; margin: 0;">Verify Your Email</h1>
  </div>
  <div style="background-color: #f9f9f9; padding: 20px; border-radius: 0 0 5px 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
    <p>Hello,</p>
    <p>Thank you for signing up! Your verification code is:</p>
    <div style="text-align: center; margin: 30px 0;">
      <span style="font-size: 32px; font-weight: bold; letter-spacing: 5px; color: #4CAF50;">{{verificationCode}}</span>
    </div>
    <p>Enter this code on the verification page to complete your registration.</p>
    <p>This code will expire in 15 minutes for security reasons.</p>
    <p>If you didn't create an account with us, please ignore this email.</p>
    <p>Best regards,<br>Your App Team</p>
  </div>
  <div style="text-align: center; margin-top: 20px; color: #888; font-size: 0.8em;">
    <p>This is an automated message, please do not reply to this email.</p>
  </div>
</body>
</html>
"""

WELCOME_EMAIL_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome Email</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 80%;
            margin: 0 auto;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .header img {
            width: 100%;
            height: auto;
            border-radius: 8px;
        }
        .main-img {
          /*width: 80%;*/
          display: flex;
          /*align-items: center;*/
          /*justify-content: center;*/
        }
        .main-img img{
          width: 80%;
          margin: 3% 10%;
        }
        .main-h3 {
          font-size: 10px;
          /*font-we: 100;*/
          text-align: center;
          margin-bottom: 20px;
        }
        .welcome-text {
            /*text-align: center;*/
            margin: 20px 0;
        }
        .welcome-text h1 {
            /*text-align: center;*/
            font-size: 24px;
            color: #333333;
            margin-bottom: 50px;
        }
        .next-step {
            text-align: center;
            margin: 30px 0;
        }
        
        .next-step a {
            display: inline-block;
            padding: 10px 90px;
            font-size: 16px;
            color: #ffffff;
            background-color: #007bff;
            text-decoration: none;
            border-radius: 5px;
        }
        .resources {
            justify-content: center;
            text-align: center;
            margin: 20px 0;
        }
        .resources a {
          display: flex;
        }
        .resources img {
            width: 140px;
            height: auto;
            border-radius: 5px;
            margin: 10px;
        }
        .footer {
            text-align: center;
            margin-top: 20px;
            padding: 10px;
            border-top: 1px solid #cccccc;
        }
        .footer a {
            display: inline-block;
            padding: 10px 20px;
            font-size: 16px;
            color: #ffffff;
            background-color: #dc3545;
            text-decoration: none;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <!--<div class="header">-->
        <!--    <img src="your-company-logo-url" alt="Company Logo">-->
        <!--</div>-->
        <div class="main-h3">
          <h3>{{company_info_name}}</h3>
        </div>
        <div class="main-img">
        <img src="https://53.fs1.hubspotusercontent-na1.net/hub/53/hubfs/36_Welcome%20Email%20Templates.jpg?width=595&height=400&name=36_Welcome%20Email%20Templates.jpg" />
        </div>
        <div class="welcome-text">
            <h1>Welcome, {{name}}!</h1>
            <p>Thanks for choosing {{company_info_name}}! We are happy to see you on board.</p>
        </div>
        <div class="next-step">
            <a href="your-next-step-link">Next Step</a>
        </div>
        <div class="resources">
            <a href="your-get-started-guide-link">
                <img src="https://og-cio.vercel.app/api/og/Quick%20start%20guide?theme=dark&image=get-started" alt="Get Started Guide">
                <p>Get Started Guide</p>
            </a>
            <a href="your-onboarding-video-link">
                <img src="https://q5n8c8q9.rocketcdn.me/wp-content/uploads/2020/02/Ultimate-Guide-Onboarding-Users-with-Video.png" alt="Onboarding Video">
                <p>Onboarding Video</p>
            </a>
        </div>
        <div class="footer">
            <a href="your-unsubscribe-link">Unsubscribe</a>
        </div>
    </div>
</body>
</html>
"""

PASSWORD_RESET_REQUEST_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Reset Your Password</title>
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; padding: 20px;">
  <div style="background: linear-gradient(to right, #4CAF50, #45a049); padding: 20px; text-align: center;">
    <h1 style="color: white; margin: 0;">Password Reset</h1>
  </div>
  <div style="background-color: #f9f9f9; padding: 20px; border-radius: 0 0 5px 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
    <p>Hello,</p>
    <p>We received a request to reset your password. If you didn't make this request, please ignore this email.</p>
    <p>To reset your password, click the button below:</p>
    <div style="text-align: center; margin: 30px 0;">
      <a href="{{resetURL}}" style="background-color: #4CAF50; color: white; padding: 12px 20px; text-decoration: none; border-radius: 5px; font-weight: bold;">Reset Password</a>
    </div>
    <p>This link will expire in 1 hour for security reasons.</p>
    <p>Best regards,<br>Your App Team</p>
  </div>
  <div style="text-align: center; margin-top: 20px; color: #888; font-size: 0.8em;">
    <p>This is an automated message, please do not reply to this email.</p>
  </div>
</body>
</html>
"""

PASSWORD_RESET_SUCCESS_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Password Reset Successful</title>
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; padding: 20px;">
  <div style="background: linear-gradient(to right, #4CAF50, #45a049); padding: 20px; text-align: center;">
    <h1 style="color: white; margin: 0;">Password Reset Successful</h1>
  </div>
  <div style="background-color: #f9f9f9; padding: 20px; border-radius: 0 0 5px 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
    <p>Hello, {{name}}</p>
    <p>We're writing to confirm that your password has been successfully reset.</p>
    <div style="text-align: center; margin: 30px 0;">
      <div style="background-color: #4CAF50; color: white; width: 50px; height: 50px; line-height: 50px; border-radius: 50%; display: inline-block; font-size: 30px;">
        ✓
      </div>
    </div>
    <p>If you did not initiate this password reset, please contact our support team immediately.</p>
    <p>For security reasons, we recommend that you:</p>
    <ul>
      <li>Use a strong, unique password</li>
      <li>Enable two-factor authentication if available</li>
      <li>Avoid using the same password across multiple sites</li>
    </ul>
    <p>Thank you for helping us keep your account secure.</p>
    <p>Best regards,<br>Your App Team</p>
  </div>
  <div style="text-align: center; margin-top: 20px; color: #888; font-size: 0.8em;">
    <p>This is an automated message, please do not reply to this email.</p>
  </div>
</body>
</html>
"""


