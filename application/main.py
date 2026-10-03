import json
import os
import boto3

from scraper.scraper import CarScraper


BUCKET_NAME = "auto-scrape-devops-bucket-986156380297"
S3_KEY = "automotive/scraped_data.json"


def upload_to_s3(file_path):
    session = boto3.Session(profile_name="autoscrape")
    s3 = session.client("s3")

    s3.upload_file(
        file_path,
        BUCKET_NAME,
        S3_KEY
    )

    print(f"Uploaded {file_path} to s3://{BUCKET_NAME}/{S3_KEY}")


def main():

    url = os.getenv("SCRAPER_URL")

    if not url:
        raise ValueError(
            "SCRAPER_URL environment variable is not set."
        )

    scraper = CarScraper(url)

    result = scraper.run()

    print("Scraping completed.")
    print(f"Total listings: {result['total_listings']}")

    output_file = "scraped_data.json"

    with open(output_file, "w") as file:
        json.dump(result, file, indent=4)

    print(f"Data saved to {output_file}")

    upload_to_s3(output_file)


if __name__ == "__main__":
    main()

