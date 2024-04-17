from Cake import Cake
from coffeeCake import coffeeCake
from appleCake import appleCake
from coconutCake import coconutCake
from Instructions import Instructions

finallprint= lambda:print("see in next time...")
thiscake = ""
choose = "on"
canMakeACake = 1
while choose != "1":
    try:
        choose = input(f"Which cake do you want to bake? (coffee, coconut, apple). To exit press 1\n")
        if choose == "coffee" or choose == "coconut" or choose == "apple":
            if choose == "coffee":
                thiscake = coffeeCake()
            if choose == "coconut":
                thiscake = coconutCake()
            if choose == "apple":
                thiscake = appleCake()
            canMakeACake = thiscake.inventoryCheck()
            if canMakeACake == 0:
                break
            else:
                print("Excellent! Now you can make the cake")
                user_input=input("If you are interested in seeing a picture of the cake press 1, if you are interested in the audio guide press 2\n")
                try:
                    if user_input=='1' or user_input=='2':
                        if user_input=='1':
                            print_img = Instructions()
                            print_img.printimg(choose)
                            finallprint()
                        if user_input =='2':
                            void_guide=Instructions()
                            void_guide.instructions(choose)
                            print("seeing a picture of the cake")
                            void_guide.printimg(choose)
                            finallprint()
                    else:
                        print("The value you entered is incorrect, Try again")
                except:
                    print("The number entered is incorrect-(error 2)")
        else:
            print("The value you entered is incorrect, Try again")
    except:
        print("The input you entered is incorrect-(error 1)")

