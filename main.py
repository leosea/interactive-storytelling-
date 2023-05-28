from interactive_story_plugin import InteractiveStoryPlugin

def main():
    # Create a new InteractiveStoryPlugin object
    story_plugin = InteractiveStoryPlugin()

    # Set the genre of the story
    story_plugin.choose_genre("fantasy")

    # Create a character
    character_details = {
        "name": "Alice",
        "age": 20,
        "occupation": "wizard",
    }
    story_plugin.create_character(character_details)

    # Start the story
    user_input = "Alice starts her journey in a magical forest."
    story_plugin.user_input(user_input)

    # Continue the story
    user_input = "Alice encounters a mysterious creature."
    story_plugin.user_input(user_input)

    # Describe the current scene
    scene_description = story_plugin.describe_scene()
    print(scene_description)

if __name__ == "__main__":
    main()
