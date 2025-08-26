import os
import time
import smtplib
import ssl
from email.message import EmailMessage

# ---------- CONFIGURATION ----------
FOLDER_TO_WATCH = os.path.dirname(os.path.abspath(__file__))   # auto: folder where codesync.py is placed
SENDER_EMAIL = "yourmail@gmail.com"                           # your Gmail
SENDER_PASSWORD = "your_app_password"                         # 16-digit Google App Password
RECEIVER_EMAIL = "yourmail@gmail.com"                         # where to receive
CHECK_INTERVAL = 2  # seconds
# ----------------------------------

def send_email_with_attachments():
    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = "CodeSync: Latest Python Files"

    msg.set_content("Attached are the latest versions of your .py files from this lab session.")

    # attach all .py files in folder
    for filename in os.listdir(FOLDER_TO_WATCH):
        if filename.endswith(".py"):
            filepath = os.path.join(FOLDER_TO_WATCH, filename)
            with open(filepath, "rb") as f:
                file_data = f.read()
            msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=filename)

    # send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)

    print("✅ Email sent with attachments!")

def main():
    print("🔍 Watching folder quietly... Press Ctrl+C when done to send email.")
    try:
        while True:
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print("\n⌛ Sending final email with all .py files...")
        send_email_with_attachments()
        print("📧 Done! Exiting.")

if __name__ == "__main__":
    main()

