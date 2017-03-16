#Ally attributes

number_of_allys = input("Number of allys? ")
number_of_allys= int(number_of_allys)
level_of_ally = input("Level of allys? ")
level_of_ally = int(number_of_allys)
ally_health = (level_of_ally * 100)
ally_damage = (level_of_ally *100)

#Enemy attributes

number_of_enemys = input("Number of enemies? ")
number_of_enemys = int(number_of_enemys)
level_of_enemy = input("Level of enemies? ")
level_of_enemy = int(level_of_enemy)
enemy_health = (level_of_enemy*100)
enemy_damage = (level_of_enemy*100)

#Ally team function

ally_team_health = (number_of_allys*ally_health)
ally_team_damage = (number_of_allys*ally_damage)
enemy_team_health = (number_of_enemys*enemy_health)
enemy_team_damage = (number_of_enemys*enemy_damage)

print (" ")
print (" ")
print ("Welcome to Dungeon Wars AI!!")
print (" ")
print (" ")
print ("Number of Allys: "+str(number_of_allys))
print ("Level of Allys: "+str(level_of_ally))
print (" ")
print ("Number of Enemys: "+str(number_of_enemys))
print ("Level of Enemys: "+str(level_of_enemy))

#Dungeon battle
print (" ")
print (" ")
print ("Welcome to the Dungeon!")
print (" ")
print (" ")
print ("Initiate battle!")
print (" ")
print (" ")

if ally_team_health >= enemy_team_damage:
    print ("Allys win!")
    print ("Ally health remaining: "+str(ally_team_health-enemy_team_damage))
else:
    print ("Allys have been defeated!")
    print ("Enemy health remaining: "+str(enemy_team_damage-ally_team_health))
