import random
from datetime import datetime

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
participants = ["Audrey", "Francis", "Nicolas", "Laure", "Annie", "Christophe", "Stéphanie", "Marie", "Thierry", "Sylvie", "Aurélien"]

# Exceptions
exceptions = {
    "Nicolas": ["Audrey", "Christophe", "Sylvie"],
    "Audrey": ["Nicolas", "Thierry", "Annie"],
    "Thierry": ["Annie", "Audrey", "Aurélien"],
    "Annie": ["Thierry", "Audrey", "Aurélien"],
    "Aurélien": ["Marie", "Thierry", "Annie"],
    "Marie": ["Aurélien","Francis", "Stéphanie"],
    "Francis": ["Stéphanie", "Marie"],
    "Stéphanie": ["Francis", "Marie"],
    "Christophe": ["Nicolas", "Sylvie", "Laure"],
    "Sylvie": ["Nicolas", "Christophe", "Laure"],
    "Laure": ["Christophe", "Sylvie"],
}

assignments = secret_santa(participants, exceptions)
with open("tirage.txt", "a", encoding="UTF-8") as f:
    current_time = datetime.now().strftime("%d %B %Y à : %Hh:%Mmin:%Ss")
    f.write(f"\nTirage du {current_time}.\n")
    count=0
    for giver, receiver in assignments.items():
        count+=1
        f.write(f"{giver} donne un cadeau à {receiver}\n")
        print("----------------------------------------------")
        print(f"Tirage {count}/{len(participants)}")
        print(f"{giver} donne un cadeau à {receiver}")
        print("Appuie sur entrée pour voir le prochain duo !")
        print("----------------------------------------------")
        if count == len(participants):
            print("Tirage terminé !\n")
            input()
            break
        input()
