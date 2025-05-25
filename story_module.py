import os
import cohere

class StoryGenerator:
    def __init__(self, api_key):
        self.client = cohere.Client(api_key)

    def generate_story(self, genre, characters, setting):
        prompt = (
            f"Genre: {genre}\n"
            f"Characters: {', '.join(characters)}\n"
            f"Setting: {setting}\n"
            "Create an engaging story with the above elements. End the story in a suspenseful or curiosity-driven way, so the reader wants to know what happens next."
        )

        response = self.client.generate(
            model="command",
            prompt=prompt,
            max_tokens=400,
            temperature=0.8
        )

        return response.generations[0].text.strip()

    def continue_story(self, existing_story):
        continuation_prompt = (
            f"Continue the following story in a logical and engaging way. Maintain the original tone and characters.\n"
            f"Story so far: {existing_story}\n"
            "Continue the story, ending this part with another suspenseful or curiosity-driven twist."
        )

        response = self.client.generate(
            model="command",
            prompt=continuation_prompt,
            max_tokens=300,
            temperature=0.8
        )

        return response.generations[0].text.strip()

    def conclude_story(self, existing_story):
        conclusion_prompt = (
            f"Conclude the following story in a satisfying and logical way. Resolve all major conflicts and give a sense of closure.\n"
            f"Story so far: {existing_story}\n"
            "Write the conclusion:"
        )

        response = self.client.generate(
            model="command",
            prompt=conclusion_prompt,
            max_tokens=300,
            temperature=0.7
        )

        return response.generations[0].text.strip()
