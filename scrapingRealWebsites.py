from bs4 import BeautifulSoup
import requests

print("Put skill that you are not familiar with ")
not_familiar_skills = input("> ")
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
#print(html_text)

soup = BeautifulSoup(html_text, "lxml")
jobs = soup.find_all("li", class_ = "clearfix job-bx wht-shd-bx")

for job in jobs:
    period_posted = job.find("span", class_="sim-posted").span.text.strip()

    if "few" in period_posted.lower():
        company_name = job.find("h3", class_= "joblist-comp-name").text.strip()
        key_skills = job.find("span", class_="srp-skills").text.strip().replace(' ','')
        period_posted = job.find("span", class_="sim-posted").span.text.strip()
        more_info = job.header.h2.a['href']

        key_skills.replace(","," ")
        not_skills_set = set(not_familiar_skills.lower().split())
        r_skills_set = set(key_skills.lower().split())
        if not not_skills_set.intersection(r_skills_set):
            print(f'''
            Company Name : {company_name}
            Required Skills : {key_skills}
            Period Posted : {period_posted}
            More Info : {more_info}
            ''')