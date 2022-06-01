import time, sys, random, json
from datetime import datetime

def sprint(text, wait=0.05):
	for i in text:
		print(i,end="",flush = True)
		time.sleep(wait)
	print("")  

class weapon:
    def __init__(self, damage, hitChance, durability):
        self.damage = damage
        self.hitChance = hitChance
        self.durability = durability

class enemy:
    def __init__(self, damage, health, level):
        self.damage = damage
        self.health = health
        self.level = level

class food:
  def __init__(self, regen, level):
    self.regen = regen
    self.level = level

class player:
  def __init__(self, level):
    self.level = level

xpCount = 0
levelCount = 1
playerGold = 0
combat = True


stick = weapon(5, 75, 100)
sword = weapon(10, 70, 300)

skeleton = enemy(10, 300, 5)
zombie = enemy(10, 500, 6)


Player = player(levelCount)

weaponChoice = input("What weapon do you want to use?")
if weaponChoice == "stick":
  activeWeapon = stick
if weaponChoice == "sword":
  activeWeapon = sword

  

def combatStart():
  global newPlayerGold
  newPlayerGold = playerGold
  if combat:
    print("An enemy has engaged")
    enemy_type_number = random.randint(1,2)
    if enemy_type_number == 1:
      enemy_type = skeleton
    if enemy_type_number == 2:
      enemy_type = zombie
    enemy_health = enemy_type.health
    enemy_damage = enemy_type.damage
    weapon_damage = activeWeapon.damage
    player_health = (100 + (Player.level * 25))
    combatStarted = True
    while combatStarted:
      action = input("What would you like to do?")
      if action == "attack":
        enemy_health = enemy_health - weapon_damage
        player_health -= enemy_damage
      if action == "test":
        print(str(player_health))
      if player_health <= 0:
        print("You have fallen")
        break
      if enemy_health <= 0:
        print("You won!")
        newPlayerGold += (enemy_type.level * random.randint(20,40))
        return(newPlayerGold)


        
combatStart()
playerGold += newPlayerGold

