import json
import os


def load_data(filepath):
    file_with_json = open(filepath)
    converted_json = json.loads(file_with_json.read())
    return converted_json


def pretty_print_json(json_data):
    return json.dumps(
        json_data, sort_keys=True, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    path_to_json = input("Enter path to JSON  \n")
    json_data = load_data(path_to_json)
    print(pretty_print_json(json_data))
