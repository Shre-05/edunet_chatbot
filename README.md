# Chatbot Implementation using Streamlit

This project implements a simple chatbot using **Streamlit**, **NLTK** for natural language processing (NLP), and **Scikit-learn** for handling specific ML tasks if necessary. The chatbot is designed to answer a set of predefined questions based on the user’s input.

## Features

- A conversational interface built with **Streamlit**.
- Uses **NLTK** for processing user input and generating meaningful responses.
- Can be easily extended with more responses, intents, and logic.
- Responsive design, compatible with all screen sizes.
- Easily deployable as a web app using **Streamlit**.

## Tech Stack

- **Frontend**: Streamlit (for UI and interaction)
- **Natural Language Processing**: NLTK (for processing text input)
- **Machine Learning (optional)**: Scikit-learn (for advanced ML tasks, if added later)
- **Backend**: Python

## Installation

### Prerequisites

To get started, ensure you have **Python** installed on your system.

You can install the required dependencies by using `pip`:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/shre0505/edunet_chatbot.git
   ```

2. Navigate into the project directory:

   ```bash
   cd chatbot-streamlit
   ```

3. Install the necessary libraries:

   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file includes:

   - `streamlit`
   - `nltk`
   - `scikit-learn`

4. Download the NLTK data needed for the chatbot:

   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```

### Running the Application

Once you have the necessary dependencies, run the following command to start the Streamlit app:

```bash
streamlit run app.py
```

This will start the application, and it should open automatically in your default web browser at `http://localhost:8501`.

## How It Works

1. **User Input**: The user enters a message in the input box.
2. **Processing**: The backend uses NLTK to process and match the input with predefined patterns.
3. **Response Generation**: Based on the user input, a corresponding response is selected from the available set of responses.
4. **Streamlit Display**: The response is displayed on the Streamlit interface, simulating a conversation.

## Example Use Case

- **Greeting**: 
   - User: "Hi"
   - Bot: "Hello"
- **Goodbye**: 
   - User: "How are you"
   - Bot: "Good!"

## Customization

You can easily add more intents and responses to enhance the chatbot's functionality. Here's how to modify the intents:

1. Open the `app.py` file.
2. Update the `intents` variable with new patterns and responses.
3. Add any new logic to handle the different user inputs.

Example of adding a new intent:

```python
{
    "tag": "weather",
    "patterns": ["What's the weather like?", "Is it going to rain today?", "Tell me the weather"],
    "responses": ["I can't check the weather, but I recommend checking a weather app!"]
}
```

### Streamlit UI Enhancements

Streamlit makes it easy to update the UI. You can customize colors, layouts, and add features like images, charts, etc., using the built-in Streamlit components.

