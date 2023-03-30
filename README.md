[![Python application test with Github Actions](https://github.com/newpopnow/nd082-project2-2/actions/workflows/main.yml/badge.svg)](https://github.com/newpopnow/nd082-project2-2/actions/workflows/main.yml)

# Overview

In this project, you will build an Web app from Python then deploy to PaaS - Azure App Service, Continous Intergration by Github Actions and Continous Delivery by Azure Devops Pipelines

## Project Plan

* Trello board: https://trello.com/invite/b/HEmxDjEt/ATTI7c5939b49a59653fffed9068da7d1550299A572E/nd082-project2
* Project plan: <>

## Instructions

<TODO:  
* Architectural Diagram

![alt](/img/diagram.drawio.png)

- Github: Source code repository
- Github Actions: Continuous Intergration (CI)
- Azure Devops Pipelines: Continous Delivery (CD)
- Azure App Service: PaaS which host the application

### Let's start

* Project running on Azure App Service

* To clone source code into Azure Cloud Shell

```
git clone https://github.com/newpopnow/nd082-project2-2.git
```

![alt](/img/project_cloned_to_azure_cloud_shell.png)

Run command to create Virtual Enviroment
```
cd /nd082-project2-2 #change directory to project folder
python3 -m venv venv
source venv/bin/activate
```

* Passing tests that are displayed after running the `make all` command

![alt](/img/venv_passing_test_Makefile.png)

* Output of a test run

![alt](/img/github_action_pass.png)

* Running Azure App Service by script `commands.sh`

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



* Successful deploy of the project in Azure Pipelines.

![alt](/img/az_pipelines_run.png)





* Locust load test
On local machine, run following
```
pip install locust
locust
```
Open locust interface at http://localhost:8089, configure and start load test

![alt](/img/locust_new_load_test.png)

![alt](/img/locust_load_test.png)

## Enhancements

Try to package and run the app in Kubernetes enviroment

## Demo 

<TODO: Add link Screencast on YouTube>

