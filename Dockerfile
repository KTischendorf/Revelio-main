# Use the latest Alpine image
FROM alpine:latest

# Install necessary packages
RUN apk add --no-cache git curl jq tar

# Install GitLeaks
RUN curl -sSfL https://github.com/gitleaks/gitleaks/releases/download/v8.22.0/gitleaks_8.22.0_linux_x64.tar.gz -o gitleaks.tar.gz \
    && tar -xzf gitleaks.tar.gz -C /usr/local/bin gitleaks \
    && chmod +x /usr/local/bin/gitleaks \
    && rm gitleaks.tar.gz

# Configure Git to trust the directory
RUN git config --global --add safe.directory /repo

# Set the entrypoint to GitLeaks
ENTRYPOINT ["gitleaks"]
