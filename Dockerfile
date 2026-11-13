FROM nginx:alpine

# Copy nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy site contents
COPY . /usr/share/nginx/html

# Clean repository administrative files from the web root
RUN rm -rf /usr/share/nginx/html/.git \
    /usr/share/nginx/html/tasks \
    /usr/share/nginx/html/scripts \
    /usr/share/nginx/html/task-helper.sh \
    /usr/share/nginx/html/Dockerfile \
    /usr/share/nginx/html/docker-compose.yml \
    /usr/share/nginx/html/*.sh \
    /usr/share/nginx/html/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
