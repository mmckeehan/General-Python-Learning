"""
This is a simple "fighting" game that was built to test out using a simple class. While this is a simple script, I was able to learn
alot about the flow of a program and simple debugging. 
"""

import random
from enemy import Enemy


def main():
    player_attack = (1, 4)
    enemy1 = Enemy(5, (10, 16))
    enemy2 = Enemy(5, (20, 51))
    print("Wild enemy appears\n")
    fight(enemy1, player_attack)
    print ("You win!\n\n...\n\nWait, what's that?\n")

    fight(enemy2, player_attack)
    print("Now you win!") 

def fight(enemy, attack):
    shield = enemy.shield
    health = enemy.health
    while health > 0:
        print(f"   Enemy Health: {health}\n   Enemy Shield: {shield}\n")
        input("Press \"Enter\" to attack\n")
        damage = random.randint(attack[0], attack[1])
        print(f"Attack Damage: {damage}\n")
        if shield > 0:
            if damage >= shield:
                shield = 0
            else:
                shield -= damage
        else:
            health -= damage
    if health <= 0:
        Enemy.destroy_enemy(enemy)

if __name__ == "__main__":
    main()