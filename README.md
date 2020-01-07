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

Task #3: kubernetes security

* Created ServiceAccount's bob (cluster-admin role).
* Created ServiceAccount's dave (no access).
* Created namespaces prometheus, dev.
* Created ServiceAccount's carol (ns prometheus).
* Created role pod-reader (get, list, watch).
* Created ServiceAccount's jane (ns dev, admin role).
* Created ServiceAccount's ken (ns dev, view role).
