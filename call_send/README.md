About application.

This service allow you send message with neccessary text in number phone.

Settings:

1. Create account in host https://www.twilio.com/.
2. Copy account_sid and auth_token and put in file call_sender.py .
3. Generate free number for receive send message and put in row `from_`
4. Authenticate number in your account on such will be send a message and put in row `to`.
5. Create virtual environment in your terminal command: `python3 -m venv venv`.
6. Activate : `source venv/bin/activate`.
7. Run file call_sender.py .