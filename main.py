from story_module import StoryGenerator

def generate_story(api_key, genre, setting, characters):
    sg = StoryGenerator(api_key)
    return sg.generate_story(genre, characters, setting)

def generate_story_continuation(api_key, genre, setting, characters, previous_story):
    sg = StoryGenerator(api_key)
    return sg.generate_story_continuation(genre, characters, setting, previous_story)

def generate_conclusion(api_key, genre, setting, characters, current_story):
    sg = StoryGenerator(api_key)
    prompt = (
        f"Genre: {genre}\n"
        f"Setting: {setting}\n"
        f"Characters: {', '.join(characters)}\n"
        f"Story so far:\n{current_story}\n"
        "Write a satisfying conclusion to this story:"
    )
    response = sg.client.generate(prompt=prompt, max_tokens=200)
    conclusion = response.generations[0].text.strip()
    return current_story + "\n\n" + conclusion
