# actions.py
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import random

class ActionProvideSupport(Action):

    def name(self):
        return "action_provide_support"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        messages = [
            "I'm always here for you.",
            "You’re not alone—I’m always here if you need someone to talk to.",
            "It’s okay to feel down sometimes. Let’s talk through it, step by step.",
            "I'm really glad you're talking to me. Want to share how you're feeling?",
            "It's hard when you feel lonely, but I want you to know you have my full attention.",
        ]
        response = random.choice(messages)
        dispatcher.utter_message(text=response)
        return []

class ActionCheerUp(Action):

    def name(self):
        return "action_cheer_up"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        messages = [
            "Let's find something to brighten your day. How about your favorite song?",
            "Talking can help! How about we focus on something positive together?",
            "You’re stronger than you think! Let’s find ways to feel better together.",
            "Remember, you’ve got me whenever you need. Let’s talk about what makes you happy."
        ]
        response = random.choice(messages)
        dispatcher.utter_message(text=response)
        return []

class ActionAskAboutDay(Action):

    def name(self):
        return "action_ask_about_day"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        dispatcher.utter_message(text="How was your day today? I’d love to hear about it.")
        return []

class ActionOfferHobbies(Action):

    def name(self):
        return "action_offer_hobbies"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        dispatcher.utter_message(text="Do you have any hobbies that help when you're feeling lonely? Maybe we can talk about those!")
        return []

class ActionExpressEmpathy(Action):

    def name(self):
        return "action_express_empathy"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        dispatcher.utter_message(text="That must be really tough. I can’t fully understand, but I’m here to listen.")
        return []
