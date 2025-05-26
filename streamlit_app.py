# Regenerate the Streamlit app with Rom-Com genre using Cohere Chat API
streamlit_chat_romcom_code = """
import streamlit as st
import requests

st.set_page_config(page_title="AI Story Generator", layout="centered")
st.title("🧠 AI-Based Story Generator")
st.subheader("Powered by Cohere (Chat API)")

# Input section
genre = st.selectbox("Choose a Genre", ["Fantasy", "Horror", "Sci-Fi", "Mystery", "Rom-Com"])
char_count = st.slider("Number of Characters", 1, 5, 2)
char_names = []

for i in range(char_count):
    name = st.text_input(f"Enter name for character {i + 1}", key=f"name_{i}")
    if name:
        char_names.append(name)

# API Key input (hidden)
api_key = st.text_input("Enter your Cohere API Key", type="password")

if st.button("Generate Story"):
    if not api_key or not char_names:
        st.warning("Please provide all required inputs and your API key.")
    else:
        prompt = f"Write a {genre} story involving {', '.join(char_names)}. The story should have a suspenseful or emotional ending."

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "command",
            "chat_history": [],
            "message": prompt,
            "temperature": 0.7
        }

        response = requests.post("https://api.cohere.ai/v1/chat", json=data, headers=headers)

        if response.status_code == 200:
            story = response.json().get("text", "")
            st.success("🎉 Story Generated Successfully!")
            st.markdown(story)
        else:
            st.error(f"❌ Error: {response.status_code} - {response.text}")
"""

# Save file
romcom_file_path = "/mnt/data/streamlit_app_with_romcom.py"
with open(romcom_file_path, "w") as f:
    f.write(streamlit_chat_romcom_code)

romcom_file_path
