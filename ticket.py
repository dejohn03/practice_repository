import json

def load_tickets():
    try: 
        with open("tictek.json", "r") as file:
            return json.load("file")
    except:
        return FileNotFoundError
print(load_tickets())   
