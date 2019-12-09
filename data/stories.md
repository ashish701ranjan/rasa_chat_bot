## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_search_location
    - slot{"location": "delhi"}

## interactive_story_1
* restaurant_search{"cuisine": "mexican", "price": "mid"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "mid"}
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - utter_ask_email_id
* send_me_email{"email": "ashish@mail.com"}
    - slot{"email": "ashish@mail.com"}
    - action_send_email
    - reset_slots

## interactive_story_1
* restaurant_search{"location": "gwalior"}
    - slot{"location": "gwalior"}
    - action_search_location
    - slot{"location": null}
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_search_location
    - slot{"location": "delhi"}
* restaurant_search{"cuisine": "south-indian"}
    - slot{"cuisine": "south-indian"}
    - utter_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email_id
* restaurant_search{"email": "kapoor@mailtest.com"}
    - slot{"email": "kapoor@mailtest.com"}
    - action_send_email
    - reset_slots

## interactive_story_1
* restaurant_search{"location": "Gwalior"}
    - slot{"location": "Gwalior"}
    - action_search_location
    - slot{"location": null}
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_search_location
    - slot{"location": null}
* restaurant_search{"location": "new york"}
    - slot{"location": "new york"}
    - action_search_location
    - slot{"location": null}
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_search_location
    - slot{"location": "kolkata"}
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_price_range
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - utter_ask_email_id
* restaurant_search{"email": "tes@honeychilli.com"}
    - slot{"email": "tes@honeychilli.com"}
    - action_send_email
    - reset_slots

## interactive_story_1
* restaurant_search{"cuisine": "italian", "price": "mid", "location": "bangalore"}
    - slot{"cuisine": "italian"}
    - slot{"location": "bangalore"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email_id
* send_me_email{"email": "test@mail.com"}
    - slot{"email": "test@mail.com"}
    - action_send_email
    - reset_slots

## interactive_story_1
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - action_search_location
    - slot{"location": null}
* restaurant_search{"location": "Ahmadabad"}
    - slot{"location": "Ahmadabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "Ahmadabad"}
    - utter_ask_email_id
* negative
    - action_send_email
    - reset_slots

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "pune"}
    - slot{"cuisine": "italian"}
    - slot{"location": "pune"}
    - utter_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "pune"}
    - utter_ask_email_id
* send_me_email{"email": "zoom@testmail.com"}
    - slot{"email": "zoom@testmail.com"}
    - action_send_email
    - reset_slots

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "mid", "cuisine": "american", "location": "hyderabad"}
    - slot{"cuisine": "american"}
    - slot{"location": "hyderabad"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "hyderabad"}
    - utter_ask_email_id
* restaurant_search{"email": "yonda@mailinator.com"}
    - slot{"email": "yonda@mailinator.com"}
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "bangalore", "price": "mid"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"price": null}
    - followup{"name": "utter_price_range"}
    - utter_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email_id
* restaurant_search{"email": "test@mailinator.com"}
    - slot{"email": "test@mailinator.com"}
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_search_location
    - slot{"location": "Bangalore"}
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - utter_ask_email_id
* restaurant_search{"email": "cooltestxyz1240@gmail.com"}
    - slot{"email": "cooltestxyz1240@gmail.com"}
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_search_location
    - slot{"location": null}
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - action_search_location
    - slot{"location": null}
* restaurant_search{"location": "Gwalior"}
    - slot{"location": "Gwalior"}
    - action_search_location
    - slot{"location": "Gwalior"}
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "Gwalior"}
    - utter_ask_email_id
* affirm{"email": "testxyzsingh@gmail.com"}
    - slot{"email": "testxyzsingh@gmail.com"}
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_search_location
    - slot{"location": "kolkata"}
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_price_range
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - utter_ask_email_id
* affirm{"email": "ashish701ranjan@gmail.com"}
    - slot{"email": "ashish701ranjan@gmail.com"}
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_search_location
    - slot{"location": null}
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_search_location
    - slot{"location": "Mumbai"}
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_price_range
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email_id
* negative
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_search_location
    - slot{"location": "chandigarh"}
    - utter_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - utter_ask_email_id
* affirm{"email": "ashish701ranjan@gmail.com"}
    - slot{"email": "ashish701ranjan@gmail.com"}
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv

## interactive_story_1
* restaurant_search{"cuisine": "american", "location": "ranchi"}
    - slot{"cuisine": "american"}
    - slot{"location": "ranchi"}
    - action_search_location
    - slot{"location": "ranchi"}
    - utter_price_range
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "ranchi"}
    - utter_ask_email_id
* restaurant_search{"email": "ashish701ranjan@gmail.com"}
    - slot{"email": "ashish701ranjan@gmail.com"}
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv

## interactive_story_1
* restaurant_search{"cuisine": "american", "location": "ranchi"}
    - slot{"cuisine": "american"}
    - slot{"location": "ranchi"}
    - action_search_location
    - slot{"location": "ranchi"}
    - utter_price_range
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "ranchi"}
    - utter_ask_email_id
* restaurant_search{"email": "ashish701ranjan@gmail.com"}
    - slot{"email": "ashish701ranjan@gmail.com"}
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv

