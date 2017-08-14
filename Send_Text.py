from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "ACb4d8799630dfc11f5a563d63859266ef"
# Your Auth Token from twilio.com/console
auth_token  = "de0458fd8c68724fa405d5af20e1da4a"

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="+13479032631", 
    from_="+15162178388",
    body="You're a billionaire in the making. Your son loves you, and your future queen awaits you")

print(message.sid)
