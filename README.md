### A simple udp server and client messaging app

- Python3
- Credit to https://github.com/Marthevin/python-socket-udp-server-client-example

### Two docker images are available on Dockerhub:

- starchx/python-udp-server:latest
- starchx/python-udp-server-nginx-healthcheck:latest

### Example k8s deployment file:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: python-udp-server-deployment
  labels:
    app: python-udp-server
spec:
  replicas: 1
  selector:
    matchLabels:
      app: python-udp-server
  template:
    metadata:
      labels:
        app: python-udp-server
    spec:
      containers:
      - name: python-udp-server
        image: starchx/python-udp-server:latest
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "256Mi"
            cpu: "250m"
      - name: nginx-healthcheck
        image: starchx/python-udp-server-nginx-healthcheck:latest
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "256Mi"
            cpu: "250m"
```

### Example K8s service file

As per: https://github.com/kubernetes/kubernetes/pull/92109

```
apiVersion: v1
kind: Service
metadata:
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-type: nlb
  labels:
    app: python-udp-server
  name: python-udp-server
spec:
  externalTrafficPolicy: Cluster
  ports:
  - port: 90
    protocol: UDP
    targetPort: 9090
  selector:
    app: python-udp-server
  type: LoadBalancer
```