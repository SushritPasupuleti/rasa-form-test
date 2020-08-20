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


class ActionSendOTP(Action):

    def name(self) -> Text:
        return "send_OTP"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("GENERATING OTP... \nSending OTP to: {}".format(tracker.get_slot("email")))
        dispatcher.utter_message(text="Hello World!")

        return []

class ActionVerifyOTP(Action):

    def name(self) -> Text:
        return "verify_OTP"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("Checking OTP {} of {}".format(tracker.get_slot("otp"), tracker.get_slot("email")))
        dispatcher.utter_message(text="Hello World!")

        authenticated = True

        return [SlotSet("authenticated", authenticated)]
