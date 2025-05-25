"""
Scraping Rituals: An Annotated Script

This script scrapes weather data from a public source. But it is also a ritual:
a repeated invocation to a remote machine, shaped by politeness, rate limits,
and the negotiation of HTML structure.
"""

import requests
from bs4 import BeautifulSoup
import time

URL = "https://example.com/weather/today"

def fetch_weather():
    print("Invoking the weather spirits...")
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")
    temp = soup.find("div", class_="temperature").text.strip()
    print(f"Observed temperature: {temp}")
    return temp

if __name__ == "__main__":
    while True:
        try:
            temperature = fetch_weather()
        except Exception as e:
            print("Disruption in the ritual:", e)
        time.sleep(3600)  # Respectful interval
