import json
import os
import requests
from dotenv import load_dotenv
from github import Github
from github import Auth

load_dotenv()
auth = Auth.Token(os.getenv("GITHUB_TOKEN"))

g = Github(auth=auth)
repo = g.get_repo("Wookhq/Lution")

class Workflow:
    def __init__(self):
        pass
    
    def listall_workflow(self):
        return repo.get_workflows()
    
    def run_workflow(self, workflow_id, branch="latest"):
        try:
            workflow = repo.get_workflow(workflow_id)
            workflow.create_dispatch(ref=branch)
            return True
        except Exception as e:
            raise e

    def listall_workflow_runs(self):
        return repo.get_workflow_runs()

    def infoworkflow(self, workflow_id):
        workflow = repo.get_workflow(workflow_id)
        return workflow
