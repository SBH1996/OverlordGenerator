import random
choice = ''
print("-----US Military World War 2 Service Records Database-----")

while choice != 'q':
    print("\n[Search] Enter 1 to search the database.")
    print("[Quit] Enter q to quit the database.")
    choice = input("\nPlease Select an Option: ")
    print("-----------------------------------------------------")
    if choice == '1':


        phs = 0
        cln = input("Enter Last Name: ")
        cfn = input("Enter First Name: ")
        cage = int(input("Enter Age: "))
        cmon1 = int(input("Enter Digitized Birth Month (ex. 12): "))

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
        cday = int(input("Enter Digitized Birth Day (ex. 8): "))
        cht = input("Enter City: ")
        chs = input("Enter State: ")
        am1 = 1942
        am2 = 1945
        am3 = random.randint(am1,am2)
        cyear = am3 - cage

        tow1 = 1
        tow2 = 3
        tow3 = random.randint(tow1,tow2)
        if tow3 == 1:
            tow = ("Pacific Theater of War")
        if tow3 == 2:
            tow = ("European Theater of War")
        if tow3 == 3:
            tow = ("European Theater of War")

        print("\n||||||||||||||||||||||||||||||||||||||||")
        print("Processing user input...")
        print("Searching Database....")
        print("Service Record Discovered")
        print("Loading Service Record...")
        print("Service Record Loaded")
        print("\n----------------------------------------")
        print("|||||||__________________________|||||||")
        print("|||||||                          |||||||")
        print("|||||||US Military Service Record|||||||")
        print("|||||||__________________________|||||||")
        print("----------------------------------------")
        print("\nName: "+ cln + ", "+cfn)
        print("Date of Birth: ",cmon ,"-" ,cday,"-" , cyear)
        print("Place of Birth: ", cht + ", " + chs)

        a = 1
        b = 2
        c = random.randint(a,b)
        if c == 1:
            Branch = ("Army")
            a1 = 1
            b1 = 10
            c1 = random.randint(a1,b1)
            if c1 == 1:
                MOS = ("Infantry")
            if c1 == 2:
                MOS = ("Armor")
            if c1 == 3:
                MOS = ("Military Police")
            if c1 == 4:
                MOS = ("Artillery")
            if c1 == 5:
                MOS = ("Logistics")
            if c1 == 6:
                MOS = ("Army Corps of Engineers")
            if c1 == 7:
                MOS = ("Airborne")
            if c1 == 8:
                MOS = ("Reconnaissance")
            if c1 == 9:
                MOS = ("Special Operations")
            if c1 == 10:
                MOS = ("Intelligence")
            g = 1
            h = 11
            i = random.randint(g,h)
            if i == 1:
                grade = ("Private")
            if i == 2:
                grade = ("Private First Class")
            if i == 3:
                grade = ("Corporal")
            if i == 4:
                grade = ("Sergeant")
            if i == 5:
                grade = ("Staff Sergeant")
            if i == 6:
                grade = ("Technical Sergeant")
            if i == 7:
                grade = ("First Sergeant")
            if i == 8:
                grade = ("Master Sergeant")
            if i == 9:
                grade = ("2nd Lieutenant")
            if i == 10:
                grade = ("1st Lieutenant")
            if i == 11:
                grade = ("Captain")
            d = 1
            e = 44
            f = random.randint(d,e)
            if f == 1:
                stat = ("No Injuries")
            if f == 2:
                stat = ("Lightly Wounded - Non-Combat")
            if f == 3:
                stat = ("Moderately Wounded - Non-Combat")
            if f == 4:
                stat = ("Severely Wounded - Non-Combat")
            if f == 5:
                stat = ("Died of Injuries - Non-Combat")
            if f == 6:
                stat = ("Died in Unexpected Circumstances - Non-Combat")
            if f == 7:
                stat = ("Killed, Vehicular Crash - Non-Combat")
            if f == 8:
                stat = ("Killed, Plane Crash - Non-Combat")
            if f == 9:
                stat = ("Killed, Ship Loss - Non-Combat")
            if f == 10:
                stat = ("Killed, Accident - Non-Combat")
            if f == 11:
                stat = ("Died of Illness")
            if f == 12:
                stat = ("Missing in Action")
            if f == 13:
                stat = ("Lightly Wounded - Small-Arms Fire")
                phs = 1
            if f == 14:
                stat = ("Lightly Wounded - Shrapnel")
                phs = 1
            if f == 15:
                stat = ("Lightly Wounded - Indirect Fire")
                phs = 1
            if f == 16:
                stat = ("Lightly Wounded - Landmine/Explosion")
                phs = 1
            if f == 17:
                stat = ("Lightly Wounded - Melee Combat")
                phs = 1
            if f == 18:
                stat = ("Lightly Wounded - Vehicular Loss")
                phs = 1
            if f == 19:
                stat = ("Lightly Wounded - Aircraft Loss")
                phs = 1
            if f == 20:
                stat = ("Lightly Wounded - Ship Loss")
                phs = 1
            if f == 21:
                stat = ("Moderately Wounded - Small-Arms Fire")
                phs = 1
            if f == 22:
                stat = ("Moderately Wounded - Shrapnel")
                phs = 1
            if f == 23:
                stat = ("Moderately Wounded - Indirect Fire")
                phs = 1
            if f == 24:
                stat = ("Moderately Wounded - Landmine/Explosion")
                phs = 1
            if f == 25:
                stat = ("Moderately Wounded - Melee Combat")
                phs = 1
            if f == 26:
                stat = ("Moderately Wounded - Vehicular Loss")
                phs = 1
            if f == 27:
                stat = ("Moderately Wounded - Aircraft Loss")
                phs = 1
            if f == 28:
                stat = ("Moderately Wounded - Ship Loss")
                phs = 1
            if f == 29:
                stat = ("Severely Wounded - Small-Arms Fire")
                phs = 1
            if f == 30:
                stat = ("Severely Wounded - Shrapnel")
                phs = 1
            if f == 31:
                stat = ("Severely Wounded - Indirect Fire")
                phs = 1
            if f == 32:
                stat = ("Severely Wounded - Landmine/Explosion")
                phs = 1
            if f == 33:
                stat = ("Severely Wounded - Melee Combat")
                phs = 1
            if f == 34:
                stat = ("Severely Wounded - Vehicular Loss")
                phs = 1
            if f == 35:
                stat = ("Severely Wounded - Aircraft Loss")
                phs = 1
            if f == 36:
                stat = ("Severely Wounded - Ship Loss")
                phs = 1
            if f == 37:
                stat = ("Killed - Small-Arms Fire")
                phs = 1
            if f == 38:
                stat = ("Killed - Shrapnel")
                phs = 1
            if f == 39:
                stat = ("Killed - Indirect Fire")
                phs = 1
            if f == 40:
                stat = ("Killed - Landmine/Explosion")
                phs = 1
            if f == 41:
                stat = ("Killed - Melee Combat")
                phs = 1
            if f == 42:
                stat = ("Killed - Vehicular Loss")
                phs = 1
            if f == 43:
                stat = ("Killed - Aircraft Loss")
                phs = 1
            if f == 44:
                stat = ("Killed - Ship Loss")
                phs = 1


        if c == 2:
            Branch = ("Marine Corps")
            tow = ("Pacific Theater of War")
            a3 = 1
            b3 = 7
            c3 = random.randint(a3,b3)
            if c3 == 1:
                MOS = ("Infantry")
            if c3 == 2:
                MOS = ("Armor")
            if c3 == 3:
                MOS = ("Artillery")
            if c3 == 4:
                MOS = ("Special Operations")
            if c3 == 5:
                MOS = ("Support Personnel")
            if c3 == 6:
                MOS = ("Intelligence")
            if c3 == 7:
                MOS = ("Military Police")

            g1 = 1
            h1 = 11
            i1 = random.randint(g1,h1)
            if i1 == 1:
                grade = ("Private")
            if i1 == 2:
                grade = ("Private First Class")
            if i1 == 3:
                grade = ("Corporal")
            if i1 == 4:
                grade = ("Sergeant")
            if i1 == 5:
                grade = ("Staff Sergeant")
            if i1 == 6:
                grade = ("Gunnery Sergeant")
            if i1 == 7:
                grade = ("First Sergeant")
            if i1 == 8:
                grade = ("Master Gunnery Sergeant")
            if i1 == 9:
                grade = ("2nd Lieutenant")
            if i1 == 10:
                grade = ("1st Lieutenant")
            if i1 == 11:
                grade = ("Captain")

            d2 = 1
            e2 = 44
            f2 = random.randint(d2,e2)
            if f2 == 1:
                stat = ("No Injuries")
            if f2 == 2:
                stat = ("Lightly Wounded - Non-Combat")
            if f2 == 3:
                stat = ("Moderately Wounded - Non-Combat")
            if f2 == 4:
                stat = ("Severely Wounded - Non-Combat")
            if f2 == 5:
                stat = ("Died of Injuries - Non-Combat")
            if f2 == 6:
                stat = ("Died in Unexpected Circumstances - Non-Combat")
            if f2 == 7:
                stat = ("Killed, Vehicular Crash - Non-Combat")
            if f2 == 8:
                stat = ("Killed, Plane Crash - Non-Combat")
            if f2 == 9:
                stat = ("Killed, Ship Loss - Non-Combat")
            if f2 == 10:
                stat = ("Killed, Accident - Non-Combat")
            if f2 == 11:
                stat = ("Died of Illness")
            if f2 == 12:
                stat = ("Missing in Action")
            if f2 == 13:
                stat = ("Lightly Wounded - Small-Arms Fire")
                phs = 1
            if f2 == 14:
                stat = ("Lightly Wounded - Shrapnel")
                phs = 1
            if f2 == 15:
                stat = ("Lightly Wounded - Indirect Fire")
                phs = 1
            if f2 == 16:
                stat = ("Lightly Wounded - Landmine/Explosion")
                phs = 1
            if f2 == 17:
                stat = ("Lightly Wounded - Melee Combat")
                phs = 1
            if f2 == 18:
                stat = ("Lightly Wounded - Vehicular Loss")
                phs = 1
            if f2 == 19:
                stat = ("Lightly Wounded - Aircraft Loss")
                phs = 1
            if f2 == 20:
                stat = ("Lightly Wounded - Ship Loss")
                phs = 1
            if f2 == 21:
                stat = ("Moderately Wounded - Small-Arms Fire")
                phs = 1
            if f2 == 22:
                stat = ("Moderately Wounded - Shrapnel")
                phs = 1
            if f2 == 23:
                stat = ("Moderately Wounded - Indirect Fire")
                phs = 1
            if f2 == 24:
                stat = ("Moderately Wounded - Landmine/Explosion")
                phs = 1
            if f2 == 25:
                stat = ("Moderately Wounded - Melee Combat")
                phs = 1
            if f2 == 26:
                stat = ("Moderately Wounded - Vehicular Loss")
                phs = 1
            if f2 == 27:
                stat = ("Moderately Wounded - Aircraft Loss")
                phs = 1
            if f2 == 28:
                stat = ("Moderately Wounded - Ship Loss")
                phs = 1
            if f2 == 29:
                stat = ("Severely Wounded - Small-Arms Fire")
                phs = 1
            if f2 == 30:
                stat = ("Severely Wounded - Shrapnel")
                phs = 1
            if f2 == 31:
                stat = ("Severely Wounded - Indirect Fire")
                phs = 1
            if f2 == 32:
                stat = ("Severely Wounded - Landmine/Explosion")
                phs = 1
            if f2 == 33:
                stat = ("Severely Wounded - Melee Combat")
                phs = 1
            if f2 == 34:
                stat = ("Severely Wounded - Vehicular Loss")
                phs = 1
            if f2 == 35:
                stat = ("Severely Wounded - Aircraft Loss")
                phs = 1
            if f2 == 36:
                stat = ("Severely Wounded - Ship Loss")
                phs = 1
            if f2 == 37:
                stat = ("Killed - Small-Arms Fire")
                phs = 1
            if f2 == 38:
                stat = ("Killed - Shrapnel")
                phs = 1
            if f2 == 39:
                stat = ("Killed - Indirect Fire")
                phs = 1
            if f2 == 40:
                stat = ("Killed - Landmine/Explosion")
                phs = 1
            if f2 == 41:
                stat = ("Killed - Melee Combat")
                phs = 1
            if f2 == 42:
                stat = ("Killed - Vehicular Loss")
                phs = 1
            if f2 == 43:
                stat = ("Killed - Aircraft Loss")
                phs = 1
            if f2 == 44:
                stat = ("Killed - Ship Loss")
                phs = 1




        print("Branch of Service: ", Branch)
        print("Service Field: ", MOS)
        print("Rank: ", grade)
        print("Status: ", stat)
        print("Theater of War: ", tow)
        print("Year of Status Report: ", am3)

        mohc = 0
        mohb = 1
        moht = 35000
        mohr = random.randint(mohb,moht)
        if mohr == 15000:
            mohc = 1
            moh = ("the Medal of Honor")

        ssc = 0
        ssb = 1
        sst = 1200
        ssr = random.randint(ssb,sst)
        if ssr == 999:
            ssc = 1
            ssa = ("the Silver Star")

        ph = ("the Purple Heart")

        bsc = 0
        bsb = 1
        bst = 600
        bsr = random.randint(bsb,bst)
        if bsr == 300:
            bsc = 1
            bsa = ("the Bronze Star")

        print("\n----------------------------")
        print("------ Notable Awards ------")
        print("----------------------------")
        if mohc == 1:
            print("Awarded", moh)
        if ssc == 1:
            print("Awarded", ssa)
        if bsc == 1:
            print("Awarded", bsa)
        if phs == 1:
            print("Awarded", ph)
        if mohc == 0 and ssc == 0 and bsc ==0 and phs == 0:
            print("No Notable Awards")

        print("\n//////////End of Service Record//////////")

    elif choice == 'q':
        print("\nClosing Database Search Application.\n")
    else:
        print("\nInvalid Response, please enter either 1 or q.\n")
print("Thanks again, bye now.")
