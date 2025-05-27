import cohere

class StoryGenerator:
    def __init__(self, api_key):
        self.client = cohere.Client(api_key)

    def generate_story(self, genre, characters, setting):
        prompt = (
            f"Genre: {genre}\n"
            f"Setting: {setting}\n"
            f"Characters: {', '.join(characters)}\n"
            "Write the start of a story:"
        )
        response = self.client.generate(prompt=prompt, max_tokens=500)
        return response.generations[0].text.strip()

    def generate_story_continuation(self, genre, characters, setting, previous_story):
        prompt = (
            f"Genre: {genre}\n"
            f"Setting: {setting}\n"
            f"Characters: {', '.join(characters)}\n"
            f"Previous story:\n{previous_story}\n"
            "Continue the story:"
        )
        response = self.client.generate(prompt=prompt, max_tokens=300)
        continuation = response.generations[0].text.strip()
        return previous_story + "\n\n" + continuation
