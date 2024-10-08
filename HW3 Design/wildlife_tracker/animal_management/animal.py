from typing import Any, Optional

class Animal:
    def __init__(self, 
                 animal_id: int,
                 species: str, 
                 age: int = None, 
                 health_status: str = None):
        self.animal_id = animal_id
        self.species = species
        self.age = age
        self.health_status = health_status
        
    
    def update_animal_details(self, animal_id: int, **kwargs: Any) -> None:
        pass

    def get_animal_details(self, animal_id) -> dict[str, Any]:
        pass
