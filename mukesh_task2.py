from statistics import mean  #importing mean from statistics module

def output(mukesh): 
    """This function receive the list of data that is stored in the mukesh list and perform some operation. 
    Finally it prints the output after the calculation."""
    max_km = max(mukesh)
    max_miles = max_km/1.61
    min_km = min(mukesh)
    min_miles = min_km/1.61
    avg_km = mean(mukesh)
    avg_miles  = avg_km /1.61 

    print("\nReading Summary\n")
    if len(mukesh) == 1: # it check the length of list if length is 1 the prints "Reading" else "Readings"
        print(len(mukesh) ," Reading Analysed\n")
    else:
        print(len(mukesh), " Readings Analysed\n")
        
    print("Max is {:.1f} MPH and {:.1f} KPH".format(max_miles,max_km))
    print("Min is {:.1f} MPH and {:.1f} KPH".format(min_miles,min_km))
    print("Avg is {:.1f} MPH and {:.1f} KPH".format(avg_miles,avg_km))

mukesh = []
print("\nSwallow Speed Analysis: Version 1.0\n")
while True: #it loops the program
    read = input("Enter the Next reading: ")
    if read == "":  #if input is nothing the it breaks the loop
        break
    elif read[0] == "U": #it check that "U" is in input or not
        mukesh.append(float(read[1:])*1.61)
        print("Reading Saved.")
    elif read[0] == "E": #it check that "E" is in input or not
        mukesh.append(float(read[1:]))
        print("Reading Saved.")
    else:
        print("invalid input")
    
if len(mukesh) == 0: # if the length of list called as mukesh
    print("No data Entered. Nothing to do.")
else: # if length of list is more then it calls the output function and pass the list 
    output(mukesh) 