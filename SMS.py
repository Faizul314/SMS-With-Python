from twilio.rest import Client

account_sid = 'AC32e5f9b50d32266d4268f5ddf16da469'
auth_token = '.......' #copy and paste your AUTH TOKEN....
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+12014821933',
    body='I CANT BELIEVE THIS WORKS',
    to='........' #add verified TWILIO NUMBER....
)

print(message.sid)