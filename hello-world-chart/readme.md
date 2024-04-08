# DevOps Pipeline Project

## Description

This project demonstrates a simple DevOps pipeline using Docker, Kubernetes, and Helm. The pipeline is designed around a basic Python application that prints "Hello, World!" to showcase the end-to-end process of containerizing an application, managing it with Kubernetes, and automating deployment with Helm.

## Features

- Python "Hello World" application to demonstrate the pipeline.
- Docker for containerising the application.
- Kubernetes deployment to manage the application at scale.
- Helm chart for easy application deployment and versioning.
- Scripts for automated setup and deployment.

## Prerequisites

To run this project, you'll need:
- Docker installed on your machine. [Installation guide](https://docs.docker.com/get-docker/)
- Kubernetes cluster setup, which can be done using Minikube. [Minikube setup](https://minikube.sigs.k8s.io/docs/start/)
- Helm for managing Kubernetes applications. [Helm installation](https://helm.sh/docs/intro/install/)

## Installation

1. Clone this repository to your local machine.
   git clone <repository-url>

2. Navigate into the project directory.
   cd <project-directory>

## Usage

To run the Python application in a Docker container:
1. Build the Docker image:
   docker build -t hello-world-app

2. Run the Docker container:
   docker run -p 5000:5000 hello-world-app

#Deployment

The project includes a Kubernetes deployment configuration and a Helm chart for deployment. To deploy the application to your Kubernetes cluster:

1.Apply the Kubernetes deployment:
kubectl apply -f hello-deployment.yaml

2. Install the Helm chart:
   helm install hello-world-app ./hello-world-chart
