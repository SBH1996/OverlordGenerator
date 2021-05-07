import random
choice = ''
print("-----What would you be in Medieval Europe?-----")

while choice != 'q':
    print("\n[Search] Enter 1 to play the game!.")
    print("[Quit] Enter q to quit the game :( .")
    choice = input("\nPlease Select an Option: ")
    print("-----------------------------------------------------")
    if choice == '1':


        phs = 0
        cln = input("Enter Last Name:")
        cfn = input("Enter First Name:")
        cage = int(input("Enter Age:"))
        cmon1 = int(input("Enter Digitized Birth Month (ex. 12):"))

        if cmon1 == 1:
            cmon = ("January")
        if cmon1 == 2:
            cmon = ("February")
        if cmon1 == 3:
            cmon = ("March")
        if cmon1 == 4:
            cmon = ("April")
        if cmon1 == 5:
            cmon = ("May")
        if cmon1 == 6:
            cmon = ("June")
        if cmon1 == 7:
            cmon = ("July")
        if cmon1 == 8:
            cmon = ("August")
        if cmon1 == 9:
            cmon = ("September")
        if cmon1 == 10:
            cmon = ("October")
        if cmon1 == 11:
            cmon = ("November")
        if cmon1 == 12:
            cmon = ("December")
        cday = int(input("Enter Digitized Birth Day (ex. 8):"))
        am1 = 1000
        am2 = 1500
        am3 = random.randint(am1,am2)
        cyear = am3 - cage

        occ = ""


        co1 = 1
        co2 = 4
        co3 = random.randint(co1,co2)
        if co3 == 1:
            occ = ("tavern worker")
        if co3 == 2:
            occ = ("town guardsman")
        if co3 == 3:
            occ = ("member of a mercenary company")
        if co3 == 4:
            occ = ("hunter")

        cast1 = 1
        cast2 = 5
        castr = random.randint(cast1,cast2)

        if castr == 1:
            cast = ("High Royalty")
        if castr == 2:
            cast = ("Royalty")
        if castr == 3:
            cast = ("Low Royalty")
        if castr == 4:
            cast = ("Peasantry")
            po1 = 1
            po2 = 4
            po3 = random.randint(po1,po2)
            if po3 == 1:
                occ = ("farmer.")
            if po3 == 2:
                occ = ("blacksmith.")
            if po3 == 3:
                occ = ("member of the local militia.")
            if po3 == 4:
                occ = ("bandit.")
        if castr == 5:
            cast = ("Peasantry")
            po1 = 1
            po2 = 4
            po3 = random.randint(po1,po2)
            if po3 == 1:
                occ = ("farmer.")
            if po3 == 2:
                occ = ("blacksmith.")
            if po3 == 3:
                occ = ("member of the local militia.")
            if po3 == 4:
                occ = ("bandit.")
        if castr == 6:
            cast = ("Peasantry")
            po1 = 1
            po2 = 4
            po3 = random.randint(po1,po2)
            if po3 == 1:
                occ = ("farmer.")
            if po3 == 2:
                occ = ("blacksmith.")
            if po3 == 3:
                occ = ("member of the local militia.")
            if po3 == 4:
                occ = ("bandit.")
        if castr == 7:
            cast = ("Peasantry")
            po1 = 1
            po2 = 4
            po3 = random.randint(po1,po2)
            if po3 == 1:
                occ = ("farmer.")
            if po3 == 2:
                occ = ("blacksmith.")
            if po3 == 3:
                occ = ("member of the local militia.")
            if po3 == 4:
                occ = ("bandit.")
        if castr == 8:
            cast = ("Peasantry")
            po1 = 1
            po2 = 4
            po3 = random.randint(po1,po2)
            if po3 == 1:
                occ = ("farmer.")
            if po3 == 2:
                occ = ("blacksmith.")
            if po3 == 3:
                occ = ("member of the local militia.")
            if po3 == 4:
                occ = ("bandit.")
        if castr == 9:
            cast = ("Peasantry")
            po1 = 1
            po2 = 4
            po3 = random.randint(po1,po2)
            if po3 == 1:
                occ = ("farmer.")
            if po3 == 2:
                occ = ("blacksmith.")
            if po3 == 3:
                occ = ("member of the local militia.")
            if po3 == 4:
                occ = ("bandit.")
        if castr == 10:
            cast = ("Peasantry")
            po1 = 1
            po2 = 4
            po3 = random.randint(po1,po2)
            if po3 == 1:
                occ = ("farmer.")
            if po3 == 2:
                occ = ("blacksmith.")
            if po3 == 3:
                occ = ("member of the local militia.")
            if po3 == 4:
                occ = ("bandit.")
        if castr == 11:
            cast = ("Citizenry")
        if castr == 12:
            cast = ("Citizenry")
        if castr == 13:
            cast = ("Citizenry")
        if castr == 14:
            cast = ("Merchantry")
        if castr == 15:
            cast = ("Merchantry")
        if castr == 16:
            cast = ("Lower Nobility")
        if castr == 17:
            cast = ("Lower Nobility")
        if castr == 18:
            cast = ("Upper Nobility")




        print("You were born on", cmon, cday, "in the year of our Lord", am3)
        print("Your parents were of the", cast, ("class"))
        print("Your father was a", occ,(" He did the best he could to provide for the family"))



    elif choice == 'q':
        print("\nThanks for playing!.\n")
    else:
        print("\nPlease repeat that my lord? I didn't understand, sire...\n")
print("Thanks again, bye now.")
