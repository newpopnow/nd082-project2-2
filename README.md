# Overview

In this project, you will build an Azure App Service from Python, Continous Intergration by Github Actions and Continous Delivery by Azure Devops Pipelines

Diagram:

![alt](/img/diagram.drawio.png)

## Project Plan

* Trello board: https://trello.com/invite/b/HEmxDjEt/ATTI7c5939b49a59653fffed9068da7d1550299A572E/nd082-project2
* Project plan: <>

## Instructions

<TODO:  
* Architectural Diagram (Shows how key parts of the system work)>

<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

* Project running on Azure App Service

* Project cloned into Azure Cloud Shell

![alt](/img/project_cloned_to_azure_cloud_shell.png)

* Passing tests that are displayed after running the `make all` command from the `Makefile`

![alt](/img/venv_passing_test_Makefile.png)

* Output of a test run

![alt](/img/github_action_pass.png)

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>

