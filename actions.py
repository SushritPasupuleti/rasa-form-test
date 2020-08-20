# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

import requests


class ActionSendOTP(Action):

    def name(self) -> Text:
        return "send_OTP"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("GENERATING OTP... \nSending OTP to: {}".format(
            tracker.get_slot("email")))

        email = tracker.get_slot("email")

        req = requests.post(url="http://localhost:6000/auth/generate-otp", json={
            'slot': {'EMAIL': email}
        })

        data = req.json()
        expiry_time = data["expiry"]

        print("Expiring in {}".format(expiry_time))

        dispatcher.utter_message(
            text="Sent an OTP to {}".format(tracker.get_slot("email")))

        return []


class ActionVerifyOTP(Action):

    def name(self) -> Text:
        return "verify_OTP"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("Checking OTP {} of {}".format(
            tracker.get_slot("otp"), tracker.get_slot("email")))

        email = tracker.get_slot("email")
        otp = tracker.get_slot("otp")

        req = requests.post(url="http://localhost:6000/auth/verify-otp", json={
            'slot': {'EMAIL': email, "OTP": otp}
        })

        data = req.json()
        authenticated = data["success"]

        print("Authenticated: {}".format(authenticated))

        if authenticated: dispatcher.utter_message(text="Authenticated")
        else: dispatcher.utter_message(text="Not Authenticated :(")

        return [SlotSet("authenticated", authenticated)]
