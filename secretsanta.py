import random

def secret_santa(participants, exceptions):
    if (len(participants)) < 2:
        raise ValueError("Il doit y avoir au moins deux participants")

    def is_valid_assignment(assignments):
        for giver, receiver in assignments.items():
            if receiver in exceptions.get(giver, []):
                return False
        return True
    
    while True:
        shuffled = participants[:]
        random.shuffle(shuffled)
        assignments = {participants[i]: shuffled[i] for i in range(len(participants))}

        if all(assignments[participant] != participant for participant in participants) and is_valid_assignment(assignments):
            return assignments
        
# Liste des participants
participants = ["Nicolas", "Audrey", "Thierry", "Annie", "Aurélien", "Marie", "Christophe", "Sylvie", "Laure", "Francis", "Stéphanie"]

# Exceptions
exceptions = {
    "Nicolas": ["Audrey", "Christophe", "Sylvie","Laure"],
    "Audrey": ["Nicolas", "Thierry", "Annie","Aurélien"],
    "Thierry": ["Annie", "Audrey","Aurélien"],
    "Annie": ["Thierry", "Audrey","Aurélien"],
    "Aurélien": ["Marie", "Thierry", "Annie", "Audrey"],
    "Marie": ["Aurélien","Francis", "Stéphanie"],
    "Francis": ["Stéphanie","Marie"],
    "Stéphanie": ["Francis","Marie"],
    "Christophe": ["Nicolas", "Sylvie", "Laure"],
    "Sylvie": ["Nicolas", "Christophe", "Laure"],
}

assignments = secret_santa(participants, exceptions)
for giver, receiver in assignments.items():
    print(f"{giver} donne un cadeau à {receiver}")