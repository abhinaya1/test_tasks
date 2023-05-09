# Dockerfile
To build the Docker image, navigate to the directory containing the Dockerfile and run the following command  
```docker build -t my-node-app```

Replace "my-node-app" with the desired name for your Docker image.  
To run a container using the built image, use the following command:  
```docker run -p 8080:8080 my-node-app```    
This command maps port 8080 of the host machine to port 8080 of the container. Replace "my-node-app" with the actual image name if you used a different name during the build.

By following best practices, this Dockerfile:

1. Uses a lightweight Node.js base image (node:lts-alpine) to reduce the image size.
2. Sets the working directory to /app in the container.
3. Copies only the package.json and package-lock.json files first, and installs production dependencies using npm ci --only=production. This takes advantage of Docker's caching mechanism to avoid unnecessary reinstallation of dependencies if the package files haven't changed.
4. Copies the rest of the application code to the container.
5. Sets the PORT environment variable to 8080.
6. Exposes port 8080 from the container, allowing external access to the application.
7. Specifies the CMD instruction to start the application using node index.js when the container is launched.   

# Docker-compoase.yml  
Make sure to place this docker-compose.yml file in a directory alongside the node-js-getting-started directory (which contains your Node.js application code).  

Explanation:   

* The nodejs-app service builds the Node.js application using the specified Dockerfile and exposes port 8080 to the host.   
* The loki service uses the official Loki image, exposes port 3100 for communication, and mounts a loki-config.yaml file for configuration.   
* The promtail service uses the official Promtail image, mounts a promtail-config.yaml file for configuration, and mounts the host's /var/log directory to collect logs.   
* The grafana service uses the official Grafana image, exposes port 3000, depends on the loki service, mounts a grafana-data directory for persistent data storage, and installs the grafana-piechart-panel plugin.   

To use this setup:  

1. Create a loki-config.yaml file with the desired Loki configuration. You can refer to the Loki documentation for more details on configuring Loki: https://grafana.com/docs/loki/latest/configuration/.   
2. Create a promtail-config.yaml file with the desired Promtail configuration. You can refer to the Promtail documentation for more details on configuring Promtail: https://grafana.com/docs/loki/latest/clients/promtail/configuration/.   
3. Create an empty grafana-data directory in the same directory as the docker-compose.yml file to persist Grafana data.  
4. Open a terminal, navigate to the directory containing the docker-compose.yml file, and run the following command to start the services:  
```docker-compose up```   
5. Once the services are up and running, you can access the Node.js application at http://localhost:8080, Grafana at http://localhost:3000, and Loki at http://localhost:3100.   
The Node.js application's logs will be collected by Promtail and sent to Loki for storage and retrieval. You can then use Grafana to create visualizations and dashboards based on the collected logs.  


