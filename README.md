# 🧠 AI Story Generator

A customizable, AI-powered story generator that creates dynamic and genre-based stories with user-defined characters, settings, and tone. Built using Python and integrated with Cohere's large language models for high-quality text generation.

## 🚀 Features

- 🔥 Genre selection (Fantasy, Horror, Sci-Fi, Romance, Mystery, etc.)
- 👤 Custom number of characters with user-defined names
- 🪄 Dynamic, unique storylines for each run
- 🎭 Emotionally engaging and suspenseful endings
- 📜 Story structure: Introduction → Conflict → Climax → Conclusion
- 🌐 Easy to deploy with Streamlit
- 🔐 Secure API key management via Streamlit Secrets

## 🛠️ Tech Stack

- **Python 3.10+**
- **Cohere API** – for story generation using large language models
- **Streamlit** – for interactive UI (deployment-ready)
- **dotenv / secrets** – for safe API key storage
- **VS Code / GitHub** – for version control and development

## 📦 Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/Navaneeth1202/story__generator.git
   cd story__generator
2.**Install dependencies:**
   pip install -r requirements.txt

3.Set up API key:
Create a file named .streamlit/secrets.toml and add your Cohere API key:

    [cohere]
    api_key = "your-cohere-api-key"
_______________________________________________________________________________________________________________________________________________________________    
## 🧪 **Usage**

You can run the generator either through the command line or with Streamlit UI:

🔹 CLI version (basic):

    python story_generator.py
🔹 Streamlit version (recommended):

    streamlit run streamlit_app.py
_______________________________________________________________________________________________________________________________________________________________
## **Sample Output**

Genre: Mystery  
Characters: Detective Leo, Dr. Mason  
Story:  
Late one rainy evening, Detective Leo arrived at the abandoned lighthouse. Dr. Mason had disappeared, and strange messages kept appearing in blood-red ink...
...But as the sun rose, Leo discovered the final note—hidden in plain sight—and it changed everything.
_______________________________________________________________________________________________________________________________________________________________

## 📁 **Project Structure**

             story__generator/
             ├── app.py         # Streamlit web app interface
             ├── main.py # Main entry file for user interaction
             ├── story_module.py # Contains the story generation logic
             ├── requirements.txt # Python dependencies
             └── README.md # Project documentation
______________________________________________________________________________________________________________________________________________________________
## 📌 **Future Enhancements**

🎨 Image generation for illustrated stories

🧠 Character personality input for deeper narratives

💾 Export story to PDF/Word

📊 Dashboard to analyze reader engagement or tone
