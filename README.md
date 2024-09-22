# DostChat: A Rasa-powered Chatbot for Overcoming Loneliness

DostChat is a compassionate and engaging chatbot designed to provide companionship and support for individuals experiencing loneliness. Built using the powerful Rasa Python library, it leverages natural language understanding (NLU) to engage in meaningful conversations that foster a sense of connection.

## Features:

### Empathetic Interactions: 
DostChat utilizes Rasa's NLU capabilities to understand user sentiment and respond with supportive messages tailored to their emotional state.
### Open-Ended Dialogues: 
Encourage users to express themselves freely and explore their feelings without judgment through open-ended conversation prompts.
### Activity Suggestions: 
DostChat offers ideas for activities that can help users combat loneliness, promoting self-care and social engagement.

## Structure and Files:

### domain.yml: 
Defines the chatbot's domain, including intents (user purposes) and entities (specific words or phrases with meaning).
### nlu.yml: 
Trains the NLU model on patterns in user language to identify intents and extract entities.
### config.yml: 
Configures various aspects of the chatbot's behavior, such as dialogue policies, training parameters, and logging settings.
### stories.yml: 
Defines conversation flow and how the chatbot should react to user intents and entities through dialogue trees.
### actions.py: 
Contains custom code for actions the chatbot can take, such as fetching weather information or suggesting resources.
## Getting Started:
For those interested in contributing to DostChat's development or deploying it for their own use, this repository includes detailed instructions on setting up the Rasa environment and customizing the chatbot.

### Additional Notes:
Consider highlighting specific examples of intents and entities that your chatbot can handle.
Briefly mention the Rasa version you're using for compatibility purposes.
If you have plans for future development (e.g., integrating with external APIs), you can mention them to spark interest.
