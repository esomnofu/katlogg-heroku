"""
A HELPER FILE
=============
DOMAIN FUNCTIONS DEFINED HERE
HELPS EXTRACT THE DOMAIN NAME FROM A URL
THIS WILL HELP US WHEN CREATING FOLDERS 
FOR DIFFERENT  SITES WE WILL CRAWL
"""
from urllib.parse import urlparse


def get_store_name(url):
	try:
		if get_full_domain_name(url) == "ng.fashpa.com":
			return "Fashpa Nigeria"
		else:
			results = get_sub_domain_name(url).split('.')
			if (len(results[-1]) == 2) and (len(results) > 3) :
				return results[-3]
			return results[-2]
	except:
		return ''

def get_domain_name(url):
	try:
		results = get_sub_domain_name(url).split('.')

		if (len(results[-1]) == 2) and (len(results[-2]) == 3):
			return results[-3] +'.'+results[-2] +'.'+ results[-1]
		else:
			return results[-2] +'.'+ results[-1]
	except:
		return ''


def get_full_domain_name(url):
	try:
		ans=""
		results = get_sub_domain_name(url).split('.')
		for each in results:
			ans += each+"."
		return ans[:-1]

	except:
		return ''


def get_sub_domain_name(url):
	try:
		return urlparse(url).netloc
	except:
		return ''

