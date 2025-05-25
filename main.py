from story_module import StoryGenerator

def main():
    api_key = input("Enter your Cohere API key: ")
    genre = input("Enter the genre (e.g., horror, sci-fi, rom-com): ")
    setting = input("Enter the setting for the story: ")
    characters = input("Enter the characters (comma-separated): ").split(',')

    sg = StoryGenerator(api_key)

    # Generate the initial story
    story = sg.generate_story(genre, characters, setting)
    print("\n--- Story Start ---\n")
    print(story)
    print(" ")

    while True:
        print("\nWhat would you like to do next?")
        print("1. Continue the story")
        print("2. Conclude the story")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            story = sg.continue_story(story)
            print("\n--- Continued Story ---\n")
            print(story)
        elif choice == "2":
            conclusion = sg.conclude_story(story)
            print("\n--- Conclusion ---\n")
            print(conclusion)
            print("Thank you for using the story generator. Goodbye!")
            break
        elif choice == "3":
            print("Thank you for using the story generator. Goodbye!")
            break
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
