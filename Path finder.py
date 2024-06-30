import requests
import random
import string

def get_url_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            return None
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

def random_combination(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def find_alive_urls(base_url, num_trials):
    alive_urls = []
    for _ in range(num_trials):
        combination = random_combination(4)
        new_url = base_url.format(combination)
        print("Testing URL:", new_url)
        data = get_url_data(new_url)
        if data:
            print("Data from alive URL found with pattern:", combination)
            alive_urls.append(new_url)

    if alive_urls:
        print("Alive URLs:")
        for url in alive_urls:
            print(url)
    else:
        print("No alive URLs found")

# Example usage
base_url = "https://www.google.com/{}/"
num_trials = 20000  # Number of random combinations to try
find_alive_urls(base_url, num_trials)
