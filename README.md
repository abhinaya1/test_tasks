# Dockerfile
To build the Docker image, navigate to the directory containing the Dockerfile and run the following command  
```docker build -t my-node-app```

Replace "my-node-app" with the desired name for your Docker image.  
To run a container using the built image, use the following command:  
```docker run -p 8080:8080 my-node-app```  

