print("Stop! Who would cross the Bridge of Death\nMust answer me these questions three, 'ere the other side he see.\n")
name = input("What is your name? ")
if "Arthur" in name or "arthur" in name: # it check the arthur in name or not
    print("You may pass!")
else:
    quets = input("What is your quets? ")
    if "Grail" in quets or "grail" in quets: # it check grail in quest or not
        color = input("What is your favorit color? ")
        #comprehensing the else if statement and checking the first character of name and color
        print("You may pass!" if color[0].capitalize() == name[0].capitalize() else "Incorrect! You must now face the Gorge of Eternal Peril.") 
    else:
        print("Only those who has grail may pass!")