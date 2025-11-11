thonimport requests
from bs4 import BeautifulSoup

def extract_emails(website_url):
    emails = []
    try:
        response = requests.get(website_url)
        soup = BeautifulSoup(response.text, "html.parser")
        for a_tag in soup.find_all('a', href=True):
            if "mailto:" in a_tag['href']:
                emails.append(a_tag['href'].replace("mailto:", ""))
    except Exception as e:
        print(f"Error extracting emails from {website_url}: {e}")
    return emails