import json
import os


def load_data(filepath):
    if not os.path.exists(filepath):
        print("File not found")
        return None
    with open(filepath, 'r') as file_handler:
        try:
            return json.load(file_handler)
        except ValueError:
            print("Wrong json")
            return None


def pretty_print_json(json_data):
    return json.dumps(
    json_data, sort_keys=True, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    path_to_json = input("Enter path to JSON  \n")
    json_data = load_data(path_to_json)
    print(pretty_print_json(json_data))
