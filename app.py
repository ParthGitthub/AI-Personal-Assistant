import streamlit as st
import requests


st.title(" Your Personal Assistant")


st.subheader("What can your personal assistant do?")


st.markdown("""
            1. Answer questions on various topics.   
            2. Arrange Calendar events and meetings.  
            3. Read your emails and send replies, can even summarize them for you.
            4. Manage your tasks and to-do lists.
            5. Take quick notes for you.
            6. Track your expenses and budgeting.
            """)


st.subheader("💬 Chat with your assistant")


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


user_message = st.chat_input()

      

if user_message:
    with st.chat_message("user"):
        st.markdown(user_message)
        # append the user message to message history
        st.session_state.messages.append({"role": "user", "content": user_message})
    
    
    response = requests.post(
        "url",  # replace with your n8n webhook URL
        json={"message": user_message}
    )
    
    
    ai_response = response.json()[0]["output"]
    
    
    with st.chat_message("assistant"):
        st.markdown(ai_response)
        
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
