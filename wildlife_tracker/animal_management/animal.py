from typing import Any, Optional

class Animal:
    def __init__(self, age:int, animal_id:int, health_status:str, size:float, species:str):
        self.age = age
        self.animal_id = animal_id
        self.health_status = health_status
        self.size = size
        self.species= species

    def get_animal_details(animal_id) -> dict[str, Any]:
        pass