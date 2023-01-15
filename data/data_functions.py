import json

def load_json() -> dict:

    with open("./data/user.json", "r") as f:
        return json.load(f) 
    

def write_json(new_data : dict) -> None:

    with open("./data/user.json", "w") as f:
        json.dump(new_data, f) 

    return 