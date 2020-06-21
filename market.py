import json
import webbrowser
from configparser import ConfigParser

# Define locations
config = ConfigParser()
config.read('locations.cfg')
cities = json.loads(config.get("Config", "locations"))


# Search function
def search():
    # Get search query and format
    query = input("Enter search query: ")
    newquery = query.replace(" ", "%20")
    # Search each city and open in a new tab
    for i in range(len(cities)):
        print("Searching for " + query + " in " + cities[i])
        webbrowser.open("https://www.facebook.com/marketplace/" + cities[i] + "/search?query=" + newquery)


# Main
if __name__ == "__main__":
    while True:
        search()
