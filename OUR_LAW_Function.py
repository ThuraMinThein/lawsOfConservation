def Our_Law_Monmentum():
    choice=input("\nWanna know direct p answer or a basic answer?")
      
    if choice == "p answer":
        print("\nif the second object is at the rest please enter O in intial velocity of second object!")
        rt = True
        while rt == True:
            
            mA = float(input("\nEnter mass of first object: "))
            vA = float(input("Enter intial velocity of first object(first event):"))
            vA2 = float(input("Enter final velocity of first object(second event):"))

            mB = float(input("\nEnter mass of second object: "))
            vB = float(input("Enter intial velocity of second object(first event): "))
            vB2 = float(input("Enter final velocity of first object(second event): "))

            p1 = (mA * vA) + (mB * vB)
            p2 = (mA * vA2) + (mB * vB2)

            print("\nFirst event Total p" , p1)
            print("Second event Total p" , p2)

            if p1 == p2:
                print("\nBy the Law of Conseveration of Momentum,Total Monmentum of system is constant")
                rt = False

            elif p1 != p2:

                s1 = (mA * vA) + (mB * vB)
                s2 = s1 / (mA + mB)
                vA3 = s2
                vB3 = s2

                print("\nDear User! your input is incorrect. You should input final velcity for all second event:" , vB3)
                rt = True

    elif  choice == "basic answer":

        print("\nif the second object is at the rest please enter O in intial velocity of second object!")

        choice2 = input("\nwhich one do you want to know velocity of >intial< or >final< ")
        
        if choice2 == "intial":                                                       #find intial velocity
            choice3 = input("for first obj or second obj: ")
            
            if choice3 == "first obj":
                mA = float(input("\nEnter mass of first object: "))
                vA2 = float(input("Enter final velocity of first objcet (second event): "))

                mB = float(input("\nEnter mass of second object: "))
                vB = float(input("Enter intial velocity of second object(first event): "))
                vB2 = float(input("Enter final velocity of first object(second event): "))

                p1 = (mA * vA2) + (mB * vB2)
                p2 = p1 - (mB * vB)
                p3 = p2/ mA
                vA = p3

                print("Intial velocity is : " , vA)

                choice4 = input("Wanna find out Total momentum?  ")
                
                if choice4 == "yes":
                    s1 = (mA * vA) + (mB * vB)
                    s2 = (mA * vA2) + (mB * vB2)

                    print("\nFirst event Total p" , s1)
                    print("Second event Total p" , s2)

                    if s1 == s2:
                        print("\nBy the Law of Conseveration of Momentum,Total Monmentum of system is constant")

                    else:
                        print("\nPlease check your inputs!")

                elif choice4 == "no":
                    print("Thanks for using our program.")

            elif choice3 == "second obj": 

                mA = float(input("\nEnter mass of first object: "))
                vA = float(input("Enter intial velocity of first object(first event):"))
                vA2 = float(input("Enter final velocity of first object(second event):"))

                mB = float(input("\nEnter mass of second object: "))
                vB2 = float(input("Enter final velocity of first object(second event): "))

                p1 = (mA * vA2) + (mB * vB2)
                p2 = p1 - (mA * vA)
                p3 = p2 / mB
                vB = p3

                print("Intial velocity is : " , vB)

                choice4 = input("Wanna find out Total momentum?  ")

                if choice4 == "yes":
                    s1 = (mA * vA) + (mB * vB)
                    s2 = (mA * vA2) + (mB * vB2)

                    print("\nFirst event Total p" , s1)
                    print("Second event Total p" , s2)

                    if s1 == s2:
                        print("\nBy the Law of Conseveration of Momentum,Total Monmentum of system is constant")

                    else:
                        print("\nPlease check your inputs!")

                elif choice4 == "no":
                    print("Thanks for using our program.")                                          #find intial velocity

            else:
                print("Incorrect input")

        elif choice2 == "final":                                                                    #find final velocity
            mA = float(input("\nEnter mass of first object: "))
            vA = float(input("Enter intial velocity of first object(first event):"))
        
            mB = float(input("\nEnter mass of second object: "))
            vB = float(input("Enter intial velocity of second object(first event): "))

            p1 = (mA * vA) + (mB * vB)
            p2 = p1 / (mA + mB)
            vA2 = p2
            vB2 = p2

            print("Final velocity is : " , vB2)

            choice3= input("Wanna find out Total momentum?  ")

            if choice3 == "yes":
                s1 = (mA * vA) + (mB * vB)
                s2 = (mA + mB) * vA2

                print("\nFirst event Total p" , s1)
                print("Second event Total p" , s2)

                if s1 == s2:
                    print("\nBy the Law of Conseveration of Momentum,Total Monmentum of system is constant")

                else:
                    print("\nPlease check your inputs!")

            elif choice3 == "no":
                print("Thanks for using our program.")

        else:
            print("Incorrect input")

    else :
        print("U good......bro? cause it's not correct.Just choose the one which is in two choices dude!")

