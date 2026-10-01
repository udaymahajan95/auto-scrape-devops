import json
from scraper.scraper import CarScraper

def main():
    url = "https://example.com"
  
    scraper = CarScraper(url)
   
    result = scraper.run()
  
    print("Scraping Completed.")
   
    print(result)

    #save scraped data as a JSON
    with open("scraped_data.json", "w") as file:
        json.dump(result, file, indent=4)

    print("Data saved to scraped_data.json")

if __name__ == "__main__":
    main()	
