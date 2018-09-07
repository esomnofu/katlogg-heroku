import requests

def counted_words_at_url(url):
	print("count_words_at_url request is gotten...")
    resp = requests.get(url)
	print("count_words_at_url response is: ", resp)
	print("Last response is: ", resp.text.split())
    return len(resp.text.split())