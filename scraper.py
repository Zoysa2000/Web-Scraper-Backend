import requests
from bs4 import BeautifulSoup
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def fetch_job_listings(keyword, location, start):
    base_url = f"https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={keyword}&location={location}&start={start}"
    try:
        response = requests.get(base_url, headers=HEADERS)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching jobs at offset {start}: {e}")
        return None

def parse_jobs(html):
    soup = BeautifulSoup(html, 'html.parser')
    job_cards = soup.find_all('li')
    jobs = []
    for index, job in enumerate(job_cards):
        try:
            title = job.find('h3').text.strip()
            company = job.find('h4').text.strip()
            location = job.find('span', class_='job-search-card__location').text.strip()
            link_tag = job.find('a', href=True)
            link = link_tag['href']
            if link.startswith('/'):
                link = "https://www.linkedin.com" + link
            jobs.append({
                "Job Title": title,
                "Company Name": company,
                "Location": location,
                "Job URL": link
            })
        except Exception as e:
            print(f"Error parsing job at index {index}: {e}")
            continue
    return jobs

def scrape_linkedin_jobs(keyword="AI Engineer", location="USA"):
    keyword = keyword.replace(" ", "+")
    location = location.replace(" ", "+")
    all_jobs = []
    for start in range(0, 75, 25):
        html = fetch_job_listings(keyword, location, start)
        if html:
            jobs = parse_jobs(html)
            all_jobs.extend(jobs)
        time.sleep(1)
    return all_jobs

