import random
from flask import Flask, render_template, request
import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

app = Flask(__name__)

intents = [
    {
        "tag": "greeting",
        "patterns": ["Hello", "Hi", "How are you?", "Hey", "Good morning"],
        "responses": ["Hello!", "Hi there!", "How can I help you?", "Good morning!"]
    },
    {
        "tag": "goodbye",
        "patterns": ["Bye", "Goodbye", "See you later", "Take care"],
        "responses": ["Goodbye!", "See you later!", "Take care!"]
    },
    {
        "tag": "age",
        "patterns": ["How old are you?", "What is your age?", "Tell me your age"],
        "responses": ["I am a chatbot, I don't age!"]
    },
    {
        "tag": "thanks",
        "patterns": ["Thank you", "Thanks", "Thank you so much", "Thanks a lot"],
        "responses": ["You're welcome!", "Happy to help!", "Anytime!"]
    }
]

def respond(user_input):
    for intent in intents:
        for pattern in intent["patterns"]:
            if user_input.lower() in pattern.lower():
                return random.choice(intent["responses"])
    return "Sorry, I didn't understand that. Could you please rephrase?"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["user_input"]
    response = respond(user_input)
    return response

if __name__ == "__main__":
    app.run(debug=True)
