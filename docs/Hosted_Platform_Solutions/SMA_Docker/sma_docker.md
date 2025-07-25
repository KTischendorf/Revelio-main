---
author: "Sasha Karcz"
date: "2024-12-11"
description: "SMA Docker Deployment in JHAHOSTING"
tags: ["Docker", "SMA", "seq", "rabbitmq", "redis"]
---

# SMA Service Management

This guide provides instructions for managing the `datalust/seq`, `rabbitmq:3-management`, and `redis` Docker containers for the SMA service. Follow the steps below to bring the container up or down, check its status, view logs, and understand port forwarding.

## Prerequisites

- Docker and Docker Compose installed on the host machine.
- Access to the terminal with appropriate permissions.

## Hosts

There are currently two hosts running for this service:

| Host Name                    |  IP Address     |
|------------------------------|-----------------|
| `atxsmalnx01.jhahosting.com` | `10.218.42.138` |
| `bmosmalnx01.jhahosting.com` | `10.238.59.140` |


## Docker Compose

This deployment is managed via a [Docker Compose](https://docs.docker.com/compose/) file. You can access the file by going to the following directory:

```bash
cd /opt/sma
```

```bash
/opt/sma# tree -L 2
.
├── docker-compose.yaml <-- This is the compose file
├── rabbit_mq           <-- This is the persistent data for rabbitmq
│   └── mnesia
├── README.md           <-- This is this README but on the server
└── seq_data            <-- This is the persistent data for seq
    ├── Backups
    ├── Documents
    ├── Init
    ├── Logs
    ├── Seq.json
    └── Stream

```

### Bringing the Container Up

To start the all of the containers, navigate to the directory containing the `docker-compose.yml` file and run:

```bash
docker compose up -d
```

The `-d` flag runs the container in detached mode, allowing it to run in the background.

### Bringing the Container Down

To stop and remove the all the containers, run:

```bash
docker compose down
```

This command stops the container and removes the associated resources.

### Checking Container Status

To check the status of the containers, use the following command:

```bash
docker compose ps
```

This command lists the running containers and their status.

### Viewing Logs

To view the logs of the all the containers, run:

```bash
docker compose logs
```

or, for a specific container (`seq` for example):

```bash
docker compose logs seq
```

To view the logs live and follow them, run:

```bash
docker compose logs -f
```

### Restarting the Container

To restart all the containers, use:

```bash
docker compose restart
```

or for one container (`seq` for example):

```bash
docker compose restart seq
```

### Viewing All Containers

To view all Docker containers (running and stopped), use:

```bash
docker ps -a
```

## Port Forwarding

The seq service is configured to expose the following ports:

- **80**: HTTP port for accessing the `seq` web interface.
- **5341**: Ingestion port for `seq` events.
- **6379**: Ingestion port for Redis.
- **5672**: Ingestion port for RabbitMQ messages.
- **15672**: HTTP port for RabbitMQ management interface.


You can access the `seq` web interface by navigating to `http://bmosmalnx01.jhahosting.com` in a web browser from a Windows host with ACLs configured, or, via [SSH port forwarding](https://www.cyberciti.biz/faq/ssh-port-forwarding-tunneling/).

## Manual Deployment

This was manually deployed as network ACLs had blocked all access to Docker. Below are the steps to build the hosts by hand.

### Transfer Debian packages

Transfer the following Debian packages to the remote host:

1. containerd.io_1.7.24-1_amd64.deb
2. docker-buildx-plugin_0.19.2-1~ubuntu.22.04~jammy_amd64.deb
3. docker-ce_27.4.0-1~ubuntu.22.04~jammy_amd64.deb
4. docker-ce-cli_27.4.0-1~ubuntu.22.04~jammy_amd64.deb
5. docker-ce-rootless-extras_27.4.0-1~ubuntu.22.04~jammy_amd64.deb
6. docker-compose-plugin_2.31.0-1~ubuntu.22.04~jammy_amd64.deb
7. docker-scan-plugin_0.23.0~ubuntu-jammy_amd64.deb

### Install the Debian packages

`ssh` to the remote host. Change directories to where the Debian packages are (if not in your home directory). Then install them via `dpkg`:

```bash
sudo dpkg -i *.deb
```

### Transfer tar of Docker images

Transfer the following tarballs to the remote host:

1. rabbitmq_image.tar
2. redis_image.tar
3. seq_image.tar

### Load the Docker images

`ssh` to the remote host. Change directories to where the tarballs are (if not in your home directory). Then load them into Docker:

```bash
sudo docker load -i rabbitmq_image.tar
```

```bash
sudo docker load -i redis_image.tar
```

```bash
sudo docker load -i seq_image.tar
```

### Create a Docker Compose file

Make a new directory:

```bash
sudo mkdir /opt/sma && sudo chmod 755 /opt/sma
```

Create a new file for Docker Compose:

```bash
sudo nano /opt/sma/docker-compose.yaml
```

Paste the following content:

```bash
---
services:
  seq:
    container_name: ${HOST}_seq
    restart: unless-stopped
    environment:
      - ACCEPT_EULA=Y
      - SEQ_API_CANONICALURI=http://${HOST}.jhahosting.com
      - SEQ_FIRSTRUN_ADMINPASSWORDHASH=${SEQ_ADMIN_PASSWORD_HASH}
    volumes:
      - ./seq_data:/data
    ports:
      - 80:80
      - 5341:5341
    image: seq-with-curl:latest
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:80/health" ]
      interval: 30s
      timeout: 10s
      retries: 3

  rabbitmq:
    container_name: ${HOST}_rabbitmq
    image: rabbitmq:3-management
    restart: unless-stopped
    ports:
      - 5672:5672
      - 15672:15672
    environment:
      - RABBITMQ_DEFAULT_USER=${RABBITMQ_DEFAULT_USER}
      - RABBITMQ_DEFAULT_PASS=${RABBITMQ_DEFAULT_PASS}
    volumes:
      - ./rabbit_mq:/var/lib/rabbitmq
    healthcheck:
      test: ["CMD", "rabbitmqctl", "status"]
      interval: 30s
      timeout: 10s
      retries: 3

  redis:
    container_name: ${HOST}_redis
    image: redis:latest
    restart: unless-stopped
    ports:
      - 6379:6379
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 30s
      timeout: 10s
      retries: 3
```

### Create an environmental variable file

Create a new file:

```bash
sudo nano /opt/sma/.env
```

With the following content:

```bash
SEQ_ADMIN_PASSWORD_HASH=REDACTED
RABBITMQ_DEFAULT_USER=admin
RABBITMQ_DEFAULT_PASS=REDACTED
HOST=enter_your_host_name_here
```

You can generate the SEQ_ADMIN_PASSWORD_HASH via:

```bash
echo '${ENTER_YOUR_PASSWORD_HERE}' | docker run --rm -i datalust/seq config hash
```

#### Example `.env` file

```bash
echo 'p@ssw0rd' | docker run --rm -i datalust/seq config hash
FCfNlV8nyAIBkrXHtKGK3A6rJ15CFPNykGLdEsi98tUeqFInZg==
```

In this case, the `.env` file would look like:

```bash
SEQ_ADMIN_PASSWORD_HASH=FCfNlV8nyAIBkrXHtKGK3A6rJ15CFPNykGLdEsi98tUeqFInZg==
RABBITMQ_DEFAULT_USER=admin
RABBITMQ_DEFAULT_PASS='p@ssw0rd'
HOST=foobar
```
