# Lightweight System Monitor (Flask + Docker)

A minimalistic Python microservice designed to provide real-time system health metrics via a REST API. 

## ✨ Key Features
* **Environment Injection:** Dynamically fetches host configuration using environment variables.
* **Resource Monitoring:** Tracks CPU and Memory utilization using `psutil`.
* **Dockerized Architecture:** Fully containerized for seamless deployment across environments.
* **Production-Ready:** Implements non-root user execution and safe host binding.

## 🛠 Tech Stack
* Python 3.11 / Flask
* Docker
* psutil
