#!/bin/bash
docker build -t hello-world-app .
helm upgrade --install hello-world-app ./hello-world-chart --namespace hello-app-namespace