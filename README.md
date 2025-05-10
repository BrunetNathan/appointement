# Medical Appointment Assistant

This project is a conversational AI assistant built with Rasa. It helps users book medical appointments through natural conversation.

## Features

- Greets users and collects their first and last names.
- Displays doctors and their availability.
- Lets users choose a doctor and appointment time.
- Confirms the booking.

## Project Structure

- `flows.yml`: Defines the conversation flows.
- `domain.yml`: Describes intents, slots, responses, and actions.
- `actions.py`: Contains custom actions (like checking doctor availability).
- `data/doctors.json`: Stores doctors and their available times.
- `config.yml`: Sets up the NLU and command generation.

## Requirements

- Python 3.8+
- Rasa Pro (with LLM support)