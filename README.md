# LinkedIn Job Scraper

This Python script scrapes job listings from LinkedIn’s public job search API endpoint and extracts key job details including job title, company name, location, and job URL.

---

## Features

- Scrapes job postings for a given keyword and location
- Extracts job title, company name, location, and job URL
- Handles pagination by fetching multiple pages 
- Uses `requests` and `BeautifulSoup` for HTTP requests and HTML parsing
- Includes basic error handling and polite delays between requests

---

## End Point Check with POSTMAN
![Screenshot (1385)](https://github.com/user-attachments/assets/6204afac-5e10-4f01-b95d-70e8d21bdb12)

## Requirements

- Python 3.6+
- `requests` library
- `beautifulsoup4` library

Install dependencies with:

```bash
pip install requests beautifulsoup4


