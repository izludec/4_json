import json
import os


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def pretty_print_json(json_data):
    print(json.dumps(
    json_data, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    path_to_json = input("Enter path to JSON  \n")
    try:
        json_data = load_data(path_to_json)
    except OSError:
        print("File not found")
        json_data = None
    except ValueError:
        print("Wrong json")
        json_data = None
    else:
        pretty_print_json(json_data)
