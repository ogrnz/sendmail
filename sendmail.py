import os
import smtplib, ssl
import argparse

from dotenv import load_dotenv

load_dotenv()


def create_mail(sender, to, subj, content):
    msg = f"""\
From: From {FROM} <{FROM}>
To: To {TO} <{TO}>
MIME-Version: 1.0
Content-type: text/html
Subject: {SUBJ}

{content}"""

    return msg


def send_mail(content, PORT, SMTP, PWD):
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(SMTP, PORT, context=context) as server:
        server.login(FROM, PWD)
        server.sendmail(FROM, TO, content.encode("utf8"))

    print("Mail sent!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send plaintext emails.")

    parser.add_argument("-t", "--to", required=True, help="Receiver email address.")
    parser.add_argument("-s", "--subject", help="Subject of message.")
    parser.add_argument("-m", "--message", required=True, help="Message to send.")
    args = parser.parse_args()

    FROM = os.environ.get("FROM")
    TO = args.to if args.to else os.environ.get("TO")
    SUBJ = args.subject if args.subject else "Message from Pi"
    CONTENT = args.message
    email = create_mail(FROM, TO, SUBJ, CONTENT)

    print(email)

    PORT = os.environ.get("SSL_PORT")
    SMTP = os.environ.get("SMTP")
    PWD = os.environ.get("PWD")

    send_mail(email, PORT, SMTP, PWD)

    print(f"{PORT}")
    print(f"{SMTP}")
