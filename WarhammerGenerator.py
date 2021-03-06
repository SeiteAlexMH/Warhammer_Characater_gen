#WarhammerGenerator.py
#Alexandre Seite
import random
Stats_description = ['Weapon Skill: ', 'Ballistic Skill: ', 'Strength: ', 'Toughness: ',
					 'Initiative: ', 'Agility: ', 'Dexterity: ', 'Intelligence: ', 'Willpower: ', 
					 'Fellowship: ', 'Wounds: ', 'Fate: ', 'Resilliance: ', 'Extra points: ', 'Movement: ']

race_list = ['Human   ','Dwarf   ','Halfling','High Elf','Wood Elf']

init_height = [57,51,36,71,71]
height_dice = [2,1,1,1,1]

init_age = [15,15,15,30,30]
age_dice = [1,10,5,10,10]

Stats_tables = [[20,20,20,20,20,20,20,20,20,20,2,1,3,4],
				[30,20,20,30,20,10,30,20,40,10,0,2,2,3],
				[10,30,10,20,20,20,30,20,30,30,0,2,3,3],
				[30,30,20,20,40,30,30,30,30,20,0,0,2,5],
				[30,30,20,20,40,30,30,30,30,20,0,0,2,5]]

EyeHairIndeces = [0,1,2,3,3,3,4,4,4,4,5,5,5,6,6,6,7,8,9]

Hair_tables = [['White Blond   ','Golden Blond  ','Red Blond     ','Golden Brown  ','Light Brown   ','Dark Brown    ','Black         ','Auburn        ','Red           ','Grey          '],
			   ['White         ','Grey          ','Pale Blond    ','Golden        ','Copper        ','Bronze        ','Brown         ','Dark Brown    ','Reddish Brown ','Black         '],
			   ['Grey          ','Flaxen        ','Russet        ','Honey         ','Chessnut      ','Ginger        ','Mustard       ','Almond        ','Chocolate     ','Liquorice     '],
			   ['Silver        ','White         ','Pale Blond    ','Blond         ','Yellow Blond  ','Copper Blond  ','Red Blond     ','Auburn        ','Red           ','Black         '],
			   ['Birch Silver  ','Ash Blond     ','Rose Gold     ','Honey Blond   ','Brown         ','Mahogany Brown','Dark Brown    ','Sienna        ','Ebony         ','Blue-Black    ']]
			    
Eye_tables = [['Free Choice','Green      ','Pale Blue  ','Blue       ','Pale Grey  ','Grey       ','Brown      ','Hazel      ','Dark Brown ','Black      '],
			  ['Coal       ','Lead       ','Steel      ','Blue       ','Earth Brown','Dark Brown ','Hazel      ','Green      ','Copper     ','Gold       '],
			  ['Light Gray ','Grey       ','Pale Blue  ','Blue       ','Green      ','Hazel      ','Brown      ','Copper     ','Dark Brown ','Dark Brown '],
			  ['Jet        ','Amethyst   ','Aquamarine ','Sapphire   ','Turquoise  ','Emerald    ','Amber      ','Copper     ','Citrine    ','Gold       '],
			  ['Ivory      ','Charcoal   ','Ivy Green  ','Mossy Green','Chessnut   ','Chessnut   ','Dark Brown ','Tan        ','Sandy Brown','Violet     ']]


Class_table = ['Academics','Burghers ','Courtiers','Peasants ','Rangers  ','Riverfolk','Rogues   ','Warriors ']

