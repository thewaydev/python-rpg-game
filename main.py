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
foodCount = 0
levelCount = 3
playerGold = 0
combat = True


stick = weapon(5, 75, 100)
sword = weapon(10, 70, 300)
devstick = weapon(1000, 100, 100)

skeleton = enemy(10, 30, 5)
zombie = enemy(10, 50, 6)
theif = enemy(15, 100, 10)

burger = food(100, 1)


Player = player(levelCount)

weaponChoice = input(sprint("What weapon do you want to use?"))
if weaponChoice == "stick":
  activeWeapon = stick
if weaponChoice == "sword":
  activeWeapon = sword
if weaponChoice == "devstick":
  activeWeapon = devstick

  

def combatStart():
  global tempXpCount
  global newPlayerGold
  tempXpCount = xpCount
  newPlayerGold = playerGold
  if combat:
    enemy_type_number = random.randint(1,levelCount)
    if enemy_type_number == 1:
      enemy_type = skeleton
    if enemy_type_number == 2:
      enemy_type = zombie
    if enemy_type_number == 3:
      enemy_type = theif
    enemy_health = enemy_type.health
    enemy_damage = enemy_type.damage
    enemy_level = enemy_type.level
    weapon_damage = activeWeapon.damage
    player_health = (100 + (Player.level * 25))
    playerMaxHealth = player_health
    sprint("An" + str(enemy_type) + "has engaged")
    combatStarted = True
    while combatStarted:
      action = input("What would you like to do?")
      if action == "attack":
        enemy_health = enemy_health - weapon_damage
        player_health -= enemy_damage
      if action == "eat":
        food_choice = input("What do you want to eat?")
        if food_choice == "burger":
          player_health += burger.regen
          if player_health > playerMaxHealth:
            player_health = playerMaxHealth
      if action == "devtest1":
        sprint(str(player_health))
      if action == "devtest2":
        sprint(str(enemy_health))
      if action == "":
        player_health -= enemy_damage
      if player_health <= 0:
        sprint("You have fallen")
        break
      if enemy_health <= 0:
        sprint("You won!")
        newPlayerGold += (enemy_type.level * random.randint(20,40))
        sprint("+ " + str(newPlayerGold) + " Gold!")
        tempXpCount += (enemy_level * random.randint(5,10))
        
        mainScreen()

        

def mainScreen():
  global newPlayerGold2
  newPlayerGold2 = playerGold
  print("Welcome to the village!")
  home_tf = True
  while home_tf == True:
    home_action = input("What would you like to do?")
    if home_action == "Fight" or "fight":
      combatStart()
      break
    if home_action == "Shop" or "shop":
      sprint("Welcome to the shop!")
      shop_action = input("1. Food, 2. Weapons")
      if shop_action == "Food" or "food":
        sprint("What type of food would you like to buy?")
        food_buy_type = input(": ")
        if food_buy_type == "burger" or "Burger":
          newPlayerGold2 -= 30
      
      
      
      
      

        
combatStart()

playerGold += newPlayerGold
xpCount += tempXpCount

