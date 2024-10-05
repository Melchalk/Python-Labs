def start_block(new_pet, say_all_properties):
    print("Block 'Pet' was started")
    return new_pet(say_all_properties)

def say_pet_properties(**pet):
    print("-------------------")
    for property in pet.keys():
        print(f"{property} - {pet.get(property)}")
    print("-------------------")

def get_pets_properties(say_property, *properties):
    pets_properties = dict()
    for property in properties:
        say_property(property)
        pets_properties[property] = input()
    return pets_properties

get_list_properties = lambda : ["name", "age", "type"]

def create_pet(say_all_properties):
    say_property = lambda title: print(f"Property '{title}': ", end='')
    pets_properties = get_pets_properties(say_property, *get_list_properties())
    say_all_properties(**pets_properties)
    return pets_properties

def get_voice(pet):
    type = pet.get("type")
    def choose_voice():
        if type == "dog": return "woof"
        elif type == "cat": return "meow"
        else: return "brrr"
    print(choose_voice())

def update_pet(pet, say_all_properties):
    print("Pets properties now:")
    say_all_properties(**pet)
    print("Property type to update: ", end='')
    property_type = input()

    def update_property():
        print("New value: ", end='')
        pet[property_type] = input()
        say_all_properties(**pet)

    update_property()