Class_trapings = [['Clothing','Dagger','Pouch','Sling Bag','Writing Kit'],# Roll for sheets of parchements
				  ['Cloak','Clothing','Dagger','Hat','Pouch','Sling Bag','Lunch'],
				  ['Courtley Garb','Dagger','Pouch','Tweezers','Ear Pick','Comb'],
				  ['Cloak','Clothing','Dagger','Pouch','Sling Bag','Rations (1 day)'],
				  ['Cloak','Clothing','Dagger','Pouch','Backpack','Tinderbox','Blanket','Rations (1 day)'],
				  ['Cloak','Clothing','Dagger','Pouch','Sling Bag','Flask of Spirits'],
				  ['Clothing','Dagger','Pouch','Sling Bag','2 Candles'],# Roll for Matches and Mask or Hood
				  ['Clothing','Hand Weapon','Dagger','Pouch']]
				  
# 14 Characters for Careers
Career_table = ['Apothecary    ','Engineer      ','Lawyer        ','Nun           ','Physician     ','Priest        ','Scholar       ','Wizard        ',
				'Agitator      ','Artisan       ','Beggar        ','Investigator  ','Merchant      ','Rat Catcher   ','Townsman      ','Watchman      ',
				'Advisor       ','Artist        ','Duelist       ','Envoy         ','Noble         ','Servant       ','Spy           ','Warden        ',
				'Bailiff       ','Hedge Witch   ','Herbalist     ','Hunter        ','Miner         ','Mystic        ','Scout         ','Villager      ',
				'Bounty Hunter ','Coachman      ','Entertainer   ','Flagellant    ','Messenger     ','Pedlar        ','Road Warden   ','Witch Hunter  ',
				'Boatman       ','Huffer        ','Riverwarden   ','Riverwoman    ','Seaman        ','Smuggler      ','Stevedore     ','Wrecker       ',
				'Bawd          ','Charlatan     ','Fence         ','Grave Robber  ','Outlaw        ','Rackteer      ','Thief         ','Witch         ',
				'Cavalryman    ','Guard         ','Knight        ','Pit Fighter   ','Protagonist   ','Soldier       ','Slayer        ','Warrior Priest']

career_path_list = [("Apothecary's Apprentice",'Brass 3 '),("Student Engineer",'Brass 4 '),("Student Lawyer",'Brass 4 '),("Novitiate",'Brass 1 '),("Physician's Apprentice",'Brass 4 '),("Initiate",'Brass 2 '),("Student",'Brass 3 '),("Wizard's Apprentice",'Brass 3 '),
					("Pamphleteer",'Brass 1 '),("Apprentice Artisan",'Brass 2 '),("Pauper",'Brass 0 '),("Sleuth",'Silver 1'),("Trader",'Silver 2'),("Rat Hunter",'Brass 3 '),("Clerk",'Silver 1'),("Watch Recruit",'Brass 3 '),
					("Aide",'Silver 2'),("Apprentice Artist",'Silver 1'),("Fencer",'Silver 3'),("Herald",'Silver 2'),("Scion",'Gold 1  '),("Menial",'Silver 1'),("Informer",'Brass 3 '),("Custodian",'Silver 1'),
					("Tax Collector",'Silver 1'),("Hedge Apprentice",'Brass 1 '),("Herb Gatherer",'Brass 2 '),("Trapper",'Brass 2 '),("Prospector",'Brass 2 '),("Fortune Teller",'Brass 1 '),("Guide",'Brass 3 '),("Peasant",'Brass 2 '),
					("Thief-taker",'Silver 1'),("Postilion",'Silver 1'),("Busker",'Brass 3 '),("Zealot",'Brass 0 '),("Runner",'Brass 3 '),("Pedlar",'Brass 1 '),("Toll Keeper",' Brass 5 '),("Interrogator",'Silver 1'),
					("Boat-hand",'Silver 1'),("Riverguide",'Brass 4 '),("River Recruit",'Silver 1'),("Greenfish",'Brass 2 '),("Landsman",'Silver 1'),("River Runner",'Brass 2 '),("Dockhand",'Brass 3 '),("Cargo Scavenger",'Brass 2 '),
					("Hustler",'Brass 1 '),("Swindler",'Brass 3 '),("Broker",'Silver 1'),("Grave Robber",'Brass 2 '),("Brigand",'Brass 1 '),("Thug",'Brass 3'),("Prowler",'Brass 1 '),("Hexer",'Brass 1 '),
					("Horseman",'Silver 2'),("Sentry",'Silver 1'),("Squire",'Silver 3'),("Pugilist",'Brass 4 '),("Braggart",'Brass 2 '),("Recruit",'Silver 1'),("Troll Slayer",'Brass 2 '),("Novitiate",'Brass 2 ')]

