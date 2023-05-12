import pandas as pd
from redfin_scraper import RedfinScraper

# Initialize and set up RedfinScraper
scraper = RedfinScraper()
scraper.setup(zip_database_path="./zip_code_database.csv")

# Scrape real estate data for 77006 and 77019 zip codes in Houston, TX
scraper.scrape(city_states=["Houston,TX"], 
               zip_codes=["77006"],lat_tuner=.2, lon_tuner=.2)

# Get scraped data for 77006 and 77019 zip codes
data_77006 = scraper.get_data(id="D001")

# Convert scraped data to DataFrames
df_77006 = pd.DataFrame(data_77006)

# Concatenate DataFrames and write to CSV file
df_concat = pd.concat([df_77006], ignore_index=True)
df_concat.to_csv("redfin_data.csv", index=False)

