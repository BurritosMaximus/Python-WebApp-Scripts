import requests

def extract_links(url):
    acceptable_status_codes = [200, 301, 302, 307]  # Add more status codes as needed
    try:
        response = requests.get(url)
        if response.status_code in acceptable_status_codes:
            return set(response.text.split('<a href="')[1:])
        else:
            print("Failed to fetch the page. Status code:", response.status_code)
            return None
    except Exception as e:
        print("An error occurred:", e)
        return None

def main():
    url = input("Enter the URL to scrape: ")
    links = extract_links(url)
    if links:
        print("Extracted links:")
        for link in links:
            print(link.split('"')[0])

if __name__ == "__main__":
    main()