career_path_dict = dict(zip(Career_table,career_path_list))

HumanCareerCoord = [[0,0],[0,1],[0,2],[0,3],[0,3],[0,4],[0,5],[0,5],[0,5],[0,5],[0,5],[0,6],[0,6],[0,7],[1,8],[1,9],[1,9],[1,10],[1,10],[1,11],[1,12],[1,13],[1,13],[1,14],[1,14],
					[1,14],[1,15],[2,16],[2,17],[2,18],[2,19],[2,20],[2,21],[2,21],[2,21],[2,22],[2,23],[3,24],[3,25],[3,26],[3,27],[3,27],[3,28],[3,29],[3,30],[3,31],[3,31],[3,31],[3,31],[3,31],
					[4,32],[4,33],[4,34],[4,34],[4,35],[4,35],[4,36],[4,37],[4,38],[4,39],[5,40],[5,40],[5,41],[5,42],[5,42],[5,43],[5,43],[5,43],[5,44],[5,44],[5,45],[5,46],[5,46],[5,47],[6,48],
					[6,48],[6,49],[6,50],[6,51],[6,52],[6,52],[6,52],[6,52],[6,53],[6,54],[6,54],[6,54],[6,55],[7,56],[7,56],[7,57],[7,57],[7,58],[7,59],[7,60],[7,61],[7,61],[7,61],[7,61],[7,63]]

DwarfCareerCoord = [[0,0],[0,1],[0,1],[0,1],[0,2],[0,2],[0,4],[0,6],[0,6],[1,8],[1,8],[1,9],[1,9],[1,9],[1,9],[1,9],[1,9],[1,10],[1,11],[1,11],[1,12],[1,12],[1,12],[1,12],[1,13],
					[1,14],[1,14],[1,14],[1,14],[1,14],[1,14],[1,15],[1,15],[1,15],[2,16],[2,16],[2,17],[2,18],[2,19],[2,19],[2,20],[2,21],[2,22],[2,23],[2,23],[3,24],[3,24],[3,27],[3,27],[3,28],
					[3,28],[3,28],[3,28],[3,28],[3,30],[3,31],[4,32],[4,32],[4,32],[4,32],[4,33],[4,34],[4,34],[4,36],[4,36],[4,37],[4,37],[5,40],[5,40],[5,41],[5,43],[5,43],[5,44],[5,45],[5,45],
					[5,46],[5,46],[5,47],[6,50],[6,52],[6,52],[6,52],[6,53],[6,54],[7,57],[7,57],[7,57],[7,59],[7,59],[7,59],[7,60],[7,60],[7,60],[7,61],[7,61],[7,61],[7,62],[7,62],[7,62],[7,62]]

HaflingCareerCoord = [[0,0],[0,1],[0,2],[0,2],[0,4],[0,4],[0,6],[0,6],[1,8],[1,8],[1,9],[1,9],[1,9],[1,9],[1,9],[1,10],[1,10],[1,10],[1,10],[1,11],[1,11],[1,12],[1,12],[1,12],[1,12],
					  [1,13],[1,13],[1,13],[1,14],[1,14],[1,14],[1,15],[1,15],[2,16],[2,17],[2,17],[2,19],[2,21],[2,21],[2,21],[2,21],[2,21],[2,21],[2,22],[2,23],[2,23],[3,24],[3,26],[3,26],[3,26],
					  [3,27],[3,27],[3,28],[3,30],[3,31],[3,31],[3,31],[4,32],[4,33],[4,33],[4,34],[4,34],[4,34],[4,36],[4,36],[4,37],[4,37],[4,38],[5,40],[5,41],[5,42],[5,43],[5,43],[5,43],[5,44],
					  [5,45],[5,45],[5,45],[5,45],[5,46],[5,46],[5,46],[6,48],[6,48],[6,48],[6,49],[6,50],[6,51],[6,52],[6,53],[6,54],[6,54],[6,54],[6,54],[7,57],[7,57],[7,59],[7,61],[7,61],[7,61]]

