import streamlit as st
from main import generate_story, generate_story_continuation, generate_conclusion

st.title("AI Story Generator")

# --- Session state to store story and characters ---
if "story" not in st.session_state:
    st.session_state.story = ""
if "characters" not in st.session_state:
    st.session_state.characters = []
if "story_stage" not in st.session_state:
    st.session_state.story_stage = "start"  # stages: start, generated, continued, concluded

# User inputs Cohere API key
api_key = st.text_input("Enter your Cohere API Key:", type="password")

# User inputs
genre = st.selectbox("Choose a genre:", ["Sci-Fi", "Fantasy", "Horror", "Rom-Com"])
setting = st.text_input("Describe the setting or prompt:")

# Number of characters input and names input
num_characters = st.number_input("Enter number of characters:", min_value=1, step=1)

characters = []
for i in range(num_characters):
    char_name = st.text_input(f"Name of character {i+1}:", key=f"char_{i}")
    characters.append(char_name.strip())

# Generate Story Button
if st.button("Generate Story"):
    if not api_key:
        st.error("Please enter your Cohere API key.")
    elif not setting.strip():
        st.error("Please enter the setting.")
    elif not all(characters):
        st.error("Please enter all character names.")
    else:
        st.session_state.characters = characters
        st.session_state.story = generate_story(api_key, genre, setting, characters)
        st.session_state.story_stage = "generated"
        st.success("Story generated!")

# Show the story if generated
if st.session_state.story:
    st.markdown("### Current Story:")
    st.write(st.session_state.story)

# Continue Story Button
if st.session_state.story_stage in ["generated", "continued"] and st.button("Continue Story"):
    if not api_key:
        st.error("Please enter your Cohere API key.")
    else:
        st.session_state.story = generate_story_continuation(
            api_key,
            genre,
            setting,
            st.session_state.characters,
            st.session_state.story,
        )
        st.session_state.story_stage = "continued"
        st.success("Story continued!")

# Conclude Story Button
if st.session_state.story_stage in ["generated", "continued"] and st.button("Conclude Story"):
    if not api_key:
        st.error("Please enter your Cohere API key.")
    else:
        st.session_state.story = generate_conclusion(
            api_key,
            genre,
            setting,
            st.session_state.characters,
            st.session_state.story,
        )
        st.session_state.story_stage = "concluded"
        st.success("Story concluded! Thanks for reading.")
        st.markdown("### Final Story:")
        st.write(st.session_state.story)
