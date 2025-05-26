
import streamlit as st
import requests

st.set_page_config(page_title="AI Story Generator", layout="centered")
st.title("🧠 AI-Based Story Generator")
st.subheader("Powered by Cohere")

# Input section
genre = st.selectbox("Choose a Genre", ["Fantasy", "Horror", "Sci-Fi", "Mystery"])
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
        prompt = f"Write a {genre} story involving {', '.join(char_names)}. The story should have a suspenseful ending."

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "command-xlarge-nightly",
            "prompt": prompt,
            "max_tokens": 300,
            "temperature": 0.7
        }

        response = requests.post("https://api.cohere.ai/v1/generate", json=data, headers=headers)

        if response.status_code == 200:
            story = response.json()["generations"][0]["text"]
            st.success("🎉 Story Generated Successfully!")
            st.markdown(story)
        else:
            st.error(f"❌ Error: {response.status_code} - {response.text}")
