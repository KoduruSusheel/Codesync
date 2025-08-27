# Codesync
A simple Python tool to auto-backup lab code. Monitors your folder, and on exit (Ctrl+C) sends all .py files to your Gmail as attachments using App Passwords. Saves time, prevents data loss, and ensures you always have the latest code safely stored.
CodeSync – Automatic Python Lab Backup Tool


📌 Problem

In our lab sessions, we often get only limited time (e.g., 3 hours) to write and complete assignments.
Since the lab systems reset or we need to continue coding later in the hostel, many students email themselves partial code.

The problem:

Sending code manually takes extra time.
Sometimes students forget to back up their progress.
We needed a simple tool to automatically back up code safely without distractions.

💡 Solution

CodeSync is a Python script that automatically monitors your working folder.

.While you are coding in the lab, it silently watches all .py files.
.When you finish and stop the script (Ctrl + C), it collects all .py files in that folder and emails them to you as attachments.
.This ensures you always have the latest versions backed up in your email.

One-time Setup:
.Generate a Google App Password (since Gmail requires this for security).
.Go to Google Account Security
.Enable 2-Step Verification.
.Create an App Password for "Mail" → "Device: Other (CodeSync)".
.Copy the 16-character password.
.Save this script as codesync.py in your coding folder.

Update these lines with your details:

sender_email = "your_email@gmail.com"
receiver_email = "your_email@gmail.com"
app_password = "your_16_digit_app_password"

▶️ How to Run
.Open your lab folder (where you want to code).
.Place codesync.py inside that folder.
.Run it in terminal:
    python codesync.py
.Start coding as usual.
.When you’re done, stop with Ctrl + C.
.An email will be sent with all your .py files attached.


This project was built to solve a real lab problem with the help of AI.


