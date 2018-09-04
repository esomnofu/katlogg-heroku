#Module for Neural Network
from products.searchengine import *
#from products.nn import *

from products.general import *
from products.detect_changes import *
from products.filter_category_crawler import FilterCategoryCrawler
from products.detailed_view import DetailCrawler
import datetime
                            

def check_fourth_or_fifth_layer(set1_texts, set1_urls, fourthlayerfilters, alreadypicked, urls, start_page_number, end_page_number, concatenation_pattern, product_url, product_filters, product_filters_texts, product_name, product_color, product_seller, product_current_price, product_old_price, product_categories, product_sizes, product_percentage_off, product_images, product_description, data, faker, arg, argz,  crawler_project, category_name):
	master_list = []
	for key, value in set1_texts.items():
		for each_fourth in fourthlayerfilters:
			#print("Each Fourth is: ", each_fourth, " value is : ", value)
			if each_fourth.lower() == value.lower():
				#We checked if we have already crawled this before
				if each_fourth.lower() in alreadypicked:
					pass
					print(each_fourth, " is already crawled...")
				else:
					#Append this filter as already crawled --- The code below crawls it
					alreadypicked.append(each_fourth.lower())
					print("We need to crawl the url of this fourth layer : ", each_fourth, " so we pass this key (when key is put inside dict - it produces the filter url): ", key)
					
					#We are Looping thru all the 4th Layer filter URLs found to see if any matches what we need to crawl at that layer
					for each_fourth_url in set1_urls:
						print("each Fourth URL is: ", each_fourth_url)



					#{'http://konga.com/kids-furniture', 'http://konga.com/kids-bath', 'http://konga.com/kids-room-decor'}
					#{'kids-bath': "Kids' Bath", 'kids-furniture': "Kids' Furniture", 'kids-room-decor': "Kids' Room Decor"}


						#Possibly Fix for Jumia
						if each_fourth_url.endswith("/"):
							pass
							print("Jumia - Do not split - full url passed as key")
						else:
							each_fourth_url_list = each_fourth_url.split('/')
							print("key is still : ", key, " Array splitted is: ", each_fourth_url_list)




							if key in each_fourth_url_list:
								print("We running FilterCategoryCrawler on this url: ", each_fourth_url)
								#We visit this URL Filter link "each_fourth_url i.e pet supplies" 
								#We get all products links to crawl from there
								#Lastly we check if there are any filter urls there we might need also

								#We Recall Filter Function to get all products url and filters also we pass current url "each_fourth_url"
								each_fourth_url_crawler = FilterCategoryCrawler(each_fourth_url, start_page_number, end_page_number, concatenation_pattern, product_url, product_filters, product_filters_texts)
								each_fourth_url_crawler.crawl()
								set_to_file(each_fourth_url_crawler.items, urls)							
								matrix = NeuralCrawler('searchindex.db')

								
								four_fourth_items = each_fourth_url_crawler.items

								#We need to return both of this to check fifth layer
								#We need to return both of this to check fifth layer
								#We need to return both of this to check fifth layer
								fifth_layer_urls = each_fourth_url_crawler.fourth_layer_urls
								fifth_layer_texts = each_fourth_url_crawler.fourth_layer_urls_texts



								temp_list = {str(fifth_layer_urls) : fifth_layer_texts}
								print("Appending to master list is : ", temp_list)
								master_list.append(temp_list)
								
								#As at this level
								#1 - We have all products url of this filter to pass to Detailed View Class
								#2 Fifth layer urls and text to recall and check for more filters


								for item in four_fourth_items:
								# for item in list(four_fourth_items)[:10]:
									#Let Us Index and Add Each Info From All Products Category to our Neural Network Databases Before Getting their Full Info With our DetailCrawler
									#Let Us Index and Add Each Info From All Products Category to our Neural Network Databases Before Getting their Full Info With our DetailCrawler
									#Let Us Index and Add Each Info From All Products Category to our Neural Network Databases Before Getting their Full Info With our DetailCrawler
									#matrix.crawl(item)
									#End of Neural Functionality
									#End of Neural Functionality
									#End of Neural Functionality


									#We want to get SUb Sub Filter Text for this Product
									#Possibly Fix for Jumia
									if each_fourth_url.endswith("/"):
										product_sub_sub_categories = each_fourth_url

									else:
										actual_filter_names = each_fourth_url.split('/')
										product_sub_sub_categories = actual_filter_names[-1]
									print("The Filter / Sub Category we are fixating at is: ", product_sub_sub_categories)
									sub_sub = set1_texts[product_sub_sub_categories]
									print("The Sub Sub Filter is: ", sub_sub)

									product_info = DetailCrawler(item, product_name, product_color, product_seller, product_current_price, product_old_price, product_categories, product_sizes, product_percentage_off, product_images, product_description, sub_sub)
									product_info.product_detail()


									for items in product_info.items:
										data['product'].append(items)
										faker['product'].append(items)
										#time.sleep(5)

								the_url = os.path.join('products/' + crawler_project+' - '+str(datetime.date.today())+'/'+category_name +'/'+category_name+'_products_'+category_name+'_'+str(datetime.date.today())+'.txt')
								if not os.path.isfile(the_url):
									print('Created Dictionary Object Information File :',  crawler_project+' - '+str(datetime.date.today())+'/'+category_name+'/'+category_name+'_products_'+category_name+'_'+str(datetime.date.today())+'.txt')
									write_file(the_url, '')

								with open(the_url, 'w' ) as outfile:
									json.dump(faker, outfile)
								
								#We call the news function to work on the newly created product object file and add it to Mysql Product and News Database
								#And also add any product that has altered in attributes(i.e Price) to the News Table
								#The News Function Handles all these for us
								news(arg, argz)

								#The Set is Cleared after each Category is crawled and saved to file
								four_fourth_items.clear()

								#The Set is Cleared after each Full Product Information is crawled and saved to file
								try:
									product_info.items.clear()
								except:
									pass

								faker = {}  
								faker['product'] = []
	print("The Master List for this Level of Deep Layer: ", set1_texts, " is: ", master_list)								
	return master_list
						
							


