import requests
from bs4 import BeautifulSoup

def check_xss_vulnerabilities(url):
    try:
        # Send HTTP GET request to the specified URL
        response = requests.get(url)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')
            # Find all input fields
            input_fields = soup.find_all('input')
            for input_field in input_fields:
                # Check if the input field allows for user input
                if input_field.get('type') == 'text' or input_field.get('type') == 'textarea':
                    # Check if the input field is vulnerable to XSS
                    test_payload = "<script>alert('XSS Vulnerability Found!');</script>"
                    input_field['value'] = test_payload
                    # Send modified request
                    test_response = requests.post(url, data=soup)
                    # Check if the payload is reflected in the response
                    if test_payload in test_response.text:
                        print(f"Potential XSS vulnerability found in input field: {input_field}")
        else:
            print(f"Failed to retrieve the page. Status Code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Example usage
    target_url = "https://example.com"
    check_xss_vulnerabilities(target_url)
