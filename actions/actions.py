# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa-pro/concepts/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

import json

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionShowAvailability(Action):
    def name(self)->Text:
        return "action_show_availability"
    def run(self,dispatcher : CollectingDispatcher,tracker: Tracker, domain: Dict[Text,any]) -> List[Dict[Text,any]]:
        with open("data/doctors.json") as json_data:
                data = json.load(json_data)
                json_data.close()
        response = ""
        for doctor in data :
            response += f"{doctor['name']} is available :\n"
            for day in doctor['availability']:
                response += f"{day['day']} between {day['time'].split('-')[0]} and {day['time'].split('-')[1]}\n"
        dispatcher.utter_message(text="Here are the availabilities for next week :\n " + response)
        return []

#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
