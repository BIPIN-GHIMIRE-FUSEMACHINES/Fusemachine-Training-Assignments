'''
Create a function add_to_json that takes a filename and a dictionary as input. The
function should read the JSON data from the file, add the new dictionary to it, and
write the updated data back to the same file.
'''


import json

def add_to_json(filename, new_data):
    """
    Read JSON data from the file, add the new dictionary to it, and write the updated data back to the same file.

    Args:
        filename (str): The name of the JSON file.
        new_data (dict): The dictionary to be added to the JSON data.

    Returns:
        None

    """
    try:
        with open(filename, "r") as file:
            json_data = json.load(file)

        json_data.append(new_data)

        with open(filename, "w") as file:
            json.dump(json_data, file, indent=2)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON data in the file '{filename}'.")




new_data = {
    "name": "Sitaram",
    "age": 67
}

add_to_json("data.json", new_data)
