from twilio import rest

#Input Account SID twilio.com/console
account_sid = "*************************"
#Input Authorization Token from twilio.com/console
auth_token  = "*************************"

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="+**************", #input Phone Number that is verified
    from_="+15162178388",
    body="You're a billionaire in the making. Your son loves you, and your future queen awaits you")

print(message.sid)
