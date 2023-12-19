import requests


def make_request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        return None


target_input = "google.com"

with open("subdomainlists.txt", "r") as subdomain_list:
    for word in subdomain_list:
        word = word.strip()
        url = "http://" + word + "." + target_input
        response = make_request(url)
        if response is not None:
            print("Found subdomain -----> " + url)
