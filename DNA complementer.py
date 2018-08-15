resp = "y"
c = "n"
while resp == "y":
        print("\n")
        inp = list(input("Please enter the DNA sequence: "))
        ran = []
        for i in inp:
                if i == "G" or i == "g":
                        ran.append("C")
                elif i == "C" or i == "c":
                        ran.append("G")
                elif i == "A" or i == "a":
                        ran.append("T")
                elif i == "T" or i == "t":
                        ran.append("A")
                else:
                        ran.append("?")
                        c = "y"

        if c == "n":
                print (''.join(ran))
        elif c == "y":
                print("\n")
                print ("You have entered an unrecognized base. The program has complemented the recognizable base and replaced the unrecognizable base with a '?' \n")
                print (''.join(ran))
        resp = input("Do you want to use the complementer again? (y/n): ")
        
a = input("Please copy your complement sequence and press enter to abort the program.")