## interactive_story_1
* restaurant_search{"cuisine": "american", "location": "ranchi"}
    - slot{"cuisine": "american"}
    - slot{"location": "ranchi"}
    - action_search_location
    - slot{"location": "ranchi"}
    - utter_price_range
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "ranchi"}
    - utter_ask_email_id
* restaurant_search{"email": "ashish701ranjan@gmail.com"}
    - slot{"email": "ashish701ranjan@gmail.com"}
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv

## interactive_story_1
* restaurant_search{"cuisine": "american", "location": "ranchi"}
    - slot{"cuisine": "american"}
    - slot{"location": "ranchi"}
    - action_search_location
    - slot{"location": "ranchi"}
    - utter_price_range
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "ranchi"}
    - utter_ask_email_id
* restaurant_search{"email": "ashish701ranjan@gmail.com"}
    - slot{"email": "ashish701ranjan@gmail.com"}
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv

## interactive_story_1
* restaurant_search{"cuisine": "american", "location": "ranchi"}
    - slot{"cuisine": "american"}
    - slot{"location": "ranchi"}
    - action_search_location
    - slot{"location": "ranchi"}
    - utter_price_range
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "ranchi"}
    - utter_ask_email_id
* restaurant_search{"email": "ashish701ranjan@gmail.com"}
    - slot{"email": "ashish701ranjan@gmail.com"}
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv

## interactive_story_1
* restaurant_search{"cuisine": "american", "location": "ranchi"}
    - slot{"cuisine": "american"}
    - slot{"location": "ranchi"}
    - action_search_location
    - slot{"location": "ranchi"}
    - utter_price_range
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "ranchi"}
    - utter_ask_email_id
* restaurant_search{"email": "ashish701ranjan@gmail.com"}
    - slot{"email": "ashish701ranjan@gmail.com"}
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv

## interactive_story_1
* restaurant_search{"cuisine": "american", "location": "ranchi"}
    - slot{"cuisine": "american"}
    - slot{"location": "ranchi"}
    - action_search_location
    - slot{"location": "ranchi"}
    - utter_price_range
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "ranchi"}
    - utter_ask_email_id
* restaurant_search{"email": "ashish701ranjan@gmail.com"}
    - slot{"email": "ashish701ranjan@gmail.com"}
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv

## interactive_story_1
* restaurant_search{"cuisine": "american", "location": "ranchi"}
    - slot{"cuisine": "american"}
    - slot{"location": "ranchi"}
    - action_search_location
    - slot{"location": "ranchi"}
    - utter_price_range
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "ranchi"}
    - utter_ask_email_id
* restaurant_search{"email": "ashish701ranjan@gmail.com"}
    - slot{"email": "ashish701ranjan@gmail.com"}
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv

## interactive_story_1
* restaurant_search{"cuisine": "american", "location": "ranchi"}
    - slot{"cuisine": "american"}
    - slot{"location": "ranchi"}
    - action_search_location
    - slot{"location": "ranchi"}
    - utter_price_range
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "ranchi"}
    - utter_ask_email_id
* restaurant_search{"email": "ashish701ranjan@gmail.com"}
    - slot{"email": "ashish701ranjan@gmail.com"}
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv

## interactive_story_1
* restaurant_search{"cuisine": "american", "location": "ranchi"}
    - slot{"cuisine": "american"}
    - slot{"location": "ranchi"}
    - action_search_location
    - slot{"location": "ranchi"}
    - utter_price_range
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "ranchi"}
    - utter_ask_email_id
* restaurant_search{"email": "ashish701ranjan@gmail.com"}
    - slot{"email": "ashish701ranjan@gmail.com"}
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv

## interactive_story_1
* restaurant_search{"cuisine": "american", "location": "ranchi"}
    - slot{"cuisine": "american"}
    - slot{"location": "ranchi"}
    - action_search_location
    - slot{"location": "ranchi"}
    - utter_price_range
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "ranchi"}
    - utter_ask_email_id
* restaurant_search{"email": "ashish701ranjan@gmail.com"}
    - slot{"email": "ashish701ranjan@gmail.com"}
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv    

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "raipur"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "raipur"}
    - action_search_location
    - slot{"location": "raipur"}
    - utter_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "raipur"}
    - utter_ask_email_id
* restaurant_search{"email": "ashish701ranjan@gmail.com"}
    - slot{"email": "ashish701ranjan@gmail.com"}
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "raipur"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "raipur"}
    - action_search_location
    - slot{"location": "raipur"}
    - utter_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "raipur"}
    - utter_ask_email_id
* restaurant_search{"email": "ashish701ranjan@gmail.com"}
    - slot{"email": "ashish701ranjan@gmail.com"}
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "raipur"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "raipur"}
    - action_search_location
    - slot{"location": "raipur"}
    - utter_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "raipur"}
    - utter_ask_email_id
* restaurant_search{"email": "ashish701ranjan@gmail.com"}
    - slot{"email": "ashish701ranjan@gmail.com"}
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "raipur"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "raipur"}
    - action_search_location
    - slot{"location": "raipur"}
    - utter_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "raipur"}
    - utter_ask_email_id
