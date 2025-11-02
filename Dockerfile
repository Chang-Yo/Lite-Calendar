# Use a Debian-based image with build tools
FROM debian:bullseye

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    cmake \
    g++ \
    python3-pyside6 \
    xvfb

# Copy the project
COPY . /app

# Build the C++ applications
RUN mkdir -p /app/build
WORKDIR /app/build
RUN cmake /app/src/cpp/notifier && make
RUN rm -rf *
RUN cmake /app/src/cpp/startup && make

# Install Python dependencies from requirements.txt
RUN pip3 install --no-cache-dir -r /app/src/python/requirements.txt

# Set the working directory for the Python application
WORKDIR /app/src/python

# Command to run the application with a virtual X server
CMD ["xvfb-run", "python3", "main.py"]
