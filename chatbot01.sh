#!/bin/bash

# Function to handle user input and provide responses.

function chatbot() {
	case "$1" in
		"hello")
			echo "Hello! How can I help you?"
			;;
		"how are you")
			echo "I'm just a bash script, but thanks for asking!"
			;;
		"bye")
			echo "Goodbye! Have a great day!"
			exit 0
			;;
		*)
			echo "Sorry, I didn't understand that."
			;;
	esac
}

# Main loop to keep the chatbot running.

while true; do
	echo "You: "
	read input

	# Convert user input into lowercase for case-sensitivity matching.
	input_lc=$(echo "$input" | tr '[:upper:]' '[:lower:]')

	# Call the chatbot function with the user input.
	chatbot "$input_lc"
done
