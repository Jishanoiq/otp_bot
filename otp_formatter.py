# otp_formatter.py
from datetime import datetime

def format_otp_message(otp_data):
    now = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
    
    return f"""
✨ 𝐍𝐞𝐰 𝐎𝐓𝐏 𝐑𝐞𝐜𝐞𝐢𝐯𝐞𝐝 ✨
📞 𝐍𝐮𝐦𝐛𝐞𝐫: {otp_data['number']}
🔧 𝐒𝐞𝐫𝐯𝐢𝐜𝐞: {otp_data['service']}
⏰ 𝐓𝐢𝐦𝐞: {now}
🔑 𝐎𝐓𝐏 𝐂𝐨𝐝𝐞: {otp_data['code']}
📩 𝐅𝐮𝐥𝐥 𝐒𝐌𝐒: {otp_data['full_sms']}
🔗 [𝐌𝐀𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋]({otp_data.get('channel_link', 'https://t.me/otpbroadcast69')})
""".strip()
