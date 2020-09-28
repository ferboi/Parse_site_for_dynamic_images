# Parse_site_for_dynamic_images
This python script helps to determine if the images used by a site is hosted on the same machine used to host the site.

Basically, using the urllib.request package it opens the passed url, and parses the site using beautifulsoup package for image tags, of which the image tags are opened automatically by firefox browser.
Note: If no image is returned by the site. It therefore means that all images used by the site is hosted on the same machine hosting the site and possibly everyother content on the site.
