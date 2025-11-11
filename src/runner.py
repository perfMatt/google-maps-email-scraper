thonimport json
import logging
from extractors.google_maps_parser import parse_google_maps_data
from extractors.email_extractor import extract_emails
from outputs.exporters import export_data

logging.basicConfig(level=logging.INFO)

def run_scraper():
    logging.info("Starting Google Maps Email Scraper...")

    try:
        with open("data/inputs.sample.json", "r") as file:
            input_data = json.load(file)

        businesses = parse_google_maps_data(input_data["keywords"], input_data["location"])
        logging.info(f"Found {len(businesses)} businesses.")

        for business in businesses:
            emails = extract_emails(business["website"])
            business["emails"] = emails

        export_data(businesses, "data/output.sample.json")
        logging.info("Scraping completed successfully.")

    except Exception as e:
        logging.error(f"Error during scraping: {e}")

if __name__ == "__main__":
    run_scraper()