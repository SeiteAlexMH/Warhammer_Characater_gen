#WarhammerGenerator.py
#Alexandre Seite
import random
Stats_description = ['Weapon Skill: ', 'Ballistic Skill: ', 'Strength: ', 'Toughness: ',
					 'Initiative: ', 'Agility: ', 'Dexterity: ', 'Intelligence: ', 'Willpower: ', 
					 'Fellowship: ', 'Wounds: ', 'Fate: ', 'Resilliance: ', 'Extra points: ', 'Movement: ']
					 
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
				'Cavalryman    ','Guard         ','Knight        ','Pit Fighter   ','Protagonist   ','soldier       ','Slayer        ','Warrior Priest']

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

raceIndex = 0
Character_Stats = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
strength_bonus = 0
tough_bonus = 0
will_bonus = 0
Age = 0
Hair = ''
Eyes = ''
Career = ''
charClass = ''
charTalents = []
charTrappings = []

def Generate_stats():
	
	#Determining race, career and age
	careerScore = random.randint(0,99)
	race = random.randint(1,100)
	#Hardcode value here for specific race
	#race = 90
	#careerScore = 77
	if race <= 90:
		raceIndex = 0
		Age = 15 +random.randint(1,10)
		charClass = Class_table[HumanCareerCoord[careerScore][0]]
		Career = Career_table[HumanCareerCoord[careerScore][1]]
		get_trappings(HumanCareerCoord[careerScore][0])
		print("Human character")
	elif race <= 94:
		raceIndex = 1
		charClass = Class_table[DwarfCareerCoord[careerScore][0]]
		Career = Career_table[DwarfCareerCoord[careerScore][1]]
		get_trappings(DwarfCareerCoord[careerScore][0])
		Age = 15
		for value in range(0,10):
			Age += random.randint(1,10)
		print("Dwarf character")
	elif race <= 98:
		raceIndex = 2
		charClass = Class_table[HaflingCareerCoord[careerScore][0]]
		Career = Career_table[HaflingCareerCoord[careerScore][1]]
		get_trappings(HaflingCareerCoord[careerScore][0])
		Age = 15
		for value in range(0,5):
			Age += random.randint(1,10)
		print("Halfling character")
	elif race == 99:
		raceIndex = 3
		charClass = Class_table[HighElfCareerCoord[careerScore][0]]
		Career = Career_table[HighElfCareerCoord[careerScore][1]]
		get_trappings(HighElfCareerCoord[careerScore][0])
		Age = 30
		for value in range(0,10):
			Age += random.randint(1,10)
		print("High Elf character")
	elif race == 100:
		raceIndex = 4
		charClass = Class_table[WoodElfCareerCoord[careerScore][0]]
		Career = Career_table[WoodElfCareerCoord[careerScore][1]]
		get_trappings(WoodElfCareerCoord[careerScore][0])
		Age = 30
		for value in range(0,10):
			Age += random.randint(1,10)
		print("Wood Elf character")
	else:
		print("error?")
		
	#Generating character's stats
	for value in range(0,10):
		Character_Stats[value] = Stats_tables[raceIndex][value] + random.randint(1,10) +random.randint(1,10)
	for value in range(10,14):
		Character_Stats[value+1] = Stats_tables[raceIndex][value]
	
	#Determining stat bonus for health calc	
	strength_bonus = str(Character_Stats[2])[0]
	tough_bonus = str(Character_Stats[3])[0]
	will_bonus = str(Character_Stats[8])[0]
	
	#Health calculation
	if raceIndex == 2:
		Character_Stats[10] = 2*int(tough_bonus) + int(will_bonus)
	else:
		Character_Stats[10] = int(strength_bonus) + 2*int(tough_bonus) + int(will_bonus)
	
	#Allocating extra points to fate and resolve
	fate = int(input("you have " + str(Character_Stats[13]) + " extra points. How many should go to your fate? "))
	
	while fate > Character_Stats[13] or fate < 0:
		fate = int(input("Incorrect value! input cannot be negative or exceed " +str(Character_Stats[13]) + ": "))
		
	Character_Stats[11] += fate
	Character_Stats[12] += Character_Stats[13]-fate
	
	#rolling random hair and eye colours
	Roll= random.randint(1,10) + random.randint(1,10) - 2
	if raceIndex == 0 and Roll == 0:
		print('Free choice! choose one of the following:')
		print('1: Green, 2: Pale Blue, 3: Blue, 4: Pale Grey, 5: Grey, 6: Brown, 7: Hazel, 8: Dark Brown, 9: Black')
		Roll = int(input(''))
		Eyes = Eye_tables[raceIndex][Roll]
	else:
		Eyes = Eye_tables[raceIndex][EyeHairIndeces[Roll]]
	Roll= random.randint(1,10) + random.randint(1,10) - 2
	Hair = Hair_tables[raceIndex][EyeHairIndeces[Roll]]
	
	#Printing out stats for testing.
	for value in range(0,15):
		print(Stats_description[value] +str(Character_Stats[value]))
	print('Walk: ' + str(Character_Stats[14]*2))
	print('Run: ' + str(Character_Stats[14]*4))
	print('Age: ' + str(Age))
	print('Eye colour: ' + Eyes)
	print('Hair Colour: ' + Hair)
	print(charClass +' : '+Career)
	print(charTrappings)

def get_trappings(careerIndex):
	for trappings in Class_trapings[careerIndex]:
		charTrappings.append(trappings)
	if careerIndex == 0:
		charTrappings.append(str(random.randint(1,10))+' Sheets of Parchement')
	if careerIndex == 6:
		charTrappings.append(str(random.randint(1,10))+' Matches')
		charTrappings.append(input('Choose one: Hood or Mask (type choice) '))
		
Generate_stats()
#for value in range(0,100):
#	print(str(value+1) + ' : ' + HumanTraitTable[HumanTraitIndeces[value]])
