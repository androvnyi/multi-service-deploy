## Multi-Service Deploy (Flask + PostgreSQL + Nginx)

### Project Overview
This project demonstrates how to fully automate the deployment of multiple services on a remote server using **Ansible** and **Docker Compose**.

After running a single Ansible playbook, the production server will automatically start three containers:
- **Flask API** – a simple Python backend application
- **PostgreSQL** – a database used by the API
- **Nginx** – a reverse proxy that routes incoming traffic to the API

The automation covers:
- Installing and configuring Docker & Docker Compose
- Deploying application code and configuration files
- Setting up secrets via **Ansible Vault**
- Running the complete service stack with `docker-compose`

---

### Why This Project Is Useful
This setup is a practical example of a **multi-service deployment pipeline**.  
By building it, you will practice:
- Using **Ansible** for server automation
- Managing sensitive data with **Ansible Vault**
- Writing `docker-compose.yml` for a multi-container environment
- Building and deploying a Python API
- Setting up Nginx as a reverse proxy
- Orchestrating services with environment variables and health checks

This is close to a real-world production workflow used by DevOps engineers.

---

### Tech Stack
- **Ansible** – automation and provisioning
- **Docker** – containerization
- **Docker Compose** – multi-service orchestration
- **Python + Flask** – API implementation
- **PostgreSQL** – database
- **Nginx** – reverse proxy

---

### High-Level Deployment Flow
1. **Local (Dev Machine)** – You run the Ansible playbook targeting the production server.
2. **Ansible Tasks** – Install Docker & Compose, copy application files, templates, configs, and secrets.
3. **Docker Compose** – Starts PostgreSQL, Flask API, and Nginx in the correct order with health checks.
4. **Result** – Your services are running and accessible via the server’s IP.

---

### Repository Structure
```
 ansible/
├─ ansible.cfg
├─ inventory.ini
├─ playbook.yml
├─ group_vars/
│  └─ prod.yml
├─ vault/
│  └─ secrets.yml
└─ roles/
   ├─ docker/
   │  ├─ tasks/
   │  └─ files/
   ├─ app/
   │  ├─ tasks/
   │  └─ files/
   ├─ nginx/
   │  ├─ tasks/
   │  └─ files/
   └─ compose/
      ├─ tasks/
      └─ files/ 
```



