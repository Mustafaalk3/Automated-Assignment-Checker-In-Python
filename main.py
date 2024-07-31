import requests
import smtplib


SHEETY_API_URL = 'https://api.sheety.co/ec1fa9b9e4254e67050e9bdb5e5d6fe1/advancePythonAssignment/sheet1'
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
GMAIL_USER = "www.alkmustafa05@gmail.com"
GMAIL_PASSWORD = "vckv uxku lllu lkha"


response = requests.get(SHEETY_API_URL)
data = response.json()

def send_email(to_address, subject, message):
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(GMAIL_USER, GMAIL_PASSWORD)
            email_message = f"Subject: {subject}\n\n{message}"
            server.sendmail(GMAIL_USER, to_address, email_message)
        print(f"Successfully sent email to {to_address}")
    except Exception as e:
        print(f"Failed to send email to {to_address}: {e}")

# Process each homework submission
homework_submissions = data['sheet1']
for submission in homework_submissions:
    name = submission.get('name')
    email = submission.get('email')
    assignment_title = submission.get('assignmentTitle')
    submission_status = submission.get('submissionStatus')
    grade = submission.get('grade', 0)
    min_marks = submission.get('minimumMarks', 0)
    max_marks = submission.get('maxMarks', 0)

    if grade > min_marks:
        subject = f"Submission Confirmation for {assignment_title}"
        message = (f"Assalam-U-Alaikum {name},\n\n"
                   f"Your submission for {assignment_title} on {submission_status} "
                   f"has been recorded with a grade of {grade}.\n\n"
                   f"Best regards,\nYour Teacher")
        send_email(email, subject, message)

    elif grade < min_marks:
        subject = f"You are failing in {assignment_title} Assignment"
        message = (f"Assalam-U-Alaikum {name},\n\n"
                   f"Your grade of {grade} in {assignment_title} is below the minimum required marks of {min_marks}. "
                   f"Please take necessary actions to improve your performance.\n\n"
                   f"Best regards,\nYour Teacher")
        send_email(email, subject, message)

    else:
        subject = f"Reminder: Submit your {assignment_title}"
        message = (f"Assalam-U-Alaikum {name},\n\n"
                   f"This is a reminder to submit your {assignment_title}.\n\n"
                   f"Best regards,\nYour Teacher")
        send_email(email, subject, message)
