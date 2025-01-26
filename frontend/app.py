import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/chatbot"

st.title("Linux Performance Optimization Chatbot")

if st.button("Get Recommendations"):
    try:
        response = requests.get(API_URL).json()
        if "error" in response:
            st.error(f"API Error: {response['error']}")
        else:
            # st.subheader("System Metrics")
            # st.json(response.get("metrics", {}))
            # st.subheader("Chatbot Response")
            st.text(response.get("content", "No response from chatbot."))
    except requests.exceptions.RequestException as e:
        st.error(f"Request Error: {e}")
    except ValueError:
        st.error("Invalid JSON received from API.")

