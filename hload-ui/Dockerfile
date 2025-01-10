# Use the latest LTS version of Node.js
FROM node:18-alpine

# Set the working directory inside the container
WORKDIR /app

# Create package.json automatically (if it doesn't exist)
RUN npm init -y

# Install dependencies (you can replace this with your specific dependencies later)
RUN npm install react react-dom react-scripts --save

# Optionally, clean up after installation
RUN npm cache clean --force

# Copy the rest of your application files
COPY ../hload-ui .

# Optionally, build your app for production (if needed, for example, for React or Angular)
# RUN npm run build

# Expose the port your app runs on
EXPOSE 3000

# Define the command to run your app
CMD ["npm", "start"]