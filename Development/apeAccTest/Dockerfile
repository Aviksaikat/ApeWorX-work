FROM ubuntu:latest

# Install dependencies
RUN apt-get update && apt-get install -y python3 python3-pip apt-utils git nano

# Set working directory
WORKDIR /app

# Copy the app to the container
COPY ./ape /app
COPY ./test_contracts /test_contracts

# Install app dependencies
RUN pip3 install .
