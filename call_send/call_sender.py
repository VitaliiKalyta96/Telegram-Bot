from twilio.rest import Client

account_sid = ''
auth_token = ''

client = Client(account_sid, auth_token)

# https://www.twilio.com/

''' Change the value of 'from' with the number 
received from Twilio and the value of 'to'
with the number in which you want to send message.'''
message = client.messages.create(
  body = 'Hello everybody!',
  from_='+380___',
  to='+380___'
)


if __name__ == '__main__':
    print(message.sid)
