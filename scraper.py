# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 16:53:24 2025

@author: Kirti
"""
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import re

def find_email_from_website(url):
    try:
        page = requests.get(url, timeout=5)
        soup = BeautifulSoup(page.text, 'html.parser')
        # Scrape visible text only
        text = soup.get_text()
        emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
        valid_emails = [email for email in emails if not email.endswith(('.png', '.jpg'))]
        return list(set(valid_emails))[:1]
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return []

def get_leads(keyword, location, results_count=10):
    query = f"{keyword} company in {location} site:linkedin.com OR site:.com"
    search_results = search(query, num_results=results_count)
    
    leads = []
    for url in search_results:
        email = find_email_from_website(url)
        company_name = url.split("//")[-1].split("/")[0].replace('www.', '')
        linkedin_query = f"{company_name} founder site:linkedin.com"
        linkedin = search(linkedin_query, num_results=1)
        
        leads.append({
            'Company URL': url,
            'Contact Email': email[0] if email else "Not Found",
            'Founder LinkedIn': list(linkedin)[0] if linkedin else "Not Found"
        })
    return leads
