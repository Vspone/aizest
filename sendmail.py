#!/usr/bin/env python3
"""Send email as admin@aizest.net via Gmail SMTP"""
import smtplib, sys
from email.message import EmailMessage

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
GMAIL_USER = "getcash070707@gmail.com"
GMAIL_PASS = "nokgnfmtknlqciyt"

def send_email(to, subject, body):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = "admin@aizest.net"
    msg["To"] = to
    msg.set_content(body)
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as s:
        s.starttls()
        s.login(GMAIL_USER, GMAIL_PASS)
        s.send_message(msg)
    print(f"✅ Sent to {to}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 sendmail.py <to> <subject> <body>")
        sys.exit(1)
    send_email(sys.argv[1], sys.argv[2], sys.argv[3])
