from scrapyd_client import ScrapydClient

client = ScrapydClient()

print('projects')
# for project in client.projects():
#     print(client.jobs(project=project))

project_name = "webscraper"
# jobs = client.jobs(project=project_name)
# print('jobs ', jobs)

client.schedule(project=project_name,
                spider="webpage_spider",
                args={
                    "url":"https://scrapyd.readthedocs.io/en/stable/overview.html",
                    "run_id": "scrapyd_overview"
                })