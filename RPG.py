import random

cfn = input("Enter First Name: ")
cln = input("Enter Last Name: ")
cdob = input("Enter Age: ")
cht = input("Enter City: ")
chs = input("Enter State: ")
print("Processing user input...")
print("Searching Database....")
print("Service Record Discovered")
print("Loading Service Record...")
print("Service Record Loaded")
print("---------------------------------------")
print("-------US Military Service Record------")
print("---------------------------------------")
print("Name: ", cfn + " " + cln)
print("Date of Birth: ", cdob)
print("From: ", cht + ", " + chs)

a = 1
b = 6
c = random.randint(a,b)
if c == 1:
    Branch = ("Army")
    a1 = 1
    b1 = 4
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
        MOS = ("Administration")
    if c1 == 9:
        MOS = ("Reconnaissance")
    if c1 == 10:
        MOS = ("Special Operations")
    if c1 == 11:
        MOS = ("Intelligence")
    if c1 == 12:
        MOS = ("Air Corps")
    g = 1
    h = 14
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
    if i == 12:
        grade = ("Major")
    if i == 13:
        grade = ("Lieutenant Colonel")
    if i == 14:
        grade = ("Colonel")
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
    if f == 14:
        stat = ("Lightly Wounded - Shrapnel")
    if f == 15:
        stat = ("Lightly Wounded - Indirect Fire")
    if f == 16:
        stat = ("Lightly Wounded - Landmine/Explosion")
    if f == 17:
        stat = ("Lightly Wounded - Melee Combat")
    if f == 18:
        stat = ("Lightly Wounded - Vehicular Loss")
    if f == 19:
        stat = ("Lightly Wounded - Aircraft Loss")
    if f == 20:
        stat = ("Lightly Wounded - Ship Loss")
    if f == 21:
        stat = ("Moderately Wounded - Small-Arms Fire")
    if f == 22:
        stat = ("Moderately Wounded - Shrapnel")
    if f == 23:
        stat = ("Moderately Wounded - Indirect Fire")
    if f == 24:
        stat = ("Moderately Wounded - Landmine/Explosion")
    if f == 25:
        stat = ("Moderately Wounded - Melee Combat")
    if f == 26:
        stat = ("Moderately Wounded - Vehicular Loss")
    if f == 27:
        stat = ("Moderately Wounded - Aircraft Loss")
    if f == 28:
        stat = ("Moderately Wounded - Ship Loss")
    if f == 29:
        stat = ("Severely Wounded - Small-Arms Fire")
    if f == 30:
        stat = ("Severely Wounded - Shrapnel")
    if f == 31:
        stat = ("Severely Wounded - Indirect Fire")
    if f == 32:
        stat = ("Severely Wounded - Landmine/Explosion")
    if f == 33:
        stat = ("Severely Wounded - Melee Combat")
    if f == 34:
        stat = ("Severely Wounded - Vehicular Loss")
    if f == 35:
        stat = ("Severely Wounded - Aircraft Loss")
    if f == 36:
        stat = ("Severely Wounded - Ship Loss")
    if f == 37:
        stat = ("Killed - Small-Arms Fire")
    if f == 38:
        stat = ("Killed - Shrapnel")
    if f == 39:
        stat = ("Killed - Indirect Fire")
    if f == 40:
        stat = ("Killed - Landmine/Explosion")
    if f == 41:
        stat = ("Killed - Melee Combat")
    if f == 42:
        stat = ("Killed - Vehicular Loss")
    if f == 43:
        stat = ("Killed - Aircraft Loss")
    if f == 44:
        stat = ("Killed - Ship Loss")

