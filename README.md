SkyTemple Banner
================
This repository contains a banner and a link assosiated with it. This banner
will be displayed in SkyTemple, SkyTemple Randomizer and related apps.
Clicking on it opens the link.

# File Structure
- `enable`: A simple text file that contains "0" or "1". If it is "1", the banner is enabled.
- `banner.png`: The banner to display if `enable` contains "1". This must be 580x126px PNG.
- `banner_url`: The URL to open when clicking on the banner.

# Contributing
To submit a new banner, open a Pull Request where `enable` is changed to "1" and `banner.png` and `banner_url`
contain the banner and URL you want to use.

Yor banner must be 580x126px PNG.

# Using the banner
You can use this banner in a SkyTemple, PMDCollab or related project using the following URLs:

- https://release.skytemple.org/banner.png: Is the banner.
- https://release.skytemple.org/banner: Contains the URL to send to when clicking the banner.

Any of these two URLs will return a 404 status if the banner is currently disabled.
