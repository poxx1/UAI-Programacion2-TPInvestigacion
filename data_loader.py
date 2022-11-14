from person import Person
import json

def get_clients_from_file(path):
    clients = []
    file = open(path, "r")
    
    personJson = json.loads(file.read())
    for person in personJson:
        clients.append(Person(**person))

    return clients