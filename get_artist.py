import requests
from bs4 import BeautifulSoup

#url = "https://www.google.com/search?q=participation+lineup+for+2024+ultra+music+festival&sca_esv=fc325e7f7fccddc8&ei=flTEZbLrEcay5NoPzbSC2AU&ved=2ahUKEwjB8deX8JqEAxX1D1kFHafoBjEQyNoBKAB6BAgUEAA&uact=5&oq=ultra+festival+24+&gs_lp=Egxnd3Mtd2l6LXNlcnAiEnVsdHJhIGZlc3RpdmFsIDI0ICoCCABIAFAAWABwAHgAkAEAmAEAoAEAqgEAuAEByAEA4gMEGAAgQQ&sclient=gws-wiz-serp&si=AKbGX_oavBeeVFoe2eBOBFV3YoNZo47HMuwgfzDepGeSMix7Cp0AN6WIF5NDt7UJK3yXfDDT0dQ5L9lKqhDUDNiXd4fsT7iVv3Wlc3LIaKxAUeQ6Ym16NWwB-EMNjwM1WHhdRVtbcmLO1metIwmrZ92SGr7gidCXapAeeAy46S2JYIUXFiam-_I%3D&ictx=1"
url = "https://www.google.com/search?sca_esv=251625fef293e270&ei=u5_FZf-JEaWt5NoPg-6_OA&q=participation+lineup+for+2024+coachella&kgmid=/g/11sw0c5ksl&ephep=2445020566991000508:-1&sa=X&ved=2ahUKEwi5tcSIrJ2EAxUstokEHXwuDOYQyNoBKAB6BAgSEAA&si=AKbGX_oavBeeVFoe2eBOBFV3YoNZo47HMuwgfzDepGeSMix7CnvQ-RbcXbUg9osuHG_hwsYwmfwpu-bdDU-1K9xCka7GAo6VqSoHGPxWFfTDMdnSWUR78dHCLjBJfpewRUYnxgnjSLzdEE7ZAGsjEWSYe89XCEpVztn5SFkru8Z8i87ZeLwLCkg%3D&ictx=1"

headers = {
    'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

# <span class="nxucXc CxwsZe">David Guetta</span>
span_list = soup.find_all("span","nxucXc CxwsZe")

artist_list = [span.text for span in soup.find_all("span","nxucXc CxwsZe")]