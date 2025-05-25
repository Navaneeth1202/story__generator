# 🧠 AI Story Generator

A command-line Python application that uses **Cohere's Large Language Model (LLM)** to generate fun, engaging, and dynamic stories based on user input.

## ✨ Project Description

**AI Story Generator** is an interactive storytelling tool powered by **Cohere's AI model**. It allows users to create original stories from scratch by specifying:

- ✅ Genre (Sci-Fi, Fantasy, Horror, Rom-Com)
- ✅ Main Characters
- ✅ Custom Setting / Prompt

Once the story is generated, users can choose to:
- 🔁 **Continue** the story with new twists
- ✅ **Conclude** the story in a suspenseful or satisfying way

This project showcases how **Generative AI** can enhance creative writing, providing a great learning experience for developers working with LLMs.

---

## 🚀 Features  

- Genre-based storytelling
- Custom user prompts and character setup
- AI-generated story continuation and conclusion
- Curiosity-driven or suspenseful endings
- CLI interaction using Python

---

## 🧩 Requirements

- Python 3.7+
- [`cohere`](https://pypi.org/project/cohere/)
- [`python-dotenv`](https://pypi.org/project/python-dotenv/)

Install all dependencies using:

```bash
pip install -r requirements.txt
____________________________________________________________________________________________________________________________________________________________________________________________________________________

🔧 Setup
1.Clone this repository:
    git clone https://github.com/your-username/story-generator.git
    cd story-generator

2.Create a virtual environment (optional but recommended):
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate

3.Install dependencies:
    pip install -r requirements.txt

4.Run the script:
    python main.py
____________________________________________________________________________________________________________________________________________________________________
🔑 API Key
      👉[Get your Cohere API key here](https://dashboard.cohere.com/api-keys)
____________________________________________________________________________________________________________________________________________________________________
📁 Project Structure

         story-generator/
         │
         ├── main.py # Main entry file for user interaction
         ├── story_module.py # Contains the story generation logic
         ├── requirements.txt # Python dependencies
         └── README.md # Project documentation
___________________________________________________________________________________________________________________________________________________________________
▶️ Run the Application
    python main.py

   #You will be prompted to enter:
   1.Genre (e.g., Sci-Fi, Horror, Rom-Com)
   2.Characters (comma-separated)
   3.Story setting or prompt

   #Then choose:
   1.Continue story
   2.Show conclusion
___________________________________________________________________________________________________________________________________________________________________
🧪 Example Input
    Genre: Horror
    Characters: Mia, Detective Ray, Old Man Keller
    Setting: A foggy abandoned lighthouse off the coast
    ➡️ Generates a spooky horror story ending with a suspenseful twist. You can then choose to continue or conclude the story.
____________________________________________________________________________________________________________________________________________________________________
💻 Example Requirements (requirements.txt)
    cohere
    python-dotenv
____________________________________________________________________________________________________________________________________________________________________________________________________________________
  
