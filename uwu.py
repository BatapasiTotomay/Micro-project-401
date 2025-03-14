import json

places = []

while True:
    place = input("Enter a place (or type 'done'): ")  # Prompt user for input
    if place.lower() == 'done':  # Check for 'done' to exit loop
        break
    places.append(place)  # Append the input to the list

places_json = json.dumps(places)  # Convert list to JSON

print("Places you entered:")  # Display the places
print(places_json)  # Print the JSON string

