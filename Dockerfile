# Use a lightweight Node.js base image with the LTS version
FROM node:lts-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install production dependencies
RUN npm ci --only=production

# Copy the rest of the application code to the container
COPY . .

# Set the environment variables
ENV PORT=8080

# Expose the port the app will listen on
EXPOSE $PORT

# Start the application
CMD [ "node", "index.js" ]
