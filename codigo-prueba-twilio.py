from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_=os.getenv('TWILIO_FROM_'),
  body='Han hecho una solicitud de Helado',
  to=os.getenv('TWILIO_TO')
)

print(message.sid)

