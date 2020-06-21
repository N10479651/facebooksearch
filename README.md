# Facebook MarketPlace Bot

A simple Python program for the Facebook Marketplace to allow for multiple location to be searched at a time.

# Setup/Run

Edit locations.cfg with your desired locations
```cfg
locations: ["brisbane", "sydney", "melbourne", "adelaide", "perth"]
```
Run the script
```bash
python market.py
```
# Additional Information

For best results set search radius to the maximum amount on the marketplace settings.

Locations are abbreviated differently, for example "Los Angeles" is defined as "la" in the marketplace url. You may need to check before updating the config file.
