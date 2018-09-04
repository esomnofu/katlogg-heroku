"""
DETAILED VIEW --- TO GET ALL RELEVANT INFORMATION FOR EACH PRODUCT ON THE DETAILED PAGE
THE CLASS TAKES THE FULL URL PATH TO THE DETAIL PAGE
ACCESSES ALL RELAVANT INFO AND MAKES AN INSTANCE OF THEM AND STORES AS OBJECTS IN A SET
"""
from lxml import html
import requests
import datetime
from products.general import *
from products.domain import *
from collections import Counter
from products.determine_category import *
import ast
import time


class DetailCrawler(object):

	def __init__(self, starting_url, product_name, product_color, product_seller, product_current_price, product_old_price, product_categories, product_sizes, product_percentage_off, product_images, product_description, product_sub_sub_categories):

		self.starting_url = starting_url
		
		self.product_name = product_name

		self.product_color = product_color

		self.product_description = product_description
		
		if product_seller.strip() == "":
			self.product_seller = get_domain_name(starting_url)
		else:
			self.product_seller = product_seller
		
		self.product_current_price = product_current_price
		self.product_old_price = product_old_price
		self.product_categories = product_categories
		self.product_sizes = product_sizes
		self.product_percentage_off = product_percentage_off
		self.product_images = product_images
		self.product_sub_sub_categories = product_sub_sub_categories
		self.items = []

		ans = get_full_domain_name(self.starting_url)

		if ans == "ng.fashpa.com":
			self.project = "ng.fashpa.com"
		else:
			self.project = get_domain_name(starting_url)
	

		self.colors =  ["AliceBlue","AntiqueWhite","Aqua","Aquamarine","Azure","Beige","Bisque","Black","BlanchedAlmond","Blue","BlueViolet","Brown","BurlyWood","CadetBlue","Chartreuse","Chocolate","Coral","CornflowerBlue","Cornsilk","Crimson","Cyan","DarkBlue","DarkCyan","DarkGoldenRod","DarkGray","DarkGrey","DarkGreen","DarkKhaki","DarkMagenta","DarkOliveGreen","Darkorange","DarkOrchid","DarkRed","DarkSalmon","DarkSeaGreen","DarkSlateBlue","DarkSlateGray","DarkSlateGrey","DarkTurquoise","DarkViolet","DeepPink","DeepSkyBlue","DimGray","DimGrey","DodgerBlue","FireBrick","FloralWhite","ForestGreen","Fuchsia","Gainsboro","GhostWhite","Gold","GoldenRod","Gray","Grey","Green","GreenYellow","HoneyDew","HotPink","IndianRed","Indigo","Ivory","Khaki","Lavender","LavenderBlush","LawnGreen","LemonChiffon","LightBlue","LightCoral","LightCyan","LightGoldenRodYellow","LightGray","LightGrey","LightGreen","LightPink","LightSalmon","LightSeaGreen","LightSkyBlue","LightSlateGray","LightSlateGrey","LightSteelBlue","LightYellow","Lime","LimeGreen","Linen","Magenta","Maroon","MediumAquaMarine","MediumBlue","MediumOrchid","MediumPurple","MediumSeaGreen","MediumSlateBlue","MediumSpringGreen","MediumTurquoise","MediumVioletRed","MidnightBlue","MintCream","MistyRose","Moccasin","NavajoWhite","Navy","OldLace","Olive","OliveDrab","Orange","OrangeRed","Orchid","PaleGoldenRod","PaleGreen","PaleTurquoise","PaleVioletRed","PapayaWhip","PeachPuff","Peru","Pink","Plum","PowderBlue","Purple","Red","RosyBrown","RoyalBlue","SaddleBrown","Salmon","SandyBrown","SeaGreen","SeaShell","Sienna","Silver","SkyBlue","SlateBlue","SlateGray","SlateGrey","Snow","SpringGreen","SteelBlue","Tan","Teal","Thistle","Tomato","Turquoise","Violet","Wheat","White","WhiteSmoke","Yellow","YellowGreen"]





		#Katlogg Sub Categories
		#Katlogg Sub Categories
		#Katlogg Sub Categories
		self.kids_fashion = {"['Dresses', 'Denim, Trouser and Leggins', 'Watches', 'Bracelets / Pendants / Necklaces', 'Underwear and Socks', 'Shoes', 'Polos and Tshirts', 'Sleepwear', 'Bodysuits and Playsuits', 'Shirts', 'Kids Fashion / Miscellaneous']" : ["Kids", "Girls", "Baby", "Children", "Fashion for Girls", "Baby, Kids & Toys", "PENDANTS", "CROSS PENDANT", "NECKLACES", "BRACELETS / BANGLES", "Boys", "Kids Fashion", "Fashion for boys", "bracelet & bangles","pendants","necklaces","Watches","Women's watches","Back To School","Babies","baby & kids"]}
		self.grooming_and_healthcare = {'["Dental Care","Nose & Ear Care","Thermometer","Grooming Kits", "Grooming - Health Care / Miscellaneous"]': ["Baby Products"] }
		self.diapering_and_daily_Care =  { '["School Stores","Travel and Safety Gear","Kids Beddings and Decor","Kids Food","Toys and Activities","Baby Creams and Lotions","Shampoo and Body Wash","Bath tub and seats","Diapers and Baby Wipes","Diaper Bags","Potty Training","Diapering - Daily Care / Miscellaneous"]':["Party Store","Baby food and Milk","Elephant Teething Toy","Car teething Toy","Todi-donut Teething Toy","Toys and Games","School Store","Kid's Beauty","Kids Toys & Games","Baby Food & Milk"] }
		self.pet_supplies = { "['Pet Care Products','Pet Toys and Accessories','Pet foods','Pet Supplies / Miscellaneous']" : ['Pet Supplies', "Pet Care Products", "Pet Toys and Accessories", "Pet Accessories", "Pet Food & Supplement","Animals & Pets"] }
		self.women_fashion = { '["Dresses","Kimonos","Jumpers and Cardigans","Jumpsuits and Playsuits","Hoodies and Sweatshirts","Lingerie and Nightwear","Shorts","Skirts","Coats and Jackets","Socks and Tights","Suits","Swimwear and Beachwear","Tops","Trousers and Leggins","Women Fashion / Miscellaneous"]' : ["Women's Fashion",'Women','Equipment', 'Sales','Ankara Styles', 'Multi-Pack','Singlets','Trousers, Shorts & Leggings', "Women's Trousers", "Women's Tops", "Women's clothing", "Women's Skirts", "Women's Plus Size", "Women's Dresses", "Women's wear", "Traditional Clothing & Accessories", "Suits & Blazers","Women's Ready to Wear","Women's T-Shirts", 'Plus Size', 'Plus Sizes','Jumpsuits and Playsuits', 'Playsuits & Jumpsuits', 'Islamic Wear','Jumpers & Cardigans', 'Socks & Tights','Skirts', 'Trousers & Leggings','Babydolls', 'Sunglasses','Dresses', 'Traditional', 'Swimwear & Beachwear','BUTT PADS', 'Shoes','Shorts', 'Jeans','Coats & Jackets','Suits & Blazers', 'Lingerie & Nightwear','Polo Shirts', 'Denim','Kimonos', 'Lingerie and Sleepwear','Apparel', 'Underwear & Sleepwear','Hoodies & Sweatshirts','Clothing','Corporate Wear','Tops','Jeans & Jeggings',"Co-ordinates","Coordinates","Womens Ready to Wear","Uniforms, Work & Safety Clothing", "Beach & Swimwear","Tops & Blouses","Skirts & Trousers","mel trousers","mel tops","mel skirts","mel jackets","mel dress","mel bottoms","mel","bottoms","Fashion Fixes","Car & Travel Essentials"]}
		self.make_up = { '["Face","Eyes","Lips","Cheeks","Make-up / Miscellaneous "]' : ["Beauty","Makeup & Body Art","Make-up Cosmetics","Beauty, Health & Personal Care Bundles","Make-up","Makeup Removers","Tools & Accessories","Palettes","MUA Essentials","","Eyes","Face"] }        
		self.fragrances = { '["Men","Women","Unisex", "Fragrances/Miscellaneous"]' : ["Perfumes","Mens Fragrances","Womens Fragrances","Fragrances","fragrances & cosmetics","Perfumes"] }
		self.hair_and_hair_care = { '["Hair Care","Hair and Hair Care / Miscellaneous"]' : ["Hats & Hair Accessories","Hosiery","Scarves","Natural Products","Natural Hair Shop","Hair and Hair Care","Hair Centre","Hair & Beauty","Hair Colour","Haircare","Hair Extensions & Wigs","Styling Products","Natural Corner","Styling Tools" ] }
		self.health_and_wellbeing = { '["Personal Care","Salon and Spa","Mens Grooming","Health and Well being / Miscellaneous"]' : ["Intimate","Pharmacy & Wellness","Skin Care","Mens Grooming","Contact Lenses","Hand Feet & Nail Care","Manicure & Pedicure","Beauty, Health & Personal Care","Personal Care" ,"Health","Hand, Feet & Nail Care","Cosmetics","ZPC Health","Men's Grooming","Lifestyle Set","personal care & wellness","spa & beauty","Supplements","Feminine Care","Hand & Foot Care","Nails","Eye & Ear Care","Bath Salts & Soaks","Bath & Shower","Hair Removal","Deodorants & Wipes","Stretch Mark Creams","Body Sculpting & Toning","Bath Accessories","Shop By Skin Concern","Shop By Skin Type","Shop By Product"] }
		self.sports_and_fitness = { '["Sportswear","Football","Swimming","Boxing","Cycling" ,"Basketball" ,"Racket Sports" ,"Sports and Fitness / Miscellaneous"]' : ["Activewear","Gym Gear","Active" ,"Jerseys" ,"Basketball Jerseys", "Basketball Jersey","Football Polos" ,"Football Tracksuits" ,"Sports and fitness" ,"Sport & Lifestyle" ,"Sports Footwear","NSW" ,"Running","Cigarettes & Accessories", "Sports","Training Kits","Anthem Jackets","sports & fitness"] }
		self.adult_toys = { '["Dildos","Vibrators","Strap On","Butt Plugs","Adult Toys / Miscellaneous"]' : ["Adult toys"," Other Categories/Temptations/ Exotic clothing"] }
		self.men_fashion = { '["Jackets and Coats","Shirt","Polo Shirts","Shorts","Socks and Tights","Suits","Shirts and Vests","Tracksuits","Trousers and Chinos","Underwear","Men Fashion / Miscellaneous"]' : ["Mens Fashion","Mens Clothing","Shirts","T-Shirts","Polos","Trousers & Chinos","Tracksuits","Joggers","Jackets","T-shirt and Short Set","Underwear & Socks","Caps & Hats","Shorts","Jeans","Long Sleeve T-Shirts","Polo Shirts","Jumpers & Cardigans","Swimwear","Jackets & Coats","Hoodies &Sweatshirts","Suits & Blazers","Mens T-Shirts","Beach & Swimwear","Underwear & Sleepwear","Knitwear & Sweatshirts","Jackets & Coats","Traditional Mens","Multi-Pack","Ankara","Mens Nightwear","Mens Shirts","Mens T-Shirts","Mens Trousers and Shorts","Mens Underwear and Socks","Mens Ready to Wear","Mens Traditional Wear & Accessories","Polo Shirts","Suits","Blazers & Jackets","Sweaters and Jumpers","Styles","Youth","Business Wear","Men's Nightwear","Men's Trousers and Shorts","Men's T-Shirts","Men's Shirts","Suits, Blazers & Jackets","Men's Underwear and Socks","Men's Jeans",'Traditional',"Underwears","men's fashion","Men"," men's wear"]}
		self.maternity_fashion = { '["Dresses","Jumpers and Cardigans","Jumpsuits and Playsuits","Hoodies and Sweatshirts","Lingerie and Nightwear","Shorts","Swimwear and Beachwear","Tops","Trousers and Leggins","Maternity Fashion / Miscellaneous"]' : ["Maternity"] }
		self.accessories_female ={ '["Bags and Purses","Wallets","Belts","Watches","Jewellery","Womens Sunglasses","Hair Accessories","Scarves","Caps and Hats","Boots","Espadrilles","Flat Shoes","Heels","Sandals","Slippers","Sliders and Flip Flops","Shoes","Trainers","Female Accessories / Miscellaneous"]' : ["Flip Flops & Sandals","Bags & Purses","Women Accessories","Women Shoes","Multi-Pack","Ankara Styles","Fabric","bags","shoes","Sunglasses","casio","titan","Necklaces","Earrings","Rings","Bracelets","Fine Jewellery","Jewellery Sets","Bangles","Ankle Bracelets","Jewellery Cleaners","Cuffs","Elasticated Band","Womens Bags","Hats & Hair Accessories","Hosiery","Scarves","Womens Belts","Brooches & Bowties","Costumes","Travel Bags and Luggages","Handbags","Female Jewellery","Female Bags","fashion accessories","Clothes Care","women's shoes","women's accessories"] }	
		self.accessories_male = { '["Wallets","Belts","Jewellery","Watches","Mens Sunglasses","Caps and Hats","Ties","Boots","Slippers Sliders and Flip Flops","Shoes","Trainers","Male Accessories / Miscellaneous"]' : ["Men accessories","Sunglasses","Flip Flops & Sandals","Jewellery","Bags","Shoes, Boots & Trainers","Accessories","Bracelets","Belts","Mens Traditional Wear & Accessories","Rubber","Leather","Fabric","Cufflinks","Sneakers","Boots and High Tops","Lace Ups","Loafers","Socks","Caps and Hats","Sandals","Men's watches","Men's Accessories","Travel Bags and Luggages","Swatch","Men's shoes","Multi-Pack","Ankara Styles","Chains & Necklaces","Men's Bracelets & Cuffs","Rings"] }
		self.fabric = { '["Ankara","Lace","Fabric / Miscellaneous"]' : ["Fabric","Womens Fabric","Mens Fabric","fabrics"] }
		self.video_games ={ '["Play station","Nintendo Switch","XBOX","Accessories","Video Games / Miscellaneous "]' : ["Games and Consoles","Games"," Gaming","Other Games","Consoles & Accessories","Playstation 4"," Playstation 3","Nintendo Switch","Nintendo Wii","Xbox One","Playstation Vita","Xbox 360","Nintendo 3DS","PSP","NIntendo 2DS","Nintendo Wii u","bundles","PC Gaming","Gift Cards","Game Hardware","Other Games, Consoles & Accessories","Games Misc","gaming consoles"] }
		self.board_games = { '["Adaptations","Classics","Board Games / Miscellaneous"]' : ["board games"] }
		self.solar_and_alernative_energy = { '["Inverters and Batteries","ups","solar panels and accessories","Solar / Miscellaneous"]' : ["Automobile & Industrial","Power Supplies & Electricals","Inverter Batteries & Accessories","Inverters","Power surge","UPS","Inverters and Social Panels","UPS & Accessories","Power Backup & Regulators","Solar & Alternative Energy","Solar Panels & Accessories","Solar Water Pump"] }
		self.generators_and_accessories = { '["Generators and Accessories","Generators & Power Solutions" "Generators / Miscellaneous"]' : ["Generators & Accessories","Generators & Power Solutions","Automobile & Industries Sale","Industrial & Manufacturing Materials","generators & power supply"] }
		self.gift_bags_and_boxes = { '["Gift Bags and Boxes", "Gifts / Miscellaneous"]' : ["Gifts & Party Supplies","Gift Items & Party Supplies","Gifts For Her"] }
		self.souvenirs = { '["Souvenirs", "Souvenirs / Miscellaneous"]' : ["Other Categories/Weddings / Souvenirs"] }
		self.televisions_and_accessories = { '["Smart Televisions","Tvs","DVD Players and Recorders","Cameras", "Televisions / Miscellaneous"]' : ["Blu Ray & DVD Players","Digital Cameras","MP3 Players & Accessories","Power Supply & Electricals","Scales","Security Gadgets","TV Accessories","Televisions","Cameras","Cameras & Photo","DVD Players & Recorders","Electronic Accessories","Electronic Bundles","Surveillance & Security","Gadgets & Accessories","MP3 Players & Accessories","Audio and Video Bundles","security & surveillance"] }
		self.home_theaters = { '["Camera Accessories","Portable Audios and Gadgets","HiFI Systems","MP3 Players and Systems","Speakers","Home Theater / Miscellaneous"]' : ["Home Theatres and Audio Systems","Sound Systems","Home Theatre & Audio","Home Audio","Portable Audio & Video"] }
		self.musical_instruments_and_equipments = { '["Drums","Equalisers","Headphones and Earphones","Musical / Miscellaneous"]' : ["Musical Instruments","Musical Instruments & Sono", "musical equipment"] }       
		self.wearable_technology = {'["Activity Trackers","Smartwatches","Sports & GPS Watches","Virtual Reality","Wearable Cameras","Wearable Technology / Miscellaneous"]' : ["Activity Trackers","Smartwatches","Sports & GPS Watches","Virtual Reality","Wearable Cameras","Wearable Technology"]}
		self.auto_care_and_maintenance = { '["Accessories and Electronics","Replacement Parts","Oil and Fluids","Automotive Tools and Accessories","Tyres and Rims","Power and Batteries", "Auto Care / Miscellaneous"]' : ["Cars","Automobile and Tools","Auto Care","Automobile & Industrial","Car wash","Automobile Products","Power tools","Car electronics","Vehicle Exterior","Car & Vehicle Electronics","Automotive Parts & Accessories","Automotive & Industrial Bundles","Safety and Security","Tools","Cars and Vehicles"] }
		self.motorcycle = { '["Motorcycles Accessories","Motorcycle Clothing and Protective Gears","Motorcycle / Miscellaneous"]' : ["Automotive"] }
		self.audio_books = { '["Audio Books", "Audio Books / Miscellaneous"]' : ["Wine & Other Categories / Books & Media Library"] }
		self.books = { '["Books", "Books / Miscellaneous"]' : ["Book and Entertainment","Wine & Other Categories / Books & Media Library","Other Categories/Books, Movies & Music","books & stationery","books","Cookery","Pregnancy/Motherhood","Magazines"] }
		self.kindles = { '["kindles", "kindles / Miscellaneous"]' : ["Tablet / Other operating systems","Tablet / All Brands"] }
		self.school_and_office_supplies = { '["school and office supplies", "School - Office Supplies / Miscellaneous "]' : ["Book and Entertainment","Books & Media Library","Stationery"] }
		self.sewing_machines_and_accessories = { '["sewing machine and accessories", "Sewing / Miscellaneous"]' : ["Arts, Crafts & Sewing","Art Craft and Sewing","Mannequins"] }
		self.plumbing_materials = { '["Plumbing Materials", "Plumbing / Miscellaneous"]' : ["Plumbing Materials"] }
		self.construction_materials = { '["Construction Materials", "Construction / Miscellaneous"]' : ["Building & Construction","Home repairs"] }                                                                                                                                                
		self.laptops = { '["Windows","Macbooks", "Laptops/Miscellaneous"]' : ["Computers","Laptops", "laptops & desktops","Notebooks","hp"] }
		self.desktops_and_monitors = { '["Monitors","Desktop/Miscellaneous"]' : ["Laptop & Desktop","Computing","Computers","DESKTOP SYSTEMS - HP","DESKTOP SYSTEM - GENERIC","Acer Monitor","DESKTOP SYSTEMS - DELL","Desktops and Monitors","Desktop and Monitors","Desktops","all-in-one"] }
		self.accessories_and_electronics = { '["Printers and Scanners","Networking","Software","Projectors","Drives and Storage","Laptop and Desktops Accessories","Accessories - Electronics / Miscellaneous"]' : ["Electronics and Computers","Electronics","Accessories","Softwares","Storage Device","Projectors","Printers and scanners","Networking equipments","motherboards/processors","Printer - HP","Printer - Samsung","Printer- Epson","Projectors","Scanner- Canon","SOFTWARE - KASPERSKY ANTIVIRUS","Software - operating system","SOFTWARE NORTON ANTIVIRUS","Software- Microsoft office","Software- Srever software","Laptop Accessories","Peripherals & Accessories","Storage","Software","Computer Components","Printers & Scanners","Computing Bundles","Office Equipment","Bundles","Computer Components","Computer Software","Computing Accessories","Computing Bundles","Printers, Scanners and Accessories","Projectors & Accessories","WiFi & Networking","Software","Display systems","Printers and scanners","Printing consumables","Removable devices","Projectors & Screens","ZPC Electronics","scanners","printers","motherboards and printers","sleeves","external hard drive","computers & networking","Tech Essentials"] }
		self.office_stationary = { '["Books and Notepads","Tapes and Binding Materials","Files and File Trays","Staplers and Staple Pins","Calculators and Batteries","Office Stationery / Miscellaneous"]' : ["Non fireproof cabinet","Tables","Chairs/Sofas","Fireproof safes","Office", "Storage units","Office Furniture","Home and furniture","Furniture","Home and Kitchen Categories / Furniture / Office","CCTV security","Home and office","Office Electronics","Office Essentials"] }
		self.interior_decor =  { '["Large Appliances","Small Appliances","Accessories", "Home & Office Furniture" , "Interior Decoration / Miscellaneous"]' : ["Air Conditioners","Inverters and Social Panels","Washers and Dryers","Bluetooth speakers and woofers","Televisions","Power surge","UPS","CCTV security","Appliances With Special Offers","Floor Care & Vacuum Accessories","Furniture","Heaters","Home & Kitchen Bundles","Home Furnishings","Housekeeping & Pet Supplies","Kids' Home Store","Kitchen and Dining","Large Appliances","Seasonal Decor","Small Appliances","Special Air conditioners","Kitchen and DIning","Home Appliances","Bedsheet/Pillows","Chairs/Sofas","Mattress/Mat","Iron/wooden bed","Fireproof safe","non - fireproof safes","Tables","Home Decor","Tables and Chairs","Living Room","Outdoor furniture","Bar","Kitchen","Storage units","Wallpaper/3d Panels","Laminate floors","Epoxy floors","Window blinds","Wallpapers, Panels & Accessories","Home & Office","Household Supplies","Toiletries","Home & Furniture","Appliances","Bathroom","Outdoor","Dining","Indoor Lighting","Bedroom","tv stand","dining sets","center tables","event furniture","office chairs","office tables","wallpaper/3d panel","epoxy floor","washing machine","home decor & furnishings","kitchen & dining","housekeeping & storage","blenders","Bathroom Essentials"]}
		self.garden_and_outdoor =  { '["Outdoor", "Arts, Crafts and Sewings", "Garden - Outdoor / Miscallaneous"]' : ["Outdoor and indoor games","Outdoor","Garden","Shopping Carts, Trolleys & Racks","art","Crafts"] }
		self.mobile_phones =  { '["Smart Phones","Android","IOS","Windows","Mobile Phones / Miscellaneous"]' : ["Mobile phone type","Shop by brand","Phones","Mobile phones","Landline Phones","Desk, Radio & Intercom Phones","Alcatel","Android","Apple","Blackberry","Bryte","Fero","Gionee","HTC","Huawei","Infinix","ios","Lenovo","Motorola","Nokia","Operating System","Samsung","Silent Circle","Sony","Strong Battery","Tecno","Wiko","Xiaomi","mobile phone huawei","mobile phone htc","mobile phone infinix","mobile phone iphone","mobile phone itel","mobile phone nokia","mobile phone samsung","mobile phone sony","mobile phone techno","Older categories","phone accessories","mobiles & tablets","uncategorized","huawei p9","s7edge"] }
		self.tablet =  { '["Tablet", "Tablet/Miscellaneous"]' : ["Tablet Pads","Tablets","Tablet - Samsung","Tablet- Acer","Tablet- APPLE","TABLETS ES-TAB","Tablet- MR TAB","Tablet Techno","phones & tablets"] }
		self.mobile_phones_and_tablet_accessories =  { '["Batteries","Cables","Cases and Covers","Screen Protectors","Chargers and Power Banks","Docks","Headsets and Earphones","Memory Cards","Smart Watches","Mobile-Phones-Tablet-Accessories / Miscellaneous"]' : ["Mobile Phone Accessories","Phone & Tablet Bundles","Tablet Accessories","Software - operating system"] }
		self.insurance =  { '["Life Insurance","Motor Insurance","Travel Insurance","Device Protection","Education Insurance","Insurance / Miscellaneous"]' : ["Other Categories/Insurance"] }
		self.nutrition =  { '["nutrition", "Nutrition / Miscellaneous"]' : ["Sports Nutrition "] }
		self.christmas = { '["Christmas Hampers","Christmas costumes","Christmas / Miscellaneous"]' : ["Christmas Hampers, Food & Drinks", "Christmas Hats & Caps","Costumes","Christmas Essentials"] }
		self.wedding_and_valentine = { '["Brides","Grooms", "Valentine Wedding / Miscellaneous"]' : ["Fashion / Wedding","Other Categories/Weddings","Valentines Bundle","Valentines Bundles"] }
		self.beverage = { "['tea','coffee','hot chocolate','Beverage / Miscellaneous']" : ["Beverage", "Bundles", "Mixed & Soft Drinks", "Drinks", "Fruit Juices & Drinks", "Drinks & Groceries Bundles","Beverages","Fruit Juice","Water","Energy and Sport drinks","Non alcoholic wine"]} 
		self.alcoholic_beverage = { '["Wine","Spirit","Alcoholic Beverage / Miscellaneous"]' : ["Beer","Wine & Spirits","Cognac", "Champagne","Whisky","Wines","Sparkling Wine","Beers & Ciders","Spirits","Alcoholic Beverages","Beer, Wine & Spirits","Gin","Aperitif and Liqueur","Vodka","Tequila","Cream","Rum","Ciders","Lager","RTD","Bitters and Ale","Stout","Sparkling Brut Wine","Red wine","Rose wine","White wine","Whisky - Irish","Bourbon","Blended Scotch Whisky","Single Malt Scotch Whiskey","Champagne Demi Sec","Champagne Brut Blanc","Champagne Rose","Champagne - Brut Rose"," Champagne Brut","products"] }
		self.groceries_bundles = { '["Food & Drink","Laundry and Homecare", "Groceries", "Processes Food","Toiletries","Fresh Food","Groceries / Miscellaneous"]' : ["Agric Products"," Food","Processed Foods","Household Supplies","Food Cupboard","Toiletries","Tobacco & ECigarettes","Laundry & Homecare","Fresh Food","Bread & Bakery","Dish Washing Liquid","Floor Cleaner","Glass Cleaner","Hand Sanitizer","Hand Wash","Laundry Detergent","Sanitizers","Toilet Bowl Cleaner","food & drink","baskets","groceries","Scented Candles/Fragrances","Body Lotions, Butters & Creams"] }
		self.general_misc = {'["Watches", "General Accessories","General Miscellaneous"]' : ["Blow Out Sales","Clearance sales","Clearance Sale","Build Your Home-Cinema","Watch Accessories","unisex watches","All Watches","Aviator","Lunch In A Flash","Bundles","Tobacco & E-Cigarettes","Build your Home-Office","Rayban","Multi","Black","Gold","Analog","Analog & Digital","Digital","security & protection","New Arrivals","Sales","Youth","home","new in","sale","other accessories","Organisation & Storage","Girls On The Go","products" ]}



		self.sub_sub_categories = [self.kids_fashion, self.grooming_and_healthcare, self.diapering_and_daily_Care, self.pet_supplies, self.women_fashion, self.make_up, self.fragrances, 
		 self.hair_and_hair_care, self.health_and_wellbeing, self.sports_and_fitness, self.adult_toys, self.men_fashion, self.maternity_fashion, self.accessories_female, self.accessories_male,
		 self.fabric, self.video_games, self.board_games, self.solar_and_alernative_energy, self.generators_and_accessories, self.gift_bags_and_boxes, self.souvenirs, self.televisions_and_accessories, self.home_theaters, self.musical_instruments_and_equipments, self.auto_care_and_maintenance,
		 self.motorcycle, self.audio_books, self.books, self.kindles, self.school_and_office_supplies, self.sewing_machines_and_accessories, 
		 self.plumbing_materials, self.construction_materials, self.laptops, self.desktops_and_monitors, self.accessories_and_electronics,
		 self.office_stationary, self.interior_decor, self.garden_and_outdoor, self.mobile_phones, self.tablet, self.mobile_phones_and_tablet_accessories, 
		 self.insurance, self.nutrition, self.christmas, self.wedding_and_valentine, self.beverage, self.alcoholic_beverage, self.groceries_bundles, self.wearable_technology,self.general_misc]		
		#END Katlogg Sub Categories
		#END Katlogg Sub Categories
		#END Katlogg Sub Categories


		#Convert all values in list to lower case to completely match
		lowercase_list = []
		for each_sub in self.sub_sub_categories:
			for key, value in each_sub.items():
				for item in value:
					item = item.lower().strip()
					item.replace("'","")
					lowercase_list.append(item)

			each_sub[key] = lowercase_list
			lowercase_list = []


	def __str__(self):
		return('All Items:', self.items)


	def product_detail(self):
		each_item = self.get_item_from_link(self.starting_url)
		if each_item["current_price"] is None:
			#print("Not Added")
			return
		else:
			self.items.append(each_item)
			return


	def find_needle(self, needle, haystack):
		counted = Counter(haystack.split())[needle]
		return counted



	def get_item_from_link(self, link):
			
			start_page = requests.get(link)
			# time.sleep(10)
			tree = html.fromstring(start_page.text)
			# time.sleep(10)

			url = link
			#IF more than one xpath was supplied
			if ',' in self.product_name:
				for link in self.product_name.split(','):
					current_name = tree.xpath(link)
					if current_name != []:
						break
				#print("Initial Current Price", current_prices)
				name = list_to_string(current_name)
				try:
					name_in_title_case = name.title()
				except:
					name_in_title_case=[]

			else:
				names = tree.xpath(self.product_name)
				print("Product name: ", names)
				name = list_to_string(names)
				try:
					name_in_title_case = name.title()
				except:
					name_in_title_case=[]




			if self.product_color == '':
				color = []
				colors = name_in_title_case
				for each in self.colors:
					if each in colors:
						color.append(each)
				if len(color) == 0:
					color = ["Not Available in Colors"]
				#print('Colors is', color)
			else:
				colors = tree.xpath(self.product_color)
				color = filter_list_colors(colors)


			if '.' in self.product_seller:
				seller = self.product_seller
			
			elif ',' in self.product_seller:
				for link in self.product_seller.split(','):
					sellers = tree.xpath(link)
					if sellers != []:
						break
				seller = seller_availability(sellers)
			else:
				sellers = tree.xpath(self.product_seller)
				seller = seller_availability(sellers)

		
			if ',' in self.product_current_price:
				for link in self.product_current_price.split(','):
					current_prices = tree.xpath(link)
					print("This Current Price: ", current_prices, " Xpath is: ", link)
					if current_prices != []:
						break
				current_price = current_price_availability(current_prices)
			else:
				current_prices  = tree.xpath(self.product_current_price)

				#Doing it here cos fashpa price xpath has no comma
				if self.project == "fashpa.com":
					nameIndex = current_prices.index(name) 
					print("Product Price name match at index: ", nameIndex)
						
					#Dollar Price
					curry_price_index = current_prices[nameIndex+1]

					#Remove Dollar symbol
					curry_price_index = curry_price_index[2:]

					#Remove USD from behind and .00
					curry_price_index = curry_price_index[:-7]

					# 361.52
					#Naira Equiv
					naira_equiv = round(int(curry_price_index) * 361.52, 2)



					# print("Current Price Dollar: ", curry_price_index)
					print("Current Price Naira: ", naira_equiv)
					current_price = naira_equiv
				else:
					current_price = current_price_availability(current_prices)

			#Fix for Bestbuysforless.com.ng
			if ',' in self.product_old_price:
				old_price_check = self.product_old_price.split(',')
				old_check = tree.xpath(old_price_check[1])
				if old_check == []:
					old_price = old_price_availability(old_check)
				else:
					old_prices = tree.xpath(old_price_check[0])
					old_price = old_price_availability(old_prices)
			else:
				old_prices  = tree.xpath(self.product_old_price)
				old_price = old_price_availability(old_prices)
			
			
			categories = tree.xpath(self.product_categories)
			categories = list_items_to_categories(categories)
			

			sizes  = tree.xpath(self.product_sizes)
			valid_sizes = sizes_availability(sizes)
			if "Not Available in Sizes" not in valid_sizes:
				valid_sizes = list_items_to_string(valid_sizes)
			
			percentage_off = tree.xpath(self.product_percentage_off)
			off = off_availability(percentage_off)

			
			#Fix For Buyless.com.ng
			if ',' in self.product_images:
				for link in self.product_images.split(','):
					current_images = tree.xpath(link)
					print('Current Images', current_images)
					if current_images != []:
						break
				#Fix for Dreamcare.com.ng
				
				for index, image in enumerate(current_images):
					#Images hosted over CDNs
					if (self.project == "delphimetals.com") or (self.project == "fashpa.com"):
						pass
					elif ('http' not in image) and (self.project not in image):
						new_image = 'http://'+self.project+'/'+image
						current_images[index] = new_image
				valid_images = get_valid_images(current_images)

			else:
				#print('Images Xpath', self.product_images)	
				images = tree.xpath(self.product_images)
				print("Initial valid_images is", images)

				if self.project == "ng.fashpa.com":
					new_image_arr = []
					for img in images:
						if (".jpg" in img) or (".png" in img):
							new_image_arr.append(img)

					firstImglen = len(new_image_arr[0])

					final_list = []
					for each in new_image_arr:
						if len(each) == firstImglen:
							final_list.append(each)

					print("\nProduct URL: ", self.starting_url, "\nValid Selected Images Are: ", final_list)
					valid_images = get_valid_images(final_list)

				
				else:
					#Fix for Dreamcare.com.ng
					for index, image in enumerate(images):
						#Images hosted over CDNs
						if (self.project == "delphimetals.com") or (self.project == "fashpa.com"):
							pass
						elif ('http' not in image) and (self.project not in image):
							new_image = 'http://'+self.project+'/'+image
							images[index] = new_image
					#print("Initial 2 valid_images is", images)
					valid_images = get_valid_images(images)
					#print("valid_images is", valid_images)

			

			#Fix For Dreamcare.com.ng
			if ',' in self.product_description:
				for link in self.product_description.split(','):
					current_description = tree.xpath(link)
					#print('Current description', current_description)
					if current_description != []:
						break
				valid_description = description_availability(current_description)
			
			else:
				description = tree.xpath(self.product_description)
				#print('Initial Description', description)
				valid_description = description_availability(description)



			#Work on Categories
			#Work on valid_description

			maleCount = 0
			femaleCount = 0
			productGender = ""

			categories = categories.lower()
			haystacks = ""

			for each_category in categories.split(','):
				haystacks += " " + each_category

			maleNeedles = ["man", "male", "males", "male's", "boy", "men", "boys", "guy", "guys", "men's", "boy's", "guy's", "gentlemen", "gent", "gents", "gent's"]
			femaleNeedles = ["woman", "women", "women's", "girl", "girls", "ladies", "lady", "girl's", "female", "females"]
	

			for each in maleNeedles:
				maleCount += self.find_needle(each, haystacks)



			for each in femaleNeedles:
				femaleCount += self.find_needle(each, haystacks)


			if( (maleCount > 0) and (femaleCount == 0) ):
				#Its a Male Product tag it as Male for Gender
				productGender = "M"
				#Instantiate MaleCount back to zero
				maleCount = 0

			elif((maleCount == 0) and (femaleCount > 0)):
				#its a Female Product we tag it as Female for Gender
				productGender = "F"
				#Instantiate Female Count back to Zero
				femaleCount = 0

			else:
				if (self.project == "fashpa.com") or (self.project == "ng.fashpa.com") or (self.project == "girlyessentials.com.ng"):
					productGender = "F"
				else:
					productGender = "U"
					maleCount = 0
					femaleCount = 0

			#NO FILTER STORES MANIPULATION AREA
			#NO FILTER STORES MANIPULATION AREA
			#NO FILTER STORES MANIPULATION AREA
			#NO FILTER STORES MANIPULATION AREA
			#NO FILTER STORES MANIPULATION AREA
			#NO FILTER STORES MANIPULATION AREA
			#NO FILTER STORES MANIPULATION AREA
			if( (self.product_sub_sub_categories == "") or (self.product_sub_sub_categories is None)):
				#self.product_sub_sub_categories = "Not Assigned"
				if categories[-1:] is ",":
					categories = categories[:-1]
				each_category = categories.split(",")

				#WE WRITE FIX FOR baffshqboutique.com
				if self.project == "baffshqboutique.com":
					if "zaron cosmetics" in each_category:
						self.product_sub_sub_categories = "Cosmetics"

					elif "missguided" in each_category:
						self.product_sub_sub_categories = "Jeans & Jeggings"

					elif "kids" in each_category:
						self.product_sub_sub_categories = "Kids Fashion"

					elif "adidas" in each_category:
						self.product_sub_sub_categories = "Women Shoes"

					elif "perfumes" in each_category:
						self.product_sub_sub_categories = "Perfumes"

					elif "polo shirts" in each_category:
						self.product_sub_sub_categories = "Polo Shirts"

					elif "baffs haute" in each_category:
						self.product_sub_sub_categories = "Mens Fashion"

					elif "zaraman" in each_category:
						self.product_sub_sub_categories = "Men's shoes"

					elif "men joggers" in each_category:
						self.product_sub_sub_categories = "Joggers"

					elif "watches" in each_category:
						self.product_sub_sub_categories = "Watches"

					else:
						#We assign this filter gotten from the category
						if len(each_category) < 3:
							self.product_sub_sub_categories = each_category[-1]
						else:
							self.product_sub_sub_categories = each_category[-2]

				if self.project == "bellevistaworld.com":
					if ("fashion & clothings" in each_category) and ("men" in each_category):
						self.product_sub_sub_categories = "Mens Fashion"

					elif ("fashion & clothings" in each_category) and ("women" in each_category):
						self.product_sub_sub_categories = "Women's Fashion"

					else:
						#We assign this filter gotten from the category
						if len(each_category) < 3:
							self.product_sub_sub_categories = each_category[-1]
						else:
							self.product_sub_sub_categories = each_category[-2]

				if self.project == "bestbuyforless.com.ng":
					if ("men" in each_category) and ("shoes" in each_category):
						self.product_sub_sub_categories = "Men's shoes"
					else:
						#We assign this filter gotten from the category
						if len(each_category) < 3:
							self.product_sub_sub_categories = each_category[-1]
						else:
							self.product_sub_sub_categories = each_category[-2]

				if self.project == "gafunk.info":
					if "tablet- mr tab" in each_category:
						self.product_sub_sub_categories = "Tablets"

					elif ("software- microsoft office" in each_category) or ("software norton antivirus" in each_category) or ("software - operating system" in each_category) or ("software - kaspersky antivirus" in each_category)  or ("server hp" in each_category):
						self.product_sub_sub_categories = "Software"

					elif ("printer- epson" in each_category) or ("printer - hp" in each_category):
						self.product_sub_sub_categories = "printers"

					elif ("notebooks- hp" in each_category):
						self.product_sub_sub_categories = "Laptops"

					elif ("motherboards/processors" in each_category):
						self.product_sub_sub_categories = "motherboards and printers"

					else:
						#We assign this filter gotten from the category
						if len(each_category) < 3:
							self.product_sub_sub_categories = each_category[-1]
						else:
							self.product_sub_sub_categories = each_category[-2]

				if self.project == "amaget.com":
					if "washers & dryers" in each_category:
						self.product_sub_sub_categories = "washing machine"

					elif "macbook" in each_category:
						self.product_sub_sub_categories = "MacBooks"

					elif "notebooks" in each_category:
						self.product_sub_sub_categories = "Notebooks"

					else:
						#We assign this filter gotten from the category
						if len(each_category) < 3:
							self.product_sub_sub_categories = each_category[-1]
						else:
							self.product_sub_sub_categories = each_category[-2]

				if self.project == "delphimetals.com":
					self.product_sub_sub_categories = "Female Jewellery"

				if self.project == "femtechit.com":

					if len(each_category) == 2:
						last_one = each_category[-1]
						last_one_list = last_one.split()

						if ("game" in last_one_list) or ("gamepad" in last_one_list):
							self.product_sub_sub_categories = "Games Misc"


						elif ("printer" in last_one_list) or ("laserjet" in last_one_list):
							self.product_sub_sub_categories = "printers"

				if self.project == "fashpa.com":
					if len(each_category) == 2:
						last_one = each_category[-1]

						if "jewellery" == last_one:
							self.product_sub_sub_categories = "Female Jewellery"

						elif "bags" == last_one:
							self.product_sub_sub_categories = "Female Bags"

						else:								
							#We assign this filter gotten from the category
							if len(each_category) < 3:
								self.product_sub_sub_categories = each_category[-1]
							else:
								self.product_sub_sub_categories = each_category[-2]

				if self.project == "emtabinteriors.com":

					if "storage" in categories:
						self.product_sub_sub_categories = "outdoor furniture"

					elif "uncategorized" in categories:
						self.product_sub_sub_categories = "outdoor furniture"


					else:
						#We assign this filter gotten from the category
						if len(each_category) < 3:
							self.product_sub_sub_categories = each_category[-1]
						else:
							self.product_sub_sub_categories = each_category[-2]

				if self.project == "dsclng.com":

					if "sony" in categories:
						self.product_sub_sub_categories = "Games Misc"

					else:
						#We assign this filter gotten from the category
						if len(each_category) < 3:
							self.product_sub_sub_categories = each_category[-1]
						else:
							self.product_sub_sub_categories = each_category[-2]

				else:
					#We assign this filter gotten from the category
					if len(each_category) < 3:
						self.product_sub_sub_categories = each_category[-1]
					else:
						self.product_sub_sub_categories = each_category[-2]




			#THIS IS TO FIX FOR ITEMS THAT CAME WITH FILTER - HOWEVER THEIR FILTER IS AMBIGUOUS "CLASHING WITH EXISTING ITEMS" AND ITEM IN CATEGORY TO PICK TO DIFFERENTIATE IS GENERIC
			#THIS IS TO FIX FOR ITEMS THAT CAME WITH FILTER - HOWEVER THEIR FILTER IS AMBIGUOUS "CLASHING WITH EXISTING ITEMS" AND ITEM IN CATEGORY TO PICK TO DIFFERENTIATE IS GENERIC
			#THIS IS TO FIX FOR ITEMS THAT CAME WITH FILTER - HOWEVER THEIR FILTER IS AMBIGUOUS "CLASHING WITH EXISTING ITEMS" AND ITEM IN CATEGORY TO PICK TO DIFFERENTIATE IS GENERIC
			#THIS IS TO FIX FOR ITEMS THAT CAME WITH FILTER - HOWEVER THEIR FILTER IS AMBIGUOUS "CLASHING WITH EXISTING ITEMS" AND ITEM IN CATEGORY TO PICK TO DIFFERENTIATE IS GENERIC
			#THIS IS TO FIX FOR ITEMS THAT CAME WITH FILTER - HOWEVER THEIR FILTER IS AMBIGUOUS "CLASHING WITH EXISTING ITEMS" AND ITEM IN CATEGORY TO PICK TO DIFFERENTIATE IS GENERIC
			else:

				if self.project == "girlyessentials.com.ng":
					if self.product_sub_sub_categories == "Accessories":
						self.product_sub_sub_categories = "Female Jewellery"





			


			#Here we have to decide which Sub category Haystack we are passing to Determine Function
			#or alternatively which one we selecting based on d filter text gotten
			haystack = "" #Initialize an empty string haystack

			#Loop thru each categories we listed
			for sub_cat in self.sub_sub_categories:
			#Get Key, value pair - values are already converted to lower case
				for key, value in sub_cat.items():
					#Make needle suitable for comparison
					comparingVar = self.product_sub_sub_categories.lower().strip()
					comparingVar.replace("'","")
					#taking in to consideration items dived by slashes
					for val in value:
						if "/" in val:
							valSplit = val.split("/")
							for item in valSplit:
								if comparingVar == item.strip():
									haystack = key
									#Don't Break - Check for another occurence and decide for male / female
									break
						elif comparingVar == val:
							haystack = key
							break
							#Don't Break - Check for another occurence and decide for male / female


			#If the filter doesn't match any of our sub sub filtered items we automatically assign Miscallaneous
			if((haystack == "") or (haystack is None) ):
				print("I '",self.product_sub_sub_categories,"' wasn't found in sub_sub_categories Values so assigned MISCALLANEAOUS from Detailed Page")
				result = "donotaddtokatlogg"
				# result = "Wasn't in Katlogg Categories" + " | " + self.product_sub_sub_categories

			else:
				haystack = ast.literal_eval(haystack)
				selectedName = DetermineCategory(self.product_sub_sub_categories, haystack)
				result = selectedName.assignCategory()
				result = result + " | " + self.product_sub_sub_categories


			each_item = {'name':name, 'seller':seller, 'current_price':current_price, 'old_price':old_price, 'url':url, 'categories':categories, 'valid_sizes':valid_sizes, 'off':off, 'valid_images':valid_images[0], 'images_url':valid_images[1], 'store_name':get_store_name(self.starting_url), 'gender':productGender, 'sub_sub': result, 'color':color, 'description':valid_description}
			return each_item

'''
otedola = DetailCrawler('https://www.konga.com/crux-mens-flannel-red-lumberjack-shirt-3953065', "//div[@class='product-name']/text()", "", "//div[@class='col-lg-9 col-md-9 col-sm-9 nopadding']/div[@class='merchant-header']/a[@class='merchant-name']/text()", "//div[@class='purchase-actions']/span[@class='price']/text()", "//div[@class='purchase-actions']/span[@class='previous-price']/text()", '//div[@class="breadcrumbs"]/ul/li/a/text()',  "//div[@class='i_do_not_exists']", "//div[@class='i_do_not_exists']", '//div[@class="carousel-inner"]/div/img/@src', "//div[@class='product-long-description-brief']/p/text()")
otedola.product_detail()
for item in otedola.items:
	print(item)

'''