HighElfCareerCoord = [[0,0],[0,0],[0,2],[0,2],[0,2],[0,2],[0,4],[0,4],[0,6],[0,6],[0,6],[0,6],[0,7],[0,7],[0,7],[0,7],[1,9],[1,9],[1,9],[1,11],[1,11],[1,12],[1,12],[1,12],[1,12],
					  [1,12],[1,14],[1,14],[1,15],[2,16],[2,16],[2,17],[2,18],[2,18],[2,19],[2,19],[2,19],[2,20],[2,20],[2,20],[2,22],[2,22],[2,22],[2,23],[2,23],[3,26],[3,26],[3,27],[3,27],[3,27],
					  [3,30],[3,30],[3,30],[3,30],[3,30],[3,30],[4,32],[4,32],[4,32],[4,34],[4,34],[4,34],[4,36],[5,40],[5,44],[5,44],[5,44],[5,44],[5,44],[5,44],[5,44],[5,44],[5,44],[5,44],[5,44],
					  [5,44],[5,44],[5,44],[5,44],[5,45],[6,48],[6,48],[6,49],[6,49],[6,49],[6,52],[6,52],[6,52],[7,56],[7,56],[7,56],[7,56],[7,57],[7,57],[7,58],[7,59],[7,59],[7,60],[7,61],[7,61]]

WoodElfCareerCoord = [[0,6],[0,7],[0,7],[0,7],[0,7],[1,9],[1,9],[1,9],[1,9],[1,9],[2,16],[2,16],[2,16],[2,16],[2,17],[2,17],[2,17],[2,17],[2,19],[2,19],[2,19],[2,19],[2,19],[2,19],[2,19],
					  [2,20],[2,20],[2,20],[2,20],[2,20],[2,20],[2,22],[2,22],[2,22],[2,22],[3,26],[3,26],[3,26],[3,26],[3,26],[3,26],[3,26],[3,27],[3,27],[3,27],[3,27],[3,27],[3,27],[3,27],[3,27],
					  [3,27],[3,27],[3,29],[3,29],[3,29],[3,29],[3,29],[3,30],[3,30],[3,30],[3,30],[3,30],[3,30],[3,30],[3,30],[3,30],[3,30],[3,30],[4,32],[4,32],[4,34],[4,34],[4,34],[4,34],[4,34],
					  [4,36],[4,36],[4,36],[5,47],[6,52],[6,52],[6,52],[6,52],[6,52],[6,52],[7,56],[7,56],[7,56],[7,56],[7,56],[7,57],[7,57],[7,58],[7,58],[7,59],[7,59],[7,61],[7,61],[7,61],[7,61]]

HumanTraitTable = ['Acute Sense(any)','Ambidextrous','Animal Affinity','artistic','Attractive','Coolheaded','Craftsman (any one)','Flee!','Hardy','Lightning Reflex','Linguistics','Luck','Marksman','Mimic','Night Vision','Nimble Fingered',
				   'Noble Blood','Orientation','Perfect Pitch','Pure Soul','Read/Write','Resistance (any one)','Savvy','Sharp','Sixth Sense','Strong Legs','Sturdy','Suave','Super Numerate','Very Resilient','Very Strong','Warrior Strong']

