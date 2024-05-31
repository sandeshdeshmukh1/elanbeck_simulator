# syntax = docker/dockerfile:experimental
# Use a multi-stage build to optimize the final image
FROM node:17.4.0-alpine3.14

# tzdata = to be able to set the correct timezone
ARG rundeps="tzdata rsync"

# Install apk dependencies
RUN --mount=type=cache,target=/var/cache/apk \
    apk update \
    && apk --progress add $rundeps

# Create a non-root user
RUN adduser -D -g '' sandeshdeshmukh

# Set the working directory
WORKDIR /install

# Copy package files separately for better Docker caching
COPY package.json package-lock.json ./

# Install node packages
RUN --mount=type=cache,target=/home/sandeshdeshmukh/.npm \
    npm ci

# Change the ownership of node_modules and create npm cache directory
RUN chown -R sandeshdeshmukh:sandeshdeshmukh /install/node_modules \
    && mkdir -p /home/sandeshdeshmukh/.npm \
    && chown -R sandeshdeshmukh:sandeshdeshmukh /home/sandeshdeshmukh/.npm

# Set environment variable for npm cache
ENV NPM_CONFIG_CACHE=/home/sandeshdeshmukh/.npm

# Add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# Set the working directory for the app
WORKDIR /app

# Copy the start script and application files
COPY ./docker-start.sh /start.sh
RUN chmod +x /start.sh
COPY . .

# Ensure application files are owned by the non-root user
RUN chown -R sandeshdeshmukh:sandeshdeshmukh /app

# Switch to the non-root user
USER sandeshdeshmukh

# Uses port which is used by the actual application
EXPOSE 3000

# Finally runs the application
CMD [ "/start.sh" ]