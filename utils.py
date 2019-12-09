import smtplib, ssl
import traceback
import json
import constants
import re
import email_credentials

price_dict = {'low': {
        'min': 0,
        'max': 300
    },
    'mid': {
        'min': 301,
        'max': 700
    },
    'high': {
        'min': 701,
        'max': 100000
    }}

def get_location(zomato, tracker):
		try:
			city_name = tracker.get_slot('location')

			print(city_name)

			location_detail=zomato.get_location(city_name, 1)

			d1 = json.loads(location_detail)

			if len(d1['location_suggestions']) == 0:
				return {'error': 'No such city found, kindly enter the city again', 'loc': [0, 0], 'name': None}
			elif city_name.lower() not in constants.serving_cities:
				return {'error': "Sorry, we don't serve here yet! Please provide some different loation.", 'loc': [0, 0], 'name':  None}

			lat=d1["location_suggestions"][0]["latitude"]
			lon=d1["location_suggestions"][0]["longitude"]
			return {'error': None, 'loc': [lat, lon], 'name': city_name }
		except Exception:
			traceback.print_exc()
			return {'error': 'Error while finding location', 'loc': [0, 0], 'name': None }


def get_cuisine_id(zomato, tracker):
    cuisine = tracker.get_slot('cuisine')
    cuisines_set = set(constants.cuisines_dict.keys())
    formatted_cuisine = re.sub('[^A-Za-z]', '', cuisine).lower()
    if (formatted_cuisine not in cuisines_set):
        return {'error': 'Sorry, currently we do not serve for this cuisine', 'id': None}
    cuisines_dict = constants.cuisines_dict
    return {'error': None, 'id': str(cuisines_dict.get(cuisine))}


def filterByPrice(restaurants, priceRange='mid'):
    if priceRange not in price_dict:
        return []

    price_values = price_dict[priceRange]
    filteredRestaurants = []
    # restaurant.average_cost_for_two
    for eachRestaurant in restaurants:
        average_cost = eachRestaurant['restaurant']['average_cost_for_two']
        if (average_cost >= price_values['min'] and average_cost <= price_values['max']):
            filteredRestaurants.append(eachRestaurant)
    return filteredRestaurants


def send_mail(receiver, restaurants, tracker):
    msg = ''
    if (len(restaurants) == 0):
        msg = 'Sorry, no restaurants found in this price range.'
    else:
        i = 0
        while i < len(restaurants):
            name = restaurants[i]['restaurant']['name']
            rating = restaurants[i]['restaurant']['user_rating']['aggregate_rating']
            address = restaurants[i]['restaurant']['location']['address']
            cost = restaurants[i]['restaurant']['average_cost_for_two']
            msg = msg + '{}. {}\n Rating: {}\n Address: {}\n Cost for two: {}\n\n'.format(i+1, name, rating, address, cost)

            i = i + 1
            if i >= 10:
                break

    city_name = tracker.get_slot('location')
    cuisine_name = tracker.get_slot('cuisine')
    price_name = tracker.get_slot('price')

    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 

    # start TLS for security 
    s.starttls() 

    # Authentication 
    s.login(email_credentials.username, email_credentials.password)

    price_value = price_name
    if price_name in price_dict:
        value = price_dict[price_name]
        price_value = '>= {} and <= {}'.format(value['min'], value['max'])
    
    # message to be sent 
    subject = 'Top 10 restaurants in {} with {} cuisine in budget {} '.format(city_name, cuisine_name, price_value)
    message = 'Subject: {}\n\n{}'.format(subject, msg)

    if len(restaurants) < 10 and len(restaurants) != 0:
        message = '{} \n\n *only {} restaurants found in this budget range.'.format(message, len(restaurants))

    # sending the mail 
    s.sendmail("ashish.pesit@gmail.com", receiver, message) 

    # terminating the session 
    s.quit()
