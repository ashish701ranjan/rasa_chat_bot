from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.events import FollowupAction
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.events import Restarted
import zomatopy
import json
import constants
import utils

user_key = "c5023762c45f2b31128e8374fce8aba5"

restaurants_in_price_range = []

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key": user_key}
		zomato = zomatopy.initialize_app(config)
		loc_res = utils.get_location(zomato, tracker)

		print(loc_res)

		if loc_res['error']:
			dispatcher.utter_message("----- " + loc_res['error'])
			# SlotSet('location', loc_res['name'])
			return [SlotSet('location', loc_res['name']), FollowupAction('action_search_restaurants')]
		lat, lon = loc_res['loc']

		cuisine_search = utils.get_cuisine_id(zomato, tracker)
		cuisine_id = cuisine_search['id']
		if cuisine_search['error']:
			dispatcher.utter_message("----- " + cuisine_search['error'])
			# SlotSet('cuisine', cuisine_id)
			return [SlotSet('cuisine', cuisine_id), FollowupAction('action_search_restaurants')]

		results = zomato.restaurant_search("", lat, lon, cuisine_id, 20)
		d = json.loads(results)

		response = ""
		if d['results_found'] == 0:
			response= "no results"
		else:
			global restaurants_in_price_range
			restaurants_in_price_range = utils.filterByPrice(d['restaurants'], tracker.get_slot('price'))
			if len(restaurants_in_price_range) == 0:
				dispatcher.utter_message(" Sorry, No restaurants found in this price range. Please select some other budget")
				# dispatcher.utter_template('utter_price_range', tracker)
				return [SlotSet('price', None), FollowupAction('utter_price_range')]
			else:
				i = 0
				while i < len(restaurants_in_price_range):
					restaurant = restaurants_in_price_range[i]
					name = restaurant['restaurant']['name']
					address = restaurant['restaurant']['location']['address']
					rating = restaurant['restaurant']['user_rating']['aggregate_rating']
					response = response + "{} in {} has been rated {}\n".format(name, address, rating)
					i = i + 1
					if i >= 5:
						break
		
		dispatcher.utter_message(response)
		return [SlotSet('location', loc_res['name'])]


class ActionSearchLocation(Action):
	def name(self):
		return 'action_search_location'

	def run(self, dispatcher, tracker, domain):
		config={ "user_key": user_key}
		zomato = zomatopy.initialize_app(config)
		loc_res = utils.get_location(zomato, tracker)
		if loc_res['error']:
			dispatcher.utter_message("----- " + loc_res['error'])
			return [SlotSet('location', loc_res['name'])]
		if not tracker.get_slot('cuisine'):
			dispatcher.utter_template("utter_ask_cuisine", tracker)
		return [SlotSet('location', loc_res['name'])]

class ActionSearchCuisine(Action):
	def name(self):
		return 'action_search_cuisine'
	
	def run(self, dispatcher, tracker, domain):
		config={ "user_key": user_key}
		zomato = zomatopy.initialize_app(config)
		cuisine_search = utils.get_cuisine_id(zomato, tracker)
		if cuisine_search['error']:
			dispatcher.utter_message("----- " + cuisine_search['error'])
		if not tracker.get_slot('location'):
			dispatcher.utter_template("utter_ask_location", tracker)
		return [SlotSet('cuisine', cuisine_search['id'])]


class ActionSendEmail(Action):
	def name(self):
		return 'action_send_email'
	
	def run(self, dispatcher, tracker, domain):
		config={ "user_key": user_key}
		zomato = zomatopy.initialize_app(config)
		email = tracker.get_slot('email')
		if (not email):
			dispatcher.utter_template("utter_goodbye", tracker)
			return [AllSlotsReset(), FollowupAction('action_restart_my_conv')]

		global restaurants_in_price_range
		utils.send_mail(email, restaurants_in_price_range, tracker)
		dispatcher.utter_message('Thank you, We will be sending you the email.')
		return [AllSlotsReset(), FollowupAction('action_restart_my_conv')]

class ActionRestartMyConv(Action):
	def name(self):
		return 'action_restart_my_conv'

	def run(self, dispatcher, tracker, domain):
		return [Restarted()]