HumanTraitIndeces = [0,0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,11,11,11,11,12,12,12,13,13,13,14,14,14,15,15,15,
					 16,16,17,17,17,18,18,18,19,19,19,19,20,20,20,21,21,21,22,22,22,23,23,23,24,24,24,24,25,25,25,26,26,26,27,27,27,28,28,28,28,29,29,29,30,30,30,31,31,31]

class Character:
	raceIndex = 0
	race = ''
	name = ''
	Character_Stats = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	strength_bonus = 0
	tough_bonus = 0
	will_bonus = 0
	Age = 0
	Hair = ''
	heigth = 0
	height_str = ''
	Eyes = ''
	Career = ''
	charClass = ''
	charTalents = []
	charTrappings = []

def Generate_stats():
	c = Character()
	#Determining race, career and age
	careerScore = random.randint(0,99)
	race = random.randint(1,100)
	#Hardcode value here for specific race
	#+race = 90
	#careerScore = 77
	if race <= 90:
		set_race(c,0)
		c.charClass = Class_table[HumanCareerCoord[careerScore][0]]
		c.Career = Career_table[HumanCareerCoord[careerScore][1]]
		#get_trappings(HumanCareerCoord[careerScore][0])
		print("Human character")
	elif race <= 94:
		set_race(c,1)
		c.charClass = Class_table[DwarfCareerCoord[careerScore][0]]
		c.Career = Career_table[DwarfCareerCoord[careerScore][1]]
		#get_trappings(DwarfCareerCoord[careerScore][0])
		print("Dwarf character")
	elif race <= 98:
		set_race(c,2)
		c.charClass = Class_table[HaflingCareerCoord[careerScore][0]]
		c.Career = Career_table[HaflingCareerCoord[careerScore][1]]
		#get_trappings(HaflingCareerCoord[careerScore][0])
		print("Halfling character")
	elif race == 99:
		set_race(c,3)
		c.charClass = Class_table[HighElfCareerCoord[careerScore][0]]
		c.Career = Career_table[HighElfCareerCoord[careerScore][1]]
		#get_trappings(HighElfCareerCoord[careerScore][0])
		print("High Elf character")
	elif race == 100:
		set_race(c,4)
		c.charClass = Class_table[WoodElfCareerCoord[careerScore][0]]
		c.Career = Career_table[WoodElfCareerCoord[careerScore][1]]
		#get_trappings(WoodElfCareerCoord[careerScore][0])
		print("Wood Elf character")
	else:
		print("error?")

	c.name = input('character name? ').title()

	c.height_str = '{}\'{}"'.format(str(c.height//12),str(c.height%12))
	if len(c.height_str)<5:
		c.height_str+=' '

	#Generating character's stats
	for value in range(0,10):
		c.Character_Stats[value] = Stats_tables[c.raceIndex][value] + random.randint(1,10) +random.randint(1,10)
	for value in range(10,14):
		c.Character_Stats[value+1] = Stats_tables[c.raceIndex][value]
	
	#Determining stat bonus for health calc	
	c.strength_bonus = str(c.Character_Stats[2])[0]
	c.tough_bonus = str(c.Character_Stats[3])[0]
	c.will_bonus = str(c.Character_Stats[8])[0]
	
	#Health calculation
	if c.raceIndex == 2:
		c.Character_Stats[10] = 2*int(c.tough_bonus) + int(c.will_bonus)
	else:
		c.Character_Stats[10] = int(c.strength_bonus) + 2*int(c.tough_bonus) + int(c.will_bonus)
	
	#Allocating extra points to fate and resolve
	fate = int(input("you have " + str(c.Character_Stats[13]) + " extra points. How many should go to your fate? "))
	
	while fate > c.Character_Stats[13] or fate < 0:
		fate = int(input("Incorrect value! input cannot be negative or exceed " +str(c.Character_Stats[13]) + ": "))
		
	c.Character_Stats[11] += fate
	c.Character_Stats[12] += c.Character_Stats[13]-fate
	
	#rolling random hair and eye colours
	Roll= random.randint(1,10) + random.randint(1,10) - 2
	if c.raceIndex == 0 and Roll == 0:
		print('Free choice! choose one of the following:')
		print('1: Green, 2: Pale Blue, 3: Blue, 4: Pale Grey, 5: Grey, 6: Brown, 7: Hazel, 8: Dark Brown, 9: Black')
		Roll = int(input(''))
		c.Eyes = Eye_tables[c.raceIndex][Roll]
	else:
		c.Eyes = Eye_tables[c.raceIndex][EyeHairIndeces[Roll]]
	Roll= random.randint(1,10) + random.randint(1,10) - 2
	c.Hair = Hair_tables[c.raceIndex][EyeHairIndeces[Roll]]
	
	#Printing out stats for testing.
	for value in range(0,15):
		print(Stats_description[value] +str(c.Character_Stats[value]))
	print('Walk: ' + str(c.Character_Stats[14]*2))
	print('Run: ' + str(c.Character_Stats[14]*4))
	print('Age: ' + str(c.Age))
	print('Eye colour: ' + c.Eyes)
	print('Hair Colour: ' + c.Hair)
	print(c.charClass +' : '+ c.Career)
	#print(charTrappings)
	print_char(c)

def set_race(char,r_index):
	char.raceIndex = r_index
	char.race = race_list[r_index]
	char.height = init_height[r_index]
	for i in range(0,height_dice[r_index]):
		char.height += random.randint(1,10)
	char.Age = init_age[r_index]
	for value in range(0,age_dice[r_index]):
		char.Age += random.randint(1,10)

def get_trappings(careerIndex):
	for trappings in Class_trapings[careerIndex]:
		charTrappings.append(trappings)
	if careerIndex == 0:
		charTrappings.append(str(random.randint(1,10))+' Sheets of Parchement')
	if careerIndex == 6:
		charTrappings.append(str(random.randint(1,10))+' Matches')
		charTrappings.append(input('Choose one: Hood or Mask (type choice) '))

def print_char(char):
	blank = open('sheet2.txt','r')
	new_sheet = open('{}.txt'.format(char.name),'w')
	for i in range(0,7):
		new_sheet.write(blank.readline())
	new_sheet.write(blank.readline().format(char.name + ' '*(53-len(char.name)),char.race,char.charClass))
	new_sheet.write(blank.readline())
	new_sheet.write(blank.readline().format(char.Career))
	new_sheet.write(blank.readline())
	new_sheet.write(blank.readline().format(career_path_dict.get(char.Career)[0]+' '*(23-len(career_path_dict.get(char.Career)[0])),career_path_dict.get(char.Career)[1]))
	new_sheet.write(blank.readline())
	new_sheet.write(blank.readline().format(char.Age,char.height_str,char.Hair,char.Eyes))
	for i in range(0,3):
		new_sheet.write(blank.readline())
	new_sheet.write(blank.readline().format(str(char.Character_Stats[11])+' '))
	new_sheet.write(blank.readline())
	new_sheet.write(blank.readline().format(str(char.Character_Stats[0]),str(char.Character_Stats[1]),str(char.Character_Stats[2]),
											str(char.Character_Stats[3]),str(char.Character_Stats[4]),str(char.Character_Stats[5]),
											str(char.Character_Stats[6]),str(char.Character_Stats[7]),str(char.Character_Stats[8]),
											str(char.Character_Stats[9]),str(char.Character_Stats[11])+' ',str(char.Character_Stats[12])+' ',
											str(char.Character_Stats[12])+' '))
	for i in range(0,3):
		new_sheet.write(blank.readline())
	new_sheet.write(blank.readline().format(str(char.Character_Stats[14])+' ',str(char.Character_Stats[14]*2)+' ',str(char.Character_Stats[14]*4)))
	new_sheet.write(blank.read())
	blank.close()
	new_sheet.close()

Generate_stats()
