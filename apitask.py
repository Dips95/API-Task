import requests
import pandas as pd
import sys
import json

def get_character_data(character_name):
    response = requests.get(f"https://rickandmortyapi.com/api/character/?name={character_name}")
    data = response.json()

    if data["info"]["count"] == 0:
        print(f"No character found with the name {character_name}")
        sys.exit(0)

    character = data["results"][0]
    return character

def get_episode_data(episode_urls):
    episodes = []
    for url in episode_urls:
        response = requests.get(url)
        episode = response.json()
        episodes.append(episode)
    return episodes

def print_and_save_data(character, episodes):
    # Prepare data for DataFrame
    data = {
        "Character Name": character["name"],
        "Current Location": character["location"]["name"],
        "Episodes": [episode["name"] for episode in episodes]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Print tabular data
    print(df.to_string(index=False))

    # Save to Excel (You can mention your own local path to save)
    df.to_excel("C:/Users/dipshikha.ghosh/Downloads/character_data.xlsx", index=False)

def main():
    character_name = sys.argv[1]
    character = get_character_data(character_name)
    episodes = get_episode_data(character["episode"])
    print_and_save_data(character, episodes)

if __name__ == "__main__":
    main()
