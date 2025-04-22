import random

class Enemy:
    def __init__(self, health, shield_range):
        self.health = health
        self.shield = random.randint(shield_range[0], shield_range[1])
    def destroy_enemy(self):
        print("Enemy Destroyed")