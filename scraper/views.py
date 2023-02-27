import os
import json
from django.shortcuts import render
from scraper.scrape import scrape_url, scrape_content, get_valid_link
# Create your views here.


def scrap_companies():
    print(os.getcwd())
    file = open("/Users/imshakil/Desktop/DevskillDjangoCourse/coding/jobsBD/jobsbd/scraper/resource.json")
    data = json.load(file)
    items = []
    for company in data["companies"]:
        name = company["companyName"]
        url = company["url"]
        print("looking jobs for: ", company)
        if not company["jobs_list"]["tag"]:
            continue

        try:
            tag = company["jobs_list"]
            jobs = scrape_url(url)
            jobs = jobs.find_all(tag["tag"], {"class": tag["class"], "id": tag["id"]})
            for job in jobs:
                content = scrape_content(str(job))
                path = content.find("a")
                if path is not None:
                    path = path.get("href")
                    link = get_valid_link(path)
                    if not link:
                        link = url + path
                        print(link)
                    item = content.get_text().strip().split("\n")
                    item = [itm.strip() for itm in item if len(itm) > 0]
                    job_item = dict()
                    job_item['link'] = link
                    job_item['title'] = item[0]
                    job_item['description'] = item
                    print(item)
                    items.append(job_item)
        except Exception as e:
            pass
    return items


def openning(request):
    items = scrap_companies()
    items = {"items": items}
    print(items)
    return render(request, 'load_job.html', items)
