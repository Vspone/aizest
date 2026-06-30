import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "SMTP Test - AI Zest"
msg["From"] = "admin@aizest.net"
msg["To"] = "admin@aizest.net"
msg.set_content("如果收到这封邮件，说明 Gmail SMTP 配置成功，可以正常用 admin@aizest.net 发信了。")

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as s:
        s.starttls()
        s.login("getcash070707@gmail.com", "nokgnfmtknlqciyt")
        s.send_message(msg)
    print("✅ 发送成功！去收件箱确认。")
except Exception as e:
    print(f"❌ 失败: {e}")
