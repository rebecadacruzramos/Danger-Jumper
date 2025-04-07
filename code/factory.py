from player import Player
from enemy import Enemy
from background import Background

class EntityFactory:
    def get_entity(self, entity_type):
        if entity_type == "player":
            return Player()
        elif entity_type == "enemy":
            return Enemy()
        elif entity_type == "background":
            return Background()
        else:
            raise ValueError("Tipo de entidade desconhecido: " + entity_type)