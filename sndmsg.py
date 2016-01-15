from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC04bd29d8b3aa6e8066f73ffe1e488967"
auth_token  = "3453630140835a66d37276edc057e32b"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.sms.messages.create(
body="Parag! I love you <3",
    to="+17169395402",    # Replace with your phone number
    from_="+17166713060") # Replace with your Twilio number
print message.sid