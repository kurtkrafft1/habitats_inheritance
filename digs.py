from animals import (Ant, BettaFish, Copperhead, EarthWorm, Finch, Gerbil, Mouse, Parakeet, Rattlesnake, Terrapin)
from movements import (IWalk, ISlither, ISwim, IFly , IDig)
from habitats import (Aquarium, FlyCage, Atrium, LandCage, Terrarium, WaterCage)

andy = Ant("Andy", "Fire Red")
barry = BettaFish("Barry", "Blue")
calvin = Copperhead("Calvin", 'Camo')
earl = EarthWorm("Earl", "Mud Brown")
frita = Finch("Frita", "Yellow")
grandpa = Gerbil("Granpa", "Brown")
milton = Mouse("milton", "Orange")
paulina = Parakeet("Paulina", "Purple")
rayray = Rattlesnake("Ray-Ray", "Camo")
tim = Terrapin("Tim", "green")

aqua = Aquarium()
atri = Atrium()
terra = Terrarium()
flyCage = FlyCage()
landCage = LandCage()
waterCage = WaterCage()


#Uncomment by section

#SECTION 1_____________________________________

# #Aquarium adds
# aqua.add_animal(barry)
# aqua.add_animal(tim)

# #Atrium Adds
# atri.add_animal(frita)
# atri.add_animal(paulina)

# #Terrarium Adds
# terra.add_animal(andy)
# terra.add_animal(calvin)
# terra.add_animal(earl)
# terra.add_animal(grandpa)
# terra.add_animal(milton)
# terra.add_animal(rayray)



#SECTION 2_____________________________________

# #Water Cage Adds
# waterCage.add_animal(barry)
# waterCage.add_animal(tim)

# #Fly Cage Adds
# flyCage.add_animal(frita)
# flyCage.add_animal(paulina)

# #Land Cage Add
# landCage.add_animal(andy)
# landCage.add_animal(calvin)
# landCage.add_animal(earl)
# landCage.add_animal(grandpa)
# landCage.add_animal(milton)
# landCage.add_animal(rayray)



#SECTION 3____________________________________

#Raising Errors

# #aquarium
# aqua.add_animal(andy)

# #Atrium
# atri.add_animal(andy)

# #Terrarium
# terra.add_animal(barry)

# #water cage
# waterCage.add_animal(frita)

# #fly cage
# flyCage.add_animal(rayray)

# #land cage
# landCage.add_animal(barry)




