# Denver Broncos Restaurant ChatBot

The Denver Broncos Restaurant ChatBot is a project that demonstrates various skills in building a retrieval-based chatbot system tailored for a restaurant serving delicious food. In this project, I employ techniques such as tf-idf scoring, word embedding models, and custom user-defined functions to create an interactive chatbot capable of answering a wide range of questions from restaurant diners.

## Project Overview

Retrieval-based chatbots are widely used in customer service environments, where user questions are typically constrained to a specific domain. In this case, my chatbot is designed to provide information about the restaurant's menu items while adding a touch of the Denver Broncos spirit (despite them going 1-4 on the season on Sunday 😢).

1. **Exit Commands Handling**: The chatbot allows users to gracefully end the conversation using predefined exit commands.

2. **User Interaction**: The chatbot engages users in a conversation, taking user input and responding to their queries.

3. **Intent Classification**: It classifies user intents by comparing their input to a set of predefined responses, selecting the most appropriate response.

4. **Entity Recognition**: The chatbot extracts candidate entities (menu items) from user messages to provide contextually relevant responses.

5. **Response Selection**: It selects responses based on both user intent and extracted entities, creating dynamic and context-aware replies.

6. **Code Modularity**: The project is organized into separate Python files, each with a specific purpose (e.g., responses, user functions), demonstrating code modularity and best practices.

## Project Structure

1. **restaurant_bot.py**: This is the main script that defines the chatbot's behavior, handles user input, and responds with information about the restaurant's menu items.

2. **user_functions.py**: Contains utility functions used by the chatbot to preprocess user input, compare word overlap, extract nouns, and compute word similarities.

3. **responses.py**: Stores a list of responses that the chatbot uses to answer user queries about menu items. Responses include placeholders for menu items that are filled based on user input.

## Running the ChatBot

To run the Denver Broncos Restaurant ChatBot:

1. Ensure you have Python 3.x installed.

2. Install the required libraries (spacy, nltk) using `pip`:

   ```
   pip install spacy nltk
   ```

3. Download the spaCy English word vectors model:

   ```
   python -m spacy download en_core_web_lg
   ```

4. Clone or download this project repository to your local machine.

5. Open a terminal or command prompt and navigate to the directory containing `restaurant_bot.py`.

6. Run the chatbot script:

   ```
   python restaurant_bot.py
   ```

7. Start a conversation with the chatbot by entering questions or menu item preferences.

## Example Conversation

Here's an example of a conversation with the Denver Broncos Restaurant ChatBot:

```
Welcome to the Denver Broncos Restaurant ChatBot. What would you like to know about our menu today? Tell me about your specials.
The Orange Crush is our most popular item, just like the Denver Broncos are the pride of the NFL!
Do you have any other questions? What's the Mile High Stadium Special?
Our Mile High Stadium Special is named after the Mile High Stadium. It's a real crowd-pleaser!
Do you have any other questions? Exit
Goodbye! Have a great day!
```
