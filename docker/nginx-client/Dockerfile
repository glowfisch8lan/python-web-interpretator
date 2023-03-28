FROM node:16.15.1

RUN apt-get update && apt-get install -y nginx

EXPOSE 80

ADD config/nginx.conf /etc/nginx/nginx.conf
CMD ["nginx"]