if c == 2:
    Branch = ("Navy")
    a2 = 1
    b2 = 4
    c2 = random.randint(a2,b2)
    if c2 == 1:
        MOS = ("Assigned to Aircraft Carrier")
    if c2 == 2:
        MOS = ("Assigned to Battleship")
    if c2 == 3:
        MOS = ("Assigned to Cruiser")
    if c2 == 4:
        MOS = ("Assigned to Destroyer")
    if c2 == 5:
        MOS = ("Assigned to Submarine")
    g1 = 1
    h1 = 13
    i1 = random.randint(g1,h1)
    if i1 == 1:
        grade = ("Apprentice Seaman")
    if i1 == 2:
        grade = ("Seaman Second Class")
    if i1 == 3:
        grade = ("Seaman First Class")
    if i1 == 4:
        grade = ("Petty Officer Third Class")
    if i1 == 5:
        grade = ("Petty Officer Second Class")
    if i1 == 6:
        grade = ("Petty Officer First Class")
    if i1 == 7:
        grade = ("Chief Petty Officer")
    if i1 == 8:
        grade = ("Ensign")
    if i1 == 9:
        grade = ("Lieutenant Junior Grade")
    if i1 == 10:
        grade = ("Lieutenant")
    if i1 == 11:
        grade = ("Lieutenant Commander")
    if i1 == 12:
        grade = ("Commander")
    if i1 == 13:
        grade = ("Captain")
    d1 = 1
    e1 = 25
    f1 = random.randint(d1,e1)
    if f1 == 1:
        stat = ("No Injuries")
    if f1 == 2:
        stat = ("Lightly Wounded - Non-Combat")
    if f1 == 3:
        stat = ("Moderately Wounded - Non-Combat")
    if f1 == 4:
        stat = ("Severely Wounded - Non-Combat")
    if f1 == 5:
        stat = ("Died of Injuries - Non-Combat")
    if f1 == 6:
        stat = ("Died in Unexpected Circumstances - Non-Combat")
    if f1 == 7:
        stat = ("Killed, Vehicular Crash - Non-Combat")
    if f1 == 8:
        stat = ("Killed, Plane Crash - Non-Combat")
    if f1 == 9:
        stat = ("Killed, Ship Loss - Non-Combat")
    if f1 == 10:
        stat = ("Killed, Accident - Non-Combat")
    if f1 == 11:
        stat = ("Died of Illness")
    if f1 == 12:
        stat = ("Missing in Action")
    if f1 == 13:
        stat = ("Lost at Sea")
    if f1 == 14:
        stat = ("Lightly Wounded - Aircraft Attack")
    if f1 == 15:
        stat = ("Lightly Wounded - Ship Attack")
    if f1 == 16:
        stat = ("Lightly Wounded - Ship Loss")
    if f1 == 17:
        stat = ("Moderately Wounded - Aircraft Attack")
    if f1 == 18:
        stat = ("Moderately Wounded - Ship Attack")
    if f1 == 19:
        stat = ("Moderately Wounded - Ship Loss")
    if f1 == 20:
        stat = ("Severely Wounded - Aircraft Attack")
    if f1 == 21:
        stat = ("Severely Wounded - Ship Attack")
    if f1 == 22:
        stat = ("Severely Wounded - Ship Loss")
    if f1 == 23:
        stat = ("Killed - Aircraft Attack")
    if f1 == 24:
        stat = ("Killed - Ship Attack")
    if f1 == 25:
        stat = ("Killed - Ship Loss")
if c == 3:
    Branch = ("Marine Corps")
    a3 = 1
    b3 = 4
    c3 = random.randint(a3,b3)
    if c3 == 1:
        MOS = ("Infantry")
    if c3 == 2:
        MOS = ("Armor")
    if c3 == 3:
        MOS = ("Air Wing")
    if c3 == 4:
        MOS = ("Artillery")
    if c3 == 5:
        MOS = ("Special Operations")
    if c3 == 6:
        MOS = ("Administration")
    if c3 == 7:
        MOS = ("Logisitics")
    if c3 == 8:
        MOS = ("Support Personnel")
    if c3 == 9:
        MOS = ("Intelligence")
    if c3 == 10:
        MOS = ("Military Police")

    g1 = 1
    h1 = 14
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
        grade = ("Master Sergeant")
    if i1 == 9:
        grade = ("2nd Lieutenant")
    if i1 == 10:
        grade = ("1st Lieutenant")
    if i1 == 11:
        grade = ("Captain")
    if i1 == 12:
        grade = ("Major")
    if i1 == 13:
        grade = ("Lieutenant Colonel")
    if i1 == 14:
        grade = ("Colonel")
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
    if f2 == 14:
        stat = ("Lightly Wounded - Shrapnel")
    if f2 == 15:
        stat = ("Lightly Wounded - Indirect Fire")
    if f2 == 16:
        stat = ("Lightly Wounded - Landmine/Explosion")
    if f2 == 17:
        stat = ("Lightly Wounded - Melee Combat")
    if f2 == 18:
        stat = ("Lightly Wounded - Vehicular Loss")
    if f2 == 19:
        stat = ("Lightly Wounded - Aircraft Loss")
    if f2 == 20:
        stat = ("Lightly Wounded - Ship Loss")
    if f2 == 21:
        stat = ("Moderately Wounded - Small-Arms Fire")
    if f2 == 22:
        stat = ("Moderately Wounded - Shrapnel")
    if f2 == 23:
        stat = ("Moderately Wounded - Indirect Fire")
    if f2 == 24:
        stat = ("Moderately Wounded - Landmine/Explosion")
    if f2 == 25:
        stat = ("Moderately Wounded - Melee Combat")
    if f2 == 26:
        stat = ("Moderately Wounded - Vehicular Loss")
    if f2 == 27:
        stat = ("Moderately Wounded - Aircraft Loss")
    if f2 == 28:
        stat = ("Moderately Wounded - Ship Loss")
    if f2 == 29:
        stat = ("Severely Wounded - Small-Arms Fire")
    if f2 == 30:
        stat = ("Severely Wounded - Shrapnel")
    if f2 == 31:
        stat = ("Severely Wounded - Indirect Fire")
    if f2 == 32:
        stat = ("Severely Wounded - Landmine/Explosion")
    if f2 == 33:
        stat = ("Severely Wounded - Melee Combat")
    if f2 == 34:
        stat = ("Severely Wounded - Vehicular Loss")
    if f2 == 35:
        stat = ("Severely Wounded - Aircraft Loss")
    if f2 == 36:
        stat = ("Severely Wounded - Ship Loss")
    if f2 == 37:
        stat = ("Killed - Small-Arms Fire")
    if f2 == 38:
        stat = ("Killed - Shrapnel")
    if f2 == 39:
        stat = ("Killed - Indirect Fire")
    if f2 == 40:
        stat = ("Killed - Landmine/Explosion")
    if f2 == 41:
        stat = ("Killed - Melee Combat")
    if f2 == 42:
        stat = ("Killed - Vehicular Loss")
    if f2 == 43:
        stat = ("Killed - Aircraft Loss")
    if f2 == 44:
        stat = ("Killed - Ship Loss")

if c == 4:
    Branch = ("Marine Air Wing")
    MOS = "Aviation Crew/Pilot"
    ax = 1
    ay = 6
    ap = random.randint(ax,ay)
    if ap == 1:
        grade = ("Second Lieutenant")
    if ap == 2:
        grade = ("First Lieutenant")
    if ap == 3:
        grade = ("Captain")
    if ap == 4:
        grade = ("Major")
    if ap == 5:
        grade = ("Lieutenant Colonel")
    if ap == 6:
        grade = ("Colonel")
    d3 = 1
    e3 = 20
    f3 = random.randint(d3,e3)
    if f3 == 1:
        stat = ("No Injuries")
    if f3 == 2:
        stat = ("Lightly Wounded - Non-Combat")
    if f3 == 3:
        stat = ("Moderately Wounded - Non-Combat")
    if f3 == 4:
        stat = ("Severely Wounded - Non-Combat")
    if f3 == 5:
        stat = ("Died of Injuries - Non-Combat")
    if f3 == 6:
        stat = ("Died in Unexpected Circumstances - Non-Combat")
    if f3 == 7:
        stat = ("Killed, Vehicular Crash - Non-Combat")
    if f3 == 8:
        stat = ("Killed, Plane Crash - Non-Combat")
    if f3 == 9:
        stat = ("Killed, Ship Loss - Non-Combat")
    if f3 == 10:
        stat = ("Killed, Accident - Non-Combat")
    if f3 == 11:
        stat = ("Died of Illness")
    if f3 == 12:
        stat = ("Missing in Action")
    if f3 == 13:
        stat = ("Lightly Wounded - Aircraft Loss")
    if f3 == 14:
        stat = ("Lightly Wounded - Ship Loss")
    if f3 == 15:
        stat = ("Moderately Wounded - Aircraft Loss")
    if f3 == 16:
        stat = ("Moderately Wounded - Ship Loss")
    if f3 == 17:
        stat = ("Severely Wounded - Aircraft Loss")
    if f3 == 18:
        stat = ("Severely Wounded - Ship Loss")
    if f3 == 19:
        stat = ("Killed - Aircraft Loss")
    if f3 == 20:
        stat = ("Killed - Ship Loss")

