from __future__ import annotations
import httpx
from .base import NotConfigured, AdapterError
from ..settings import settings
class TwilioVoiceAdapter:
    def create_callback(self, *, customer_number:str, twiml_url:str, status_callback:str):
        if not settings.twilio_account_sid or not settings.twilio_auth_token or not settings.twilio_from_number:
            raise NotConfigured("Twilio credentials/from number required")
        url=f"https://api.twilio.com/2010-04-01/Accounts/{settings.twilio_account_sid}/Calls.json"
        data={"To":customer_number,"From":settings.twilio_from_number,"Url":twiml_url,"StatusCallback":status_callback,"StatusCallbackEvent":["initiated","ringing","answered","completed"]}
        with httpx.Client(timeout=30,auth=(settings.twilio_account_sid,settings.twilio_auth_token)) as client: r=client.post(url,data=data)
        if r.status_code>=400: raise AdapterError(f"Twilio {r.status_code}: {r.text[:800]}")
        return r.json()
