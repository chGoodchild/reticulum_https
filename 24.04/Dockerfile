FROM ubuntu:24.04
MAINTAINER Aleksandar Diklic "https://github.com/rastasheep"

ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages for Python and networking
RUN apt-get update && \
    apt-get install -y openssh-server python3 python3-pip && \
    mkdir -p /var/run/sshd

# Install Python packages
RUN pip3 install httpx  # Install HTTPX for HTTP requests

# Attempt to install RNS and LXMF via pip (replace with actual package names or installation commands)
RUN pip3 install RNS LXMF

# If RNS and LXMF are not available via pip and need to be installed from source, you might do:
# RUN apt-get install -y git
# RUN git clone <RNS_REPO_URL> /tmp/rns && cd /tmp/rns && python3 setup.py install
# RUN git clone <LXMF_REPO_URL> /tmp/lxmf && cd /tmp/lxmf && python3 setup.py install

# Setup SSH to allow root login with key authentication only and disable password authentication
RUN echo 'root:root' | chpasswd && \
    sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin prohibit-password/' /etc/ssh/sshd_config && \
    sed -ri 's/UsePAM yes/#UsePAM no/g' /etc/ssh/sshd_config && \
    sed -ri 's/^#?PasswordAuthentication\s+.*/PasswordAuthentication no/' /etc/ssh/sshd_config && \
    sed -ri 's/^#?PubkeyAuthentication\s+.*/PubkeyAuthentication yes/' /etc/ssh/sshd_config

COPY authorized_keys /root/.ssh/authorized_keys

# Set permissions for SSH keys
RUN mkdir -p /root/.ssh && \
    touch /root/.ssh/authorized_keys && \
    chmod 700 /root/.ssh && \
    chmod 600 /root/.ssh/authorized_keys && \
    chown -R root:root /root/.ssh

# Clean up APT when done.
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Mount the lxmf directory
VOLUME ["/lxmf"]

# Expose the SSH port
EXPOSE 22

# Set the working directory
WORKDIR /lxmf

# Run the LXMF server script when the container starts
CMD ["python3", "serve_lxmf.py"]

# Run SSHD in foreground
CMD ["/usr/sbin/sshd", "-D"]
