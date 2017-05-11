from random import randint

champions = ["Aatrox", "Ahri", "Akali", "Alistar", "Amumu",
 "Anivia", "Annie", "Ashe", "Aurelion Sol", "Azir", "Bard",
 "Blitzcrank", "Brand", "Braum", "Caitlyn", "Camille",
 "Cassiopeia", "Cho'Gath", "Corki", "Darius", "Diana",
 "Dr.Mundo", "Draven", "Ekko", "Elise", "Evelynn",  "Ezreal",
 "Fiddlesticks", "Fiora", "Fizz", "Galio", "Gangplank",
 "Garen", "Gnar", "Gragas", "Graves", "Hecarim",
 "Heimerdinger", "Illaoi", "Irelia", "Ivern", "Janna",
 "Jarvan",  "Jayce", "Jhin", "Jinx", "Kalista", "Karma",
 "Karthus", "Kassadin", "Katarina", "Kayle", "Kennen",
 "Kha'Zix", "Kindred", "Kled", "Kog'Maw", "LeBlanc", "Lee Sin",
 "Lulu", "Lux", "Malphite", "Malzahar", "Maokai", "Master Yi",
 "Miss Fortune", "Mordekaiser", "Morgana", "Nami", "Nasus",
 "Nautilus", "Nidalee", "Nocturne", "Nunu", "Olaf", "Orianna",
 "Pantheon", "Poppy", "Quinn", "Rakan", "Rammus", "Rek'Sai", 
 "Renekton", "Rengar", "Riven", "Rumble", "Ryze", "Sejuani",
 "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir", 
 "Skarner", "Sona", "Soraka", "Swain", "Syndra", "Tahm Kench",
 "Talon", "Taric", "Tailyah", "Teemo", "Thresh", "Tristana", 
 "Trundle", "Tryndamere", "Twisted Fate", "Twitch", "Udyr", 
 "Urgot", "Varus", "Vayne", "Veigar", "Vel'Koz", "Vi", "Viktor",
 "Vladimir", "Volibear", "Warwick", "Wukong", "Xayah", "Xerath",
 "Xin Zhao", "Yasuo", "Yorick", "Zac", "Zed", "Ziggs", "Zilean",
 "Zyra"]

items = ["Abyssal Scepter", "Archangel's Staff", "Ardent Censer",
 "Athene's Unholy Grail", "Banner of Command", "Banshee's Veil",
 "Black Cleaver", "Blade of the Ruined King", "Bloodthirster",
 "Dead Man's Plate", "Death's Dance", "Duskblade of Draktharr", 
 "Edge of Night", "Essence Reaver", "Eye of the Equinox",
 "Eye of the Oasis", "Eye of the Watches", 
 "Face of the Mountain", "Frost Queen's Claim", "Frozen Heart",
 "Frozen Mallet", "Guardian Angel", "Guinsoo's Rageblade", 
 "Hextech GLP-800", "Hextech Gunblade", "Hextech Protobelt-01",
 "Iceborn Gauntlet", "Infinity Edge", "Knight's Vow", 
 "Liandry's Torment", "Lich Bane", "Locket of the Iron Solari", 
 "Lord DOminik's Regards", "Luden's Echo", "Munamune", 
 "Maw of Malmortius", "Mejai's Soulstealer", 
 "Mercurial Scimitar", "Mikael's Crucible", 
 "Moonflair Spellblade", "Morellonomicon", "Mortal Reminder", 
 "Nashor's Tooth", "Ohmwrecker", "Phantom Dancer", 
 "Rabadon's Deathcap", "Randuin's Omen", "Rapid Firecannon",
 "Ravenous Hydra", "Redemption", "Righteous Glory",
 "Rod of Ages", "Ruby Sightstone", "Runaan's Hurricane",
 "Rylai's Crystal Scepter", "Spirit Visage", "Statikk Shiv",
 "Sterak's Gage", "Sunfire Cape", "Talisman of Ascension", 
 "Thornmail", "Wit's End", "Youmuu's Ghostblade", 
 "Zeke's Harbinger", "Zhonya's Hourglass", "Zz'Rot Portal"]

boots = ["Berserker's Greaves", "Boots of Mobility",
 "Boots of Swiftness", "Ionian Boots of Lucidity", 
 "Mercury's Treads", "Ninja Tabi", "Sorcerer's Shoes"]

top_laners = ["Aatrox", "Akali", "Camille", "Darius", 
"Dr. Mundo", "Fiora", "Gangplank", , "Gnar", "Heimerdinger",
 "Illaoi", "Irelia", "Jax", "Kennen", "Kled", "Malphite", 
 "Maokai", "Mordekaiser", "Nasus", "Nautilus", "Nidalee", 
 "Nocturne", "Nunu", "Olaf", "Pantheon", "Poppy", "Quinn", 
 "Rammus", "Renekton", "Riven", "Rumble", "Shen", "Singed", 
 "Swain", "Trundle", "Tryndamere", "Vladimir", "Yasuo", "Yorick"]

junglers = ["Amumu", "Cho Gath", "Elise", "Evelynn",
 "Fiddlesticks", "Gragas", "Graves", "Hecarim", "Ivern",
 "Jarvan IV", "Kha Zix", "Kindred", "Lee Sin", "Master Yi",
 "Rek Sai", "Rengar", "Sejuani", "Shaco", "Shyvana", "Skarner",
 "Udyr", "Vi", "Volibear", "Warwick", "Wukong", "Xin Zhao", 
 "Zac"]

mid_laners = ["Ahri", "Anivia", "Annie", "Aurelion Sol", "Azir",
 "Brand", "Cassiopeia", "Corki", "Diana", "Ekko", "Fizz", 
 "Galio", "Jayce", "Karthus", "Kassadin", "Katarina", "Kayle", 
 "LeBlanc", "Lissandra", "Lux", "Malzahar", "Orianna", "Ryze",
 "Syndra", "Taliyah", "Talon", "Twisted Fate", "Veigar", 
 "VelKoz", "Viktor", "Xerath", "Zed", "Ziggs"]

adc = ["Ashe", "Caitlyn", "Draven", "Ezreal", "Jhin", "Jinx", 
"Kalista", "Kog Maw", "Lucian", "Miss Fortune", "Sivir", 
"Tristana", "Twitch", "Urgot", "Varus", "Vayne", "Xayah"]

supports = ["Alistar", "Bard", "Blitzcrank", "Braum", "Janna",
 "Karma", "Leona", "Lulu", "Morgana", "Nami", "Rakan", "Sion",
 "Sona", "Soraka", "Tahm Kench", "Taric", "Thresh", "Zilean", 
 "Zyra"]

def random_champion():
	length = len(champions)
	return champions[randint(0, length - 1)]
	
def random_item():
	length = len(items)
	return items[randint(0, length - 1)]
	
def random_boots():
	length = len(boots)
	return boots[randint(0, length - 1)]

def random_top_laner():
	length = len(top_laners)
	return top_laner[randint(0, length - 1)]
	
def random_jungler():
	length = len(junglers)
	return jungler[randint(0, length - 1)]
	
def random_mid_laner():
	length = len(mid_laners)
	return mid_laners[randint(0, length - 1)]
	
def random_adc():
	length = len(adc)
	return adc[randint(0, length - 1)]
	
def random_support():
	length = len(supports)
	return supports[randint(0, length - 1)]
	
def random_build():
	items = [random_item(), random_item(), random_item(), random_item(), random_item(), random_boots()]
	return items 
