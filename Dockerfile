# Use official Node.js image as the base image
FROM node:latest

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY ./my-npm-project/* .

# Install dependencies
RUN npm install

# Copy the rest of the application files
COPY  . ./

# Expose the port the app will run on
EXPOSE 3000

# Run the build script
RUN npm run build

# Start the application
CMD ["npm", "start"]
