FROM ubuntu:24.04

# Install base dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    python3 \
    python3-pip \
    openjdk-21-jdk \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set up Python environment
ENV PYTHONPATH=/usr/local/lib/python3/dist-packages
RUN pip3 install --no-cache-dir pipenv

# Set up Java environment
ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64

# Create CPJ workspace
WORKDIR /cpj
COPY . .

# Build CPJ
RUN make clean && make all

# Add CPJ to PATH
ENV PATH="/cpj/bin:${PATH}"

# Default command
CMD ["bash"]