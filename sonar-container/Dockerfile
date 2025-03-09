# Use an official Node.js image as the base image
FROM openjdk:11-jre-slim

# Install necessary dependencies for sonar-scanner
RUN apt-get update && apt-get install -y \
    unzip \
    curl \
    openjdk-11-jdk

# Download and install sonar-scanner
RUN curl -sSLo /tmp/sonar-scanner.zip https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.6.2.2472-linux.zip && \
    unzip /tmp/sonar-scanner.zip -d /opt && \
    rm /tmp/sonar-scanner.zip

# Set environment variables for sonar-scanner
ENV SONAR_SCANNER_HOME=/opt/sonar-scanner-4.6.2.2472-linux
ENV PATH=$SONAR_SCANNER_HOME/bin:$PATH

# Set the working directory
WORKDIR /usr/src/app

# No ENTRYPOINT, this will be provided in the docker run command
