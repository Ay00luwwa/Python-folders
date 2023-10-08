import random

responses = {
    'hello': ['Hi there!', 'Hello!', 'Hey!', 'Hi'],
    'hi': ['Hello', 'what can I do for you?'],
    'how are you': ['I am doing well, thank you.', 'Not too bad.', 'I am great!'],
    'bye': ['Goodbye!', 'Bye!', 'See you later.'],
    'what is the weather like today': ['It is Sunny.', 'It is rainy', 'It would be cloudy'],
    'what is photosynthesis' : ['The process whereby plants manufacture thier food in the presence of sunlight and chlorophyl'],
    'default': ['I am sorry, but I do not understand.', 'Can you please rephrase?', 'I am not sure what you mean.'],
    
}

def chatbot():
    while True:
        user_input = input('You: ')
        if user_input.lower() == 'exit':
            break
        response = responses.get(user_input.lower(), responses['default'])
        print('Bot:', random.choice(response))
        
        
# Start the chatbot
chatbot()