#!/usr/bin/env python3
def famous_births(people_dict):

        people_sorted = sorted(people_dict.values(), key=lambda x: x['date_of_birth'])
        for person in people_sorted:
                print(f"{person['name']} is a great scientist born in {person['date_of_birth']}.")
# sua definição de método aqui
women_scientists = {
        "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
        "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
        "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
        "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)

