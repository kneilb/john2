import time
input("WELCOME TO THE LOST FOREST press enter to continue")
name = input("Please enter your name:")
# game starts
print("You are visiting a forest in Ireland with your friend.")
print("You can take either:")
item = input("Badger slippers, Fishsticks or a Tame beaver.") # item question
print("You have arrived at the forest and are now walking to the lodge with your friend...")
time.sleep(3) # 3 sec pause
print(f'"Remember {name} we must not stray of the path!" He said.')
time.sleep(3)
print("A few seconds later and someone grabs you and pulls you of the path!")
time.sleep(4)
print('"If you give me fishsticks I will let you go!" He said...')
if item.lower() == "fishsticks":                                                          # badger slippers
    time.sleep(3)
    print("You give him the fishsticks and he lets you go but your friend is nowhere to be seen...")
    time.sleep(3)
    print("You are now lost in the forest.")
else:
    print("He traps you in a wooden cage wich is littered with skulls...")
    time.sleep(6)
    print("You notice a badger run past the cage and into a bush")
    if item.lower() == "badger slippers":                                         # badger
        print("The badger reappears and starts speaking to your badger slippers!")
        print('"Hey! I am going to break you out of here!"')
        print("The badger picks the lock using its claws and then the door swings open.")
        time.sleep(10)
        print("You walk around for a while before finding camp!")
        time.sleep(3)
        print("WELL DONE THANKS FOR PLAYING!!!")
    
    elif item.lower() == "tame beaver":                                      # tame beaver
        print("Your beaver chews open the door hinges and it swings open.")
        time.sleep(5)
        print("You walk around a bit then realise that you are still lost!")
        
        
        





