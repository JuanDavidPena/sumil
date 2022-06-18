""" API with Github info integration, database control """
from fastapi import FastAPI
import urllib.request
from company import Company
from db import mydatabase
from developer import Developer
from project import Project

app = FastAPI()


""" GITHUB INFORMATION RETRIEVE """
@app.get("/readme")
async def readme(readme_link):
    """ Extract the readme from github """
    base = "https://raw.githubusercontent.com"
    readme_url = base + readme_link.replace("/blob/", "/").split(".com")[1]
    content = urllib.request.urlopen(readme_url).read()
    return content



""" DATABASE MANIPULATION """
""" DEVELOPER"""
@app.get("/developers")
async def all_developers():
    """ Extract all developers """
    devs = list(mydatabase.developers.find())
    return [Developer(**dev) for dev in devs]

""" COMPANY """
@app.get("/companies")
async def all_companies():
    """ Extract all companies """
    companies = list(mydatabase.companies.find())
    return [Company(**companies) for company in companies]

""" PROJECT """
@app.get("/projects")
async def all_projects():
    """ Extract all projects """
    projects = list(mydatabase.projects.find())
    return [Project(**project) for project in projects]

@app.post("/projects")
async def create_project(project: Project):
    """ Add a project to the database """
    mydatabase.projects.insert(project)
    return None
