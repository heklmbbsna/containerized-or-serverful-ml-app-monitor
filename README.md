## Containerized or Serverless Machine Learning

### Implementation & deployment architecture

The serverful Flask ML Application was deployed on a GCP VM Instance using Prometheus and Grafana for metrics and monitoring. All tied together using docker-compose.

The serverless version can be deployed on Google Cloud Functions & monitored using built-in dashboard.

### Install dependencies (serverful)

```
pip install -r api/requirements.txt
```

### Set up and deploy app using docker-compose (serverful)

```
docker-compose up
```

### Access

* API: http://localhost:8080
* Prometheus: http://localhost:9090
* Grafana: http://localhost:3000 `[username: admin, password: pass@123]`
