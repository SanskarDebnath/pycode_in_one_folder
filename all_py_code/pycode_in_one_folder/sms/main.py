from twilio.rest import Client
import keys

Client = Client(keys.account_sid, keys.auth_token)

message = Client.messages.create(
    body = "#main message body",
    from_= keys.twilio_number,
    to=keys.target_number
)

print(message.body)

#it will send the message in this registerd twilio account (phone number)
#i will add a screenshot for a clear perspective view
