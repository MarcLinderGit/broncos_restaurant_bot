from collections import Counter
from responses import responses, blank_spot
from user_functions import preprocess, compare_overlap, pos_tag, extract_nouns, compute_similarity
import spacy

# Load word2vec model for English language
# in termial: python -m spacy download en_core_web_lg
word2vec = spacy.load('en_core_web_lg')

# Define exit commands
exit_commands = ("quit", "goodbye", "exit", "no")

# Define a ChatBot class
class ChatBot:

    # Define a method to handle exit commands
    def make_exit(self, user_message):
        for exit_command in exit_commands:
            if exit_command in user_message:
                print("Goodbye! Have a great day!")
                return True

    # Define a method to initiate a chat with the user
    def chat(self):
        user_message = input("Welcome to the Denver Broncos Restaurant ChatBot. What would you like to know about our menu today? ")
        while not self.make_exit(user_message):
            user_message = self.respond(user_message)

    # Define a method to find the best intent match in the responses
    def find_intent_match(self, responses, user_message):
        bow_user_message = Counter(preprocess(user_message))
        bow_responses = [Counter(preprocess(response)) for response in responses]
        similarity_list = [compare_overlap(bow_response, bow_user_message) for bow_response in bow_responses]
        response_index = similarity_list.index(max(similarity_list))
        return responses[response_index]

    # Define a method to extract candidate entities
    def find_entities(self, user_message):
        tagged_user_message = pos_tag(preprocess(user_message))
        message_nouns = extract_nouns(tagged_user_message)
        tokens = word2vec(" ".join(message_nouns))
        category = word2vec(blank_spot)
        word2vec_result = compute_similarity(tokens, category)
        word2vec_result.sort(key=lambda x: x[2])
        if len(word2vec_result) < 1:
            return blank_spot
        else:
            return word2vec_result[-1][0]  # Return the first element of the last list item

    # Define a method to respond to user queries
    def respond(self, user_message):
        best_response = self.find_intent_match(responses, user_message)
        entity = self.find_entities(user_message)
        print(best_response.format(entity))
        input_message = input("Do you have any other questions? ")
        return input_message

# Initialize an instance of the ChatBot
DenverBroncosBot = ChatBot()

# Start the chat
DenverBroncosBot.chat()
