[![Python application test with Github Actions](https://github.com/newpopnow/nd082-project2-2/actions/workflows/main.yml/badge.svg)](https://github.com/newpopnow/nd082-project2-2/actions/workflows/main.yml)

# Overview

In this project, you will build an Azure App Service from Python, Continous Intergration by Github Actions and Continous Delivery by Azure Devops Pipelines

## Project Plan

* Trello board: https://trello.com/invite/b/HEmxDjEt/ATTI7c5939b49a59653fffed9068da7d1550299A572E/nd082-project2
* Project plan: <>

## Instructions

<TODO:  
* Architectural Diagram (Shows how key parts of the system work)>

Diagram:

![alt](/img/diagram.drawio.png)

<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

* Project running on Azure App Service

* Project cloned into Azure Cloud Shell

![alt](/img/project_cloned_to_azure_cloud_shell.png)

Run command to create Virtual Enviroment
```
cd /nd082-project2-2 #change directory to project folder
python3 -m venv venv
source venv/bin/activate
```

* Passing tests that are displayed after running the `make all` command from the `Makefile`

![alt](/img/venv_passing_test_Makefile.png)

* Output of a test run

![alt](/img/github_action_pass.png)

* Successful deploy of the project in Azure Pipelines.

![alt](/img/az_pipelines_run.png)

* Running Azure App Service from Azure Pipelines automatic deployment

![alt](/img/az_webapp_running.png)

* Successful prediction from deployed flask app in Azure Cloud Shell.

```bash
./make_predict_azure_app.sh
```

![alt](/img/make_prediction.png)

* Output of streamed log files from deployed application
```
az webapp log tail
```

![alt](/img/az_webapp_log_tail.png)

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>