* restaurant_search{"email": "ashish701ranjan@gmail.com"}
    - slot{"email": "ashish701ranjan@gmail.com"}
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "raipur"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "raipur"}
    - action_search_location
    - slot{"location": "raipur"}
    - utter_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "raipur"}
    - utter_ask_email_id
* restaurant_search{"email": "ashish701ranjan@gmail.com"}
    - slot{"email": "ashish701ranjan@gmail.com"}
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "raipur"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "raipur"}
    - action_search_location
    - slot{"location": "raipur"}
    - utter_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "raipur"}
    - utter_ask_email_id
* restaurant_search{"email": "ashish701ranjan@gmail.com"}
    - slot{"email": "ashish701ranjan@gmail.com"}
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "raipur"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "raipur"}
    - action_search_location
    - slot{"location": "raipur"}
    - utter_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "raipur"}
    - utter_ask_email_id
* restaurant_search{"email": "ashish701ranjan@gmail.com"}
    - slot{"email": "ashish701ranjan@gmail.com"}
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "raipur"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "raipur"}
    - action_search_location
    - slot{"location": "raipur"}
    - utter_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "raipur"}
    - utter_ask_email_id
* restaurant_search{"email": "ashish701ranjan@gmail.com"}
    - slot{"email": "ashish701ranjan@gmail.com"}
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "raipur"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "raipur"}
    - action_search_location
    - slot{"location": "raipur"}
    - utter_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "raipur"}
    - utter_ask_email_id
* restaurant_search{"email": "ashish701ranjan@gmail.com"}
    - slot{"email": "ashish701ranjan@gmail.com"}
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "raipur"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "raipur"}
    - action_search_location
    - slot{"location": "raipur"}
    - utter_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "raipur"}
    - utter_ask_email_id
* restaurant_search{"email": "ashish701ranjan@gmail.com"}
    - slot{"email": "ashish701ranjan@gmail.com"}
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "raipur"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "raipur"}
    - action_search_location
    - slot{"location": "raipur"}
    - utter_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "raipur"}
    - utter_ask_email_id
* restaurant_search{"email": "ashish701ranjan@gmail.com"}
    - slot{"email": "ashish701ranjan@gmail.com"}
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "raipur"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "raipur"}
    - action_search_location
    - slot{"location": "raipur"}
    - utter_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "raipur"}
    - utter_ask_email_id
* restaurant_search{"email": "ashish701ranjan@gmail.com"}
    - slot{"email": "ashish701ranjan@gmail.com"}
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv
## interactive_story_1
* restaurant_search{"cuisine": "american", "location": "bhopal"}
    - slot{"cuisine": "american"}
    - slot{"location": "bhopal"}
    - action_search_location
    - slot{"location": "bhopal"}
    - utter_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "bhopal"}
    - utter_ask_email_id
* negative
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv

## interactive_story_1
* restaurant_search{"cuisine": "South Indian", "location": "dilralterxyz"}
    - slot{"cuisine": "South Indian"}
    - slot{"location": "dilralterxyz"}
    - action_search_location
    - slot{"location": null}
* restaurant_search{"location": "ludhiyana"}
    - slot{"location": "ludhiyana"}
    - action_search_location
    - slot{"location": null}
* restaurant_search{"location": "firozabad"}
    - slot{"location": "firozabad"}
    - action_search_location
    - slot{"location": "firozabad"}
    - utter_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"price": null}
    - followup{"name": "utter_price_range"}
    - utter_price_range
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "firozabad"}
    - utter_ask_email_id

## interactive_story_1
* restaurant_search{"cuisine": "american", "location": "chennai"}
    - slot{"cuisine": "american"}
    - slot{"location": "chennai"}
    - action_search_location
    - slot{"location": "chennai"}
    - utter_price_range

## interactive_story_1
* restaurant_search{"cuisine": "italian", "location": "patna"}
    - slot{"cuisine": "italian"}
    - slot{"location": "patna"}
    - action_search_location
    - slot{"location": "patna"}
    - utter_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "patna"}
    - utter_ask_email_id
* restaurant_search{"email": "ashish701ranjan@gmail.com"}
    - slot{"email": "ashish701ranjan@gmail.com"}
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_search_location
    - slot{"location": "Bangalore"}
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}

## interactive_story_1
* restaurant_search{"price": "mid", "cuisine": "italian", "location": "kochi"}
    - slot{"cuisine": "italian"}
    - slot{"location": "kochi"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "kochi"}
    - utter_ask_email_id
* restaurant_search{"email": "ashish701ranjan@gmail.com"}
    - slot{"email": "ashish701ranjan@gmail.com"}
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv

## interactive_story_1
* restaurant_search{"cuisine": "South Indian", "location": "jalandhar", "price": "mid", "email": "ashish701ranjan@gmail.com"}
    - slot{"cuisine": "South Indian"}
    - slot{"email": "ashish701ranjan@gmail.com"}
    - slot{"location": "jalandhar"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "jalandhar"}
    - action_send_email
    - reset_slots
    - followup{"name": "action_restart_my_conv"}
    - action_restart_my_conv