def Our_Law_Energy():

    def check():
        choice3 = input("\nWanna know E total answer more?")
        if choice3 =="yes":
                
            sq_vA = vA * vA
            sq_vB = vB * vB
            p1 = m * ((g * hA) + (0.5 * sq_vA))
            p2 = m * ((g * hB) + (0.5 * sq_vB))

            print("\nE total of first place: " , p1 , "\nE total of second place: " , p2)

            if p1 == p2:
                print("\nBy the law of conservation of Eneergy,E total must be constant.\n\nThanks for using our program...")

        elif choice3 =="no":
                print("Thank you...")

        else:
                print("Are you kidding me :( ")

    def Jpick():
        choice3 = input("\nWould you like to use this correct new value of the height of the first place to get the correct E total answer!")
        if choice3 =="yes":
                
            sq_vA = vA * vA
            sq_vB = vB * vB
            p1 = m * ((g * hA) + (0.5 * sq_vA))
            p2 = m * ((g * hB) + (0.5 * sq_vB))

            print("\nE total of first place: " , p1 , "\nE total of second place: " , p2)

            if p1 == p2:
                print("\nBy the law of conservation of Eneergy,E total must be constant.\n\nThanks for using our program...")

        elif choice3 =="no":
                print("Thank you...")

        else:
                print("Are you kidding me :( ")  

    print("\nEnergy required by a body due to its motion is called Kinetic energy.\n\nThe energy stored in a body due to its position or cofiguration is called the potential energy.\n\nIf the object is on the ground PE must be 0.")
    
    choice = input("Enter 'E total answer' or 'basic answer': ")
    ch1 = "E total answer"
    ch2 = "basic answer"
    if choice == ch1:

            m = float(input("\nEnter mass of the object: "))
            vA = float(input("Enter velocity of object at the first place: "))
            hA = float(input("Enter the height of the first place: "))

            vB = float(input("\nEnter the velocity of object at the second place: "))
            hB = float(input("Enter the height of the second place: "))
            g = 10
            print("Acceleration due to gravity" , g)
            sq_vA = vA * vA
            sq_vB = vB * vB

            p1 = m * ((g * hA) + (0.5 * sq_vA))
            p2 = m * ((g * hB) + (0.5 * sq_vB))

            print("\nE total of first place: " , p1 , "\nE total of second place: " , p2)

            if p1 == p2:
                print("\nBy the law of conservation of Eneergy,E total must be constant")

            else:
                sq_vA = vA * vA
                sq_vB = vB * vB
                
                s1 = sq_vB - sq_vA + (2*g*hB)
                s2 = s1 / (2 * g)
                hA = s2
                print("\nDear user your inputs are incorrect! Please input the value for velocity of the first place ss" , hA)
                Jpick()

    elif choice == ch2:

        print("\n'vA' for velocity of the first place.\n'hA' for the height of the first place.\n'vB' for velocity of the second place.\n'hB' for the height of the second place.\n")

        choice2 = input("Which one do you wanna know,please pick only one:")

        match choice2:

            case "vA" : 
                m = float(input("\nEnter mass of the object: "))
                hA = float(input("Enter the height of the first place: "))

                vB = float(input("\nEnter the velocity of object at the second place: "))
                hB = float(input("Enter the height of the second place: "))

                g = 10
                print("\nAcceleration due to gravity " , g)
                
                sq_vB = vB * vB
                s1 = (2 * g * hB) + sq_vB - (2 * g * hA)
                s2 = s1 ** 0.5
                vA = s2
                print("\nThe velocity of the first place: " , vA)
                check()                

            case "vB":
                m = float(input("\nEnter mass of the object: "))
                vA = float(input("Enter velocity of object at the first place: "))
                hA = float(input("Enter the height of the first place: "))

                hB = float(input("Enter the height of the second place: "))

                g =10
                print("\nAcceleration due to gravity ", g)
                sq_vA = vA * vA

                s1 = sq_vA - (2 * g * hB) + (2 * g * hA)
                s2 = s1 ** 0.5
                vB = s2
                print("\nThe velocity of the second place: " , vB)
                check()

            case "hA":
                m = float(input("\nEnter mass of the object: "))
                vA = float(input("Enter velocity of object at the first place: "))

                vB = float(input("\nEnter the velocity of object at the second place: "))
                hB = float(input("Enter the height of the second place: "))

                g = 10
                print("\nAcceleration due to gravity ", g)

                sq_vA = vA * vA
                sq_vB = vB * vB
                
                s1 = sq_vB - sq_vA + (2*g*hB)
                s2 = s1 / (2 * g)
                hA = s2
                print("The hight of the first place: " , hA)
                check()

            case "hB":
                m = float(input("\nEnter mass of the object: "))
                vA = float(input("Enter velocity of object at the first place: "))
                hA = float(input("Enter the height of the first place: "))

                vB = float(input("\nEnter the velocity of object at the second place: "))
                
                g = 10
                print("\nAcceleration due to gravity " ,g)

                sq_vA = vA * vA
                sq_vB = vB * vB

                s1 = sq_vA - sq_vB + (2*g*hA)
                s2 = s1 / (2 * g)
                hB = s2
                print("The height of the second place: " , hB)
                check()

    else:
        print("\nWhat on earth that are you just input :) just choose one which is in two choices!")

Our_Law_Energy()