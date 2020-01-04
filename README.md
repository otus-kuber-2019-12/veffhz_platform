# veffhz_platform
veffhz Platform repository

Task #1: kubernetes intro

* Created Docker image with Python web server (kubernetes-intro/web/Dockerfile)
* Created Kubernetes manifest file for pod with containers and initContainer specs (kubernetes-intro/web-pod.yaml)
* Fixed broken frontend pod (Hipster Shop) (kubernetes-intro/frontend-pod-healthy.yaml)
  
Task #2: kubernetes controllers

* Created kubernetes kind cluster.
* Created ReplicaSet manifest for frontend & paymentservice.
* Created Deployment manifest with different strategy for paymentservice.
* Created Daemonset manifest for node-exporter with control-plane nodes.

