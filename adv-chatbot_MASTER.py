#!/bin/bash

import random
import requests
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from datetime import datetime

# Define some predefined responses.
greetings = ["hello", "hi", "hey", "howdy"]
goodbyes = ["bye", "goodbye", "see you", "see ya"]
responses = {
	"how are you": ["I'm good, thank you!", "I'm doing fine, how about you?", "All good!"],
	"what's your name": ["I'm PADAM, your virtual assistant.", "You can call be PADAM.", "I go by the name PADAM."],
	"tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!", "What do you call fake spaghetti? An impasta!"],
	"default": ["I'm sorry, I don't understand.", "Could you please rephrase that?", "I'm still learning, can you try something else?"]
}

# Initialize the sentiment analyzer.
sentiment_analyzer = SentimentIntensityAnalyzer()

# Global variable to store context.
context = {}

def get_response(user_input):
	user_input = user_input.lower()
	for key in responses:
		if key in user_input:
			return random.choice(responses[key])
	return random.choice(responses["default"])

def handle_sentiment(user_input):
	# Analyze the sentiment of the user's input.
	sentiment_score = sentiment_analyzer.polarity_scores(user_input)["compound"]
	if sentiment_score >= 0.5:
		return "It seems like you are very positive!"
	elif sentiment_score <= -0.5:
		return "I'm sorry to hear that you are feeling negative. Is there anything I can do to help?  May I suggest a calming circle?"
	else:
		return "It's good to know you have mixed feelings.  How can I assist you?"

# This is a placeholder for a future addition for a weather API.  Below is default for easier update and use at a later date.
# def handle_weather():
# 	# Fetch weather data using an external API key.
# 	api_key = "YOUR_API_KEY_GOES_HERE"
# 	city = "CURRENT_CITY"
# 	url = f"INSERT_URL_FOR_WEATHER_API_HERE"
# 	response = requests.get(url)
# 	if response.status_code == 200:
# 		weather_data = response.json()
# 		description = weather_data["weather"][0]["description"]
# 		temperature = weather_data["main"]["temp"]
# 		return f"In {city}, it is currently {description} with a temperature of {temperature}F."
# 	else:
# 		return "Sorry, I couldn't fetch the weather information at the moment."

def main():
	print("PADAM: Hi! I'm your interactive chatbot.  Type 'exit' or 'quit' to end the conversation.")
	while True:
		user_input = input("You: ")
		if user_input.lower() in ["exit", "quit", "bye", "goodbye", "see ya"]:
			print("PADAM: Goodbye! Have a great day!")
			break

        if "weather" in context:
            response = handle_weather()
            del context["weather"]

            if not response:
            response = get_response(user_input)

        # Contextual Awareness
        if "name" in user_input:
            context["name"] = user_input.split("name")[1].strip() # Store the name in the context dictionary.
            response = "You mentioned a name.  Who is it?"

		# Sentiment Analysis
		if "?" in user_input:
			sentiment_response = handle_sentiment(user_input)
			response += " " + sentiment_response

		# Dynamic Responses
		if "time" in user_input:
			current_time = datetime.now().strftime("%H:%M:%S")
			response += f" The current time is {current_time}."

		# Weather Response(s) - update response once weather API key has been updated.
		if "weather" in user_input:
			context["weather"] = True
			response += " I'm sorry, weather updates are currently a work in progress.  Please check another  time."

        # Personalize the response using stored context.
        if "how are you" in user_input:
            if "name" in context:
                user_name = context["name"]
                response = f"Hello, {user_name}! I'm doing fine, how about you?"
            else:
                response = "I'm good, thank you!"
        elif "what's your name" in user_input:
            if "name" in context:
                user_name = context["name"]
                response = f"{user_name}, you can call me PADAM."
            else:
                response = "I am PADAM, your virtual assistant."

        # Clear context information when it's no longer needed.
        if "name" in context:
            del context["name"]

		print("PADAM:", response)

if __name__ == "__main__":
	main()
