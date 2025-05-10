from typing import Any, Text, Dict, List

import json
import re

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

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
        dispatcher.utter_message(text="Here are the availabilities for next week :\n" + response)
        return []

class ActionParseTime(Action):
     def name(self)->Text:
          return "action_parse_time"
     def run(self,dispatcher : CollectingDispatcher,tracker: Tracker, domain: Dict[Text,any]) -> List[Dict[Text,any]]:
            time = tracker.get_slot("time")
            if not time:
                 dispatcher.utter_message(text="Sorry, I couldn't find the time information.")
                 return []
            day_pattern = r"\b\w{4,}\b"
            hour_pattern = r'\b([01]?\d|2[0-3])(:[0-5]\d)?\b'
            day = re.findall(day_pattern,time)
            hour_matches = re.findall(hour_pattern,time)
            hour = ["".join(match) for match in hour_matches]
            return [SlotSet("day",day[0]),SlotSet("hour",hour[0])]
     
class ActionCheckAvailability(Action):
    def name(self) -> Text:
        return "action_check_availability"
    def run(self,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],) -> List[Dict[Text, Any]]:
        with open("data/doctors.json") as json_data:
                data = json.load(json_data)
                json_data.close()
        doctor = tracker.get_slot("doctor")
        day = tracker.get_slot("day")
        hour = tracker.get_slot("hour")
        print(f"{doctor} | {day} | {hour}")
        return [SlotSet("appointement_availability",True)]