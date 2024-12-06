# import streamlit as st
# import os
# from groq import Groq
# import random

# from langchain.chains import ConversationChain
# from langchain.chains.conversation.memory import ConversationBufferWindowMemory
# from langchain_groq import ChatGroq
# from langchain.prompts import PromptTemplate
# from dotenv import load_dotenv
# import os 

# load_dotenv()

# groq_api_key = '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'

# def main():

#     st.title("Groq Chat App")

#     # Add customization options to the sidebar
#     st.sidebar.title('Select an LLM')
#     model = st.sidebar.selectbox(
#         'Choose a model',
#         ['mixtral-8x7b-32768', 'llama2-70b-4096']
#     )
#     conversational_memory_length = st.sidebar.slider('Conversational memory length:', 1, 10, value = 5)

#     memory=ConversationBufferWindowMemory(k=conversational_memory_length)

#     user_question = st.text_area("Ask a question:")

#     # session state variable
#     if 'chat_history' not in st.session_state:
#         st.session_state.chat_history=[]
#     else:
#         for message in st.session_state.chat_history:
#             memory.save_context({'input':message['human']},{'output':message['AI']})


#     # Initialize Groq Langchain chat object and conversation
#     groq_chat = ChatGroq(
#             groq_api_key=groq_api_key, 
#             model_name=model
#     )

#     conversation = ConversationChain(
#             llm=groq_chat,
#             memory=memory
#     )

#     if user_question:
#         response = conversation(user_question)
#         message = {'human':user_question,'AI':response['response']}
#         st.session_state.chat_history.append(message)
#         st.write("Chatbot:", response['response'])

# if __name__ == "__main__":
#     main()










# import streamlit as st
# import os
# from groq import Groq
# import random
# import speech_recognition as sr
# import pyttsx3
# from langchain.chains import ConversationChain
# from langchain.chains.conversation.memory import ConversationBufferWindowMemory
# from langchain_groq import ChatGroq
# from dotenv import load_dotenv

# load_dotenv()

# groq_api_key = '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'

# # Initialize TTS engine
# tts_engine = pyttsx3.init()
# tts_engine.setProperty('rate', 150)  # Set speaking speed

# def listen_to_voice():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.write("Listening... Speak now!")
#         try:
#             audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
#             text = recognizer.recognize_google(audio)
#             st.write(f"You said: {text}")
#             return text
#         except sr.UnknownValueError:
#             st.error("Sorry, I could not understand your speech.")
#         except sr.RequestError as e:
#             st.error(f"Could not request results; {e}")
#         except sr.WaitTimeoutError:
#             st.error("Listening timed out. Try again.")
#         return ""

# def main():
#     st.title("Groq Chat App")

#     # Add customization options to the sidebar
#     st.sidebar.title('Select an LLM')
#     model = st.sidebar.selectbox(
#         'Choose a model',
#         ['mixtral-8x7b-32768', 'llama2-70b-4096']
#     )
#     conversational_memory_length = st.sidebar.slider('Conversational memory length:', 1, 10, value=5)

#     memory = ConversationBufferWindowMemory(k=conversational_memory_length)

#     # Session state variable
#     if 'chat_history' not in st.session_state:
#         st.session_state.chat_history = []
#     else:
#         for message in st.session_state.chat_history:
#             memory.save_context({'input': message['human']}, {'output': message['AI']})

#     # Initialize Groq Langchain chat object and conversation
#     groq_chat = ChatGroq(
#         groq_api_key=groq_api_key, 
#         model_name=model
#     )

#     conversation = ConversationChain(
#         llm=groq_chat,
#         memory=memory
#     )

#     # Voice or text input
#     input_mode = st.radio("Input Mode", ['Text', 'Voice'])
#     user_question = ""
#     if input_mode == 'Text':
#         user_question = st.text_area("Ask a question:")
#     elif input_mode == 'Voice':
#         if st.button("Speak"):
#             user_question = listen_to_voice()

#     if user_question:
#         response = conversation(user_question)
#         message = {'human': user_question, 'AI': response['response']}
#         st.session_state.chat_history.append(message)

#         st.write("Chatbot:", response['response'])

#         # Play the audio response
#         tts_engine.say(response['response'])
#         tts_engine.runAndWait()

# if __name__ == "__main__":
#     main()


from gtts import gTTS
import streamlit as st
import os
from groq import Groq
import random
import speech_recognition as sr
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

groq_api_key = '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'

def listen_to_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening... Speak now!")
        try:
            audio = recognizer.listen(source, timeout=20, phrase_time_limit=10)
            text = recognizer.recognize_google(audio)
            st.write(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            st.error("Sorry, I could not understand your speech.")
        except sr.RequestError as e:
            st.error(f"Could not request results; {e}")
        except sr.WaitTimeoutError:
            st.error("Listening timed out. Try again.")
        return ""

def play_audio(response_text):
    tts = gTTS(response_text)
    audio_file = "response.mp3"
    tts.save(audio_file)
    st.audio(audio_file, format="audio/mp3")
    os.remove(audio_file)  # Clean up after playing

def main():
    st.title("Groq Chat App")

    # Add customization options to the sidebar
    st.sidebar.title('Select an LLM')
    model = st.sidebar.selectbox(
        'Choose a model',
        ['mixtral-8x7b-32768', 'llama2-70b-4096']
    )
    conversational_memory_length = st.sidebar.slider('Conversational memory length:', 1, 10, value=5)

    memory = ConversationBufferWindowMemory(k=conversational_memory_length)

    # Session state variable
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    else:
        for message in st.session_state.chat_history:
            memory.save_context({'input': message['human']}, {'output': message['AI']})

    # Initialize Groq Langchain chat object and conversation
    groq_chat = ChatGroq(
        groq_api_key=groq_api_key, 
        model_name=model
    )

    conversation = ConversationChain(
        llm=groq_chat,
        memory=memory
    )

    # Voice or text input
    input_mode = st.radio("Input Mode", ['Text', 'Voice'])
    user_question = ""
    if input_mode == 'Text':
        user_question = st.text_area("Ask a question:")
    elif input_mode == 'Voice':
        if st.button("Speak"):
            user_question = listen_to_voice()

    if user_question:
        response = conversation(user_question)
        message = {'human': user_question, 'AI': response['response']}
        st.session_state.chat_history.append(message)

        st.write("Chatbot:", response['response'])

        # Play the audio response
        play_audio(response['response'])

if __name__ == "__main__":
    main()
