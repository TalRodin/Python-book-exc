import pet
def main():
    pet_info=input().split()
    pet_i=pet.Pet(pet_info[0],pet_info[1],pet_info[2])
    print(pet_i.get_name())
    print(pet_i.get_animal_type())
    print(pet_i.get_age())
main()