if c == 5:
    Branch = ("Naval Aviation")
    MOS = "Aviation Crew/Pilot"
    ax1 = 1
    ay1 = 6
    ap1 = random.randint(ax1,ay1)
    if ap1 == 1:
        grade = ("Ensign")
    if ap1 == 2:
        grade = ("Lieutenant Junior Grade")
    if ap1 == 3:
        grade = ("Lieutenant")
    if ap1 == 4:
        grade = ("Lieutenant Commander")
    if ap1 == 5:
        grade = ("Commander")
    if ap1 == 6:
        grade = ("Captain")
    d4 = 1
    e4 = 20
    f4 = random.randint(d4,e4)
    if f4 == 1:
        stat = ("No Injuries")
    if f4 == 2:
        stat = ("Lightly Wounded - Non-Combat")
    if f4 == 3:
        stat = ("Moderately Wounded - Non-Combat")
    if f4 == 4:
        stat = ("Severely Wounded - Non-Combat")
    if f4 == 5:
        stat = ("Died of Injuries - Non-Combat")
    if f4 == 6:
        stat = ("Died in Unexpected Circumstances - Non-Combat")
    if f4 == 7:
        stat = ("Killed, Vehicular Crash - Non-Combat")
    if f4 == 8:
        stat = ("Killed, Plane Crash - Non-Combat")
    if f4 == 9:
        stat = ("Killed, Ship Loss - Non-Combat")
    if f4 == 10:
        stat = ("Killed, Accident - Non-Combat")
    if f4 == 11:
        stat = ("Died of Illness")
    if f4 == 12:
        stat = ("Missing in Action")
    if f4 == 13:
        stat = ("Lightly Wounded - Aircraft Loss")
    if f4 == 14:
        stat = ("Lightly Wounded - Ship Loss")
    if f4 == 15:
        stat = ("Moderately Wounded - Aircraft Loss")
    if f4 == 16:
        stat = ("Moderately Wounded - Ship Loss")
    if f4 == 17:
        stat = ("Severely Wounded - Aircraft Loss")
    if f4 == 18:
        stat = ("Severely Wounded - Ship Loss")
    if f4 == 19:
        stat = ("Killed - Aircraft Loss")
    if f4 == 20:
        stat = ("Killed - Ship Loss")
if c == 6:
    Branch = ("Army Air Corps")
    MOS = "Aviation Crew/Pilot"
    ax2 = 1
    ay2 = 10
    ap2 = random.randint(ax2,ay2)
    if ap2 == 1:
        grade = ("Technician Fifth Grade")
    if ap2 == 2:
        grade = ("Technician Fourth Grade")
    if ap2 == 3:
        grade = ("Technician Third Grade")
    if ap2 == 4:
        grade = ("Flight Officer")
    if ap2 == 5:
        grade = ("2nd Lieutenant")
    if ap2 == 6:
        grade = ("1st Lieutenant")
    if ap2 == 7:
        grade = ("Captain")
    if ap2 == 8:
        grade = ("Major")
    if ap2 == 9:
        grade = ("Lieutenant Colonel")
    if ap2 == 10:
        grade = ("Colonel")
    d5 = 1
    e5 = 20
    f5 = random.randint(d5,e5)
    if f5 == 1:
        stat = ("No Injuries")
    if f5 == 2:
        stat = ("Lightly Wounded - Non-Combat")
    if f5 == 3:
        stat = ("Moderately Wounded - Non-Combat")
    if f5 == 4:
        stat = ("Severely Wounded - Non-Combat")
    if f5 == 5:
        stat = ("Died of Injuries - Non-Combat")
    if f5 == 6:
        stat = ("Died in Unexpected Circumstances - Non-Combat")
    if f5 == 7:
        stat = ("Killed, Vehicular Crash - Non-Combat")
    if f5 == 8:
        stat = ("Killed, Plane Crash - Non-Combat")
    if f5 == 9:
        stat = ("Killed, Ship Loss - Non-Combat")
    if f5 == 10:
        stat = ("Killed, Accident - Non-Combat")
    if f5 == 11:
        stat = ("Died of Illness")
    if f5 == 12:
        stat = ("Missing in Action")
    if f5 == 13:
        stat = ("Lightly Wounded - Aircraft Loss")
    if f5 == 14:
        stat = ("Lightly Wounded - Ship Loss")
    if f5 == 15:
        stat = ("Moderately Wounded - Aircraft Loss")
    if f5 == 16:
        stat = ("Moderately Wounded - Ship Loss")
    if f5 == 17:
        stat = ("Severely Wounded - Aircraft Loss")
    if f5 == 18:
        stat = ("Severely Wounded - Ship Loss")
    if f5 == 19:
        stat = ("Killed - Aircraft Loss")
    if f5 == 20:
        stat = ("Killed - Ship Loss")

mohc = 0
mohb = 1
moht = 35000
mohr = random.randint(mohb,moht)
if mohr == 15000:
    mohc = 1
    moh = ("the Medal of Honor")

print("Branch of Service: ", Branch)
print("Service Field: ", MOS)
print("Rank: ", grade)
print("Status: ", stat)
if mohc == 1:
    print("Awarded ", moh)
