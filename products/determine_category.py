import difflib


class DetermineCategory(object):

	def __init__(self, needle, haystacks):
		self.needle = needle
		self.haystacks = haystacks


	def similarityPercentage(self, needle, haystack):
		similarity = difflib.SequenceMatcher(None, needle, haystack)
		percentage = similarity.ratio()*100
		return percentage


	def assignCategory(self):


		print("Needle is: ", self.needle, " haystack is: ", self.haystacks)



		#Knowledge Base Check
		#Knowledge Base Check
		#Knowledge Base Check
		jewelries = {'Watches / Jewelries' : ["Bracelets", "Watches", "Jewelries", "Pendants", "Necklaces", "Rings", "cufflinks", "Bangles", "Ear Rings", "bracelet & bangles","pendants","necklaces","Watches","Swatch","Necklace and Pendant","Women's watches"]}
		kids_wears = { 'Kids Wears' : ["Boys", "Girls", "Wears", "Kids", "Baby","Kids"]}
		pet_products = { 'Pet Products' : ["shampoo","conditioner", "Pet", "Products", "Pet Products", "Pet Care Products"] }
		pet_toys_accessories = { 'Pet Toys and Accessories' : ["Pet Accessories","Pet Toys and Accessories"] }
		pet_foods = { 'Pet Foods' : ["Pet Food & Supplement"] }
		large_appliances = { 'Large Appliances' : ["Large Appliances", "freezers","fridge","washing machine","cookers and ovens","ventilators","Air Conditioners & Coolers","Dishwashers","Vacuum & Steam","Cleaners","Machines and Dryers","Floor Care & Vacuum Accessories","Home & Kitchen Bundles","Furniture","Heaters"] }
		small_appliances = { 'Small Appliances' : ["Small Appliances", "cookers","blenders","juicers","hot plates","fans","water dispensers","clocks","curtains","blinds"," Floor Care","Toasters & Sandwich Makers","irons","Yam Pounders","Popcorn Poppers & Candy Floss Makers","Processors, Mincers & Electric Slicers","Coffee & Tea Machines","Microwaves","Boiling Rings","Chocolate Fountains","Crepe, Bread & Pasta Makers","Electric Fryers","Electric Grills","Electric Kettles & Air Pots","Food Dehydrators","Food Sealers","Humidifiers & Purifiers","Ice Cream Machine","Ice Cube Makers"] }
		interior_accessories = {'Interior Decoration / Accessories' : ["Home Furnishing"]}
		smart_phones = { 'Smart Phones' : ["Smart Phones", "Phones", "android","ios","windows","java","Nokia","blackberry","samsung","apple","huawei p9","s7edge","htc","tecno"] }
		televisions = { 'Televisions' : ["Televisions", "TVs", "3D TVs","Curved TVs","LED TVs","OLED TVs","Plasma TVs","Smart TVs","3D Glasses","Flat Screen TVs"," UHD"] }
		games_and_consoles = { 'Games and Consoles' : ["Games", "Consoles", "Games and Consoles", "Playstation 4","Playstation 3","Nintendo Wii","Nintendo Switch","Xbox One","Playstation Vita","Xbox 360","Nintendo 3DS","NIntendo 2DS","PSP","Nintendo Wii U"," Sony PSP","PS3","PS4","gaming consoles"] }
		laptops = { 'Laptops' : ["Laptops", "Apple MacBooks", "MacBooks", "Hybrid Computers","Mini Laptops","Netbooks","Notebooks","Ultrabooks", "laptops & desktops","hp"] }
		outdoor =  {'Outdoor' : ["Outdoor","Garden"] }
		maternity_accessories =  {'Maternity Accessories' : ["Maternity Accessories"] }
		maternity_tops_and_jackets =  {'Maternity Tops & Jackets' : ["Maternity Tops & Jacketss"] }
		maternity_underwear =  {'Maternity Underwear' : ["Maternity Underwear"] }
		maternity_trousers_and_skirts =  {'Maternity Trousers & Skirts' : ["Maternity Trousers & Skirts"] }
		maternity_dresses =  {'Maternity Dresses' : ["Maternity"] }
		arts_crafts_sewing = { 'Sewing Machine and Accessories' : ["Sewing", "Machine", "Sewing Machine and Accessories", "Arts, Crafts & Sewing"] }
		activity_tracker = {'Activity Trackers': ["Activity Trackers"] }
		smart_watches = {'Smart Watches' : ["Smart Watches"] }
		sports_and_gps_watches = {'Sports & GPS Watches' : ["Sports & GPS Watches"] }
		virtual_reality = {'Virtual Reality' : ["Virtual Reality"] }
		wearable_cameras = {'Wearable Cameras': ["Wearable Cameras"] } 
		portable_audios_and_gadgets = {"Portable Audios and Gadgets" : ["Portable Audios and Gadgets","Portable Audio & Video"] }
		automotive_parts_and_accessories = { 'Automotive Tools and Accessories' : ["Automotive Parts & Accessories","Tools"] }
		generators_and_power_solutions = {"Generators & Power Solutions" : ["Generators & Power Solutions"] }
		cars_and_vehicles = {'Replacement Parts' : ["Cars and Vehicles"]}
		mens_trousers_and_shorts = {'Trousers and Chinos' : ["Men's Trousers and Shorts","Men's Jeans", "Jeans", "Trousers & Chinos"]}
		polo_shirts = {'Polo Shirts' : ["Polo Shirts", "Polos"]}
		sweaters_and_jumpers = {'Sweaters and Jumpers' : ["Sweaters and Jumpers", "Jumpers & Cardigans"]}
		lingerie_and_sleepwear = {'Lingerie and Nightwear' : ["Lingerie and Sleepwear"]}
		womens_trousers = {"Trousers and Leggins" : ["Women's Trousers","Jeans & Jeggings","Trousers, Shorts & Leggings","mel trousers","mel bottoms"]}
		suits_and_blazers = {"Suits" : ["Suits & Blazers","Suits, Blazers & Jackets","Suits"]}
		women_tops = {"Tops" : ["Women's Tops", "Tops", "Tops & Blouses","mel tops"] }
		women_skirts = {"Skirts" : ["Women's Skirts", "Skirts","mel skirts"]}
		jumpsuits_and_playsuits = {"Jumpsuits and Playsuits" : ["Jumpsuits and Playsuits", "Playsuits & Jumpsuits"]}
		kimonos = {"Kimonos" : ["Kimonos"]}
		women_dresses = {"Dresses" : ["Women's Dresses","Dresses","mel dress"]}
		lingerie_and_sleepwear = {"Lingerie and Nightwear" : ["Lingerie and Sleepwear","Singlets"]}
		mobile_phones = {"Smart Phones" : ["Mobile Phones","mobiles & tablets"]}
		tablets = {"Tablets" : ["Tablets"]}
		projectors_and_accessories = {"Projectors" : ["Projectors & Accessories","Projectors & Screens","projectors"]}
		wifi_and_networking = {"Networking" : ["WiFi & Networking","networking equipments"]}
		desktop_and_monitors = {"Desktop Computer" : ["Desktop and Monitors", "Desktops","all-in-one"]}
		computer_software = {"Software" : ["Computer Software", "Software"]}
		souvenirs = {"Souvenirs" : ["Souvenirs"]}
		construction_materials = {"Construction Materials" : ["Building & Construction"]}
		plumbing_materials = {"Plumbing Materials" : ["Plumbing Materials"]}
		dvd_players_and_recorders = {"DVD Players and Recorders" : ["DVD Players & Recorders","Blu Ray & DVD Players"]}
		cameras_photos = {"Cameras" : ["Cameras & Photo", "Cameras", "digital cameras"]}
		men_underwear_and_socks={"Socks and Tights" : ["Men's Underwear and Socks"]}
		men_shirts = {"Shirts" : ["Men's Shirts","Shirts"]}
		shorts = {"Shorts" : ["Shorts"]}
		furniture = {"Home & Office Furniture" : ["Office Furniture","tv stand","dining sets","center tables","event furniture","office chairs","office tables"]}
		hair_care = {"Hair Care" : ["Natural Hair Shop","Hair and Hair Care"]}
		personal_care = { "Personal Care" : ["Cosmetics","Skin Care","personal care & wellness","Feminine Care","Bath Salts & Soaks","Bath & Shower","Hair Removal","Deodorants & Wipes","Stretch Mark Creams","Body Sculpting & Toning","Shop By Skin Concern","Shop By Skin Type","Shop By Product"]}
		mens_grooming = {"Mens Grooming" : ["Men's Grooming"]}
		underwear = {"Underwear" : ["Underwear & Sleepwear","Underwears"]}
		jackets_and_coats = {"Jackets and Coats" : ["Jackets & Coats", "Coats & Jackets","Jackets","mel jackets"]}
		swimwear_and_beachwear = {"Swimwear and Beachwear" : ["Beach & Swimwear"]}
		toys_and_activities = {"Toys and Activities" : ["Kids Toys & Games"]}
		watches = {"Watches" : ["unisex watches","All Watches","Watch Accessories","Women's Watches","Titan","Men's Watches","Analog","Analog & Digital","Digital"]}
		general_accessories = {"General Accessories" : ["Aviator"]}
		sunglases = {"Sunglasses" : ["Sunglasses","Rayban","Multi","Black","Gold"]}
		gift_bags_items = {"Gift Bags and Boxes" : ["Gifts & Party Supplies","Gift Items & Party Supplies"]}
		kids_food = {"Kids Food" : ["Baby Food & Milk"]}
		fresh_food = {"Fresh Food" : ["Fresh Food"]}
		toiletries = {"Toiletries" : ["Toiletries", "sanitizers","hand wash","Scented Candles/Fragrances","Body Lotions, Butters & Creams"]}
		printers_and_scanner = {"Printers and Scanners" : ["Printers and scanners","Printers & Scanners","scanners","printers"]}
		tracksuits = {"Tracksuits":"Tracksuits"}
		bags_and_purses = {"Bags and Purses" : ["Handbags","Female Bags"]}
		drives_and_storage = {"Drives and Storage" : ["storage device","external hard drive"]}
		laundry_and_homecare = {"Laundry and Homecare":["toilet bowl cleaner","laundry detergent","glass cleaner","floor cleaner","dish washing liquid","baskets"]}
		arts_crafts = {"Arts, Crafts and Sewings" : ["art","Crafts"]}
		female_jewelries = {"Jewellery" : ["Female Jewellery"]}
		spirit_drink = {"Spirit" : ["Gin","Vodka","Tequila"]}
		wine_drink = {"Wine" : ["Sparkling Brut Wine", "Red wine","White wine"]}
		laptop_and_desktop_accessories = {"Laptop and Desktops Accessories" : ["sleeves"]}
		food_drink = {"Food & Drink" : ["food & drink"]}
		spa_beauty = {"Salon and Spa" : ["spa & beauty","Salon and Spa","Hand & Foot Care","Nails"]}
		groceries = {"Groceries" : ["Beer, Wine & Spirits", "groceries"]}
		books = {"Books" : ["books"]}
		make_up = {"Eyes" : ["Eyes"]}
		make_up_products = {"Face" : ["Face"]}
		#End Knowledge Base Check
		#End Knowledge Base Check
		#End Knowledge Base Check

		available_direct_checks = [jewelries,kids_wears,pet_products,pet_toys_accessories,pet_foods,large_appliances,small_appliances,
									interior_accessories,smart_phones,televisions,games_and_consoles,laptops,outdoor,maternity_accessories,
									maternity_tops_and_jackets,maternity_underwear,maternity_trousers_and_skirts,maternity_dresses,
									arts_crafts_sewing,activity_tracker,smart_watches,sports_and_gps_watches,virtual_reality,wearable_cameras,
									portable_audios_and_gadgets,automotive_parts_and_accessories,generators_and_power_solutions,cars_and_vehicles,
									mens_trousers_and_shorts,polo_shirts,sweaters_and_jumpers,lingerie_and_sleepwear,womens_trousers,suits_and_blazers,
									women_tops,women_skirts,jumpsuits_and_playsuits,kimonos,women_dresses,lingerie_and_sleepwear,mobile_phones,tablets,
									projectors_and_accessories,wifi_and_networking,desktop_and_monitors,computer_software,souvenirs,construction_materials,
									plumbing_materials,dvd_players_and_recorders,cameras_photos,men_underwear_and_socks,men_shirts,shorts, furniture,
									hair_care, personal_care, mens_grooming, underwear, jackets_and_coats, swimwear_and_beachwear, watches, general_accessories,
									sunglases, gift_bags_items, kids_food, fresh_food, toiletries, printers_and_scanner,tracksuits, bags_and_purses, drives_and_storage,
									laundry_and_homecare, arts_crafts, female_jewelries, spirit_drink, wine_drink, laptop_and_desktop_accessories, food_drink,
									spa_beauty, groceries, books, make_up_products, make_up  
									]


		for each_available in available_direct_checks:
			for key, value in each_available.items():
				loweredNeedle = self.needle.lower().strip()
				#print("loweredNeedle is: ", loweredNeedle, " value is : ", value)
				for val in value:
					valLowered = val.lower().strip()
					if ( (loweredNeedle == valLowered) or (loweredNeedle[:-1] == valLowered) or (loweredNeedle+'s' == valLowered)):
						print("We returning : ", key, " for ", self.needle)
						return key

		#We are returning the last element which is the Category Miscallaneous
		#We no longer doing Similarity Testing
		else:
			misc = self.haystacks[-1]
			print("No knowledge base found - Assign Misc class for this sub category: ", misc)
			return misc


		#All the Codes below will be ignored for now
		#All the Codes below will be ignored for now
		#All the Codes below will be ignored for now

		print("This Product ", self.needle, " is not in Knowledge Base... So we using Similarity case...")
		finalAns = {}
		finalRevAns = {}
		for eachNeedle in self.haystacks:
			#print("Each haystacks item is: ", eachNeedle)
			#2 - Do the Reverse Checks
			arrayNeedle = eachNeedle.lower().split()
			arrayNeedle = list(reversed(arrayNeedle))
			reversedNeedle = ''.join(arrayNeedle)
			arrayHay = self.needle.lower().replace(" ", "")



			reverz = self.similarityPercentage(reversedNeedle, arrayHay)
			finalRevAns[reverz] = eachNeedle


			#3 - Do the Forward Checks
			res = self.similarityPercentage(self.needle.lower(), eachNeedle.lower())
			finalAns[res] = eachNeedle


			#4 - Do Palindrome Check
			if arrayHay == reversedNeedle:
				print("Palidrome was found from Katlogg Category Names: ", eachNeedle, " and current score category name: ", self.needle)
				return eachNeedle


		#Sum Everything
		sortedList = sorted(finalAns, reverse=True)
		highestScore = sortedList[0]
		assignCategory = finalAns[highestScore]
		print(assignCategory, " was assigned as categoryName for ", self.needle, "  cos of its FORWARD highest score of ", highestScore)


		revSortedList = sorted(finalRevAns, reverse=True)
		revHighestScore = revSortedList[0]
		revAssignCategory = finalRevAns[revHighestScore]
		print(revAssignCategory, "  was assigned as categoryName for ", self.needle, " cos of its REVERSED highest score of ", revHighestScore)


		decider = 0
		#Compare and Return Answer
		if(highestScore > revHighestScore):
			decider = highestScore
			finalAssignedCategory = assignCategory
		else:
			decider = revHighestScore
			finalAssignedCategory = revAssignCategory


		if decider >= 50:
			print("Winner is ", finalAssignedCategory)
			return finalAssignedCategory
		else:
			print("Accuracy is less than 50 - Assign Miscallaneous")
			return " Less than 50% - " + "Miscallaneous"
