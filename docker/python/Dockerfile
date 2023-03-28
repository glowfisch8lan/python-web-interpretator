FROM python:3.9.2
WORKDIR /app
RUN apt-get update && apt-get install -y nginx uwsgi supervisor apt-utils uwsgi-plugin-python3 uwsgi-plugin-python
EXPOSE 80
ADD nginx/nginx.conf /etc/nginx/nginx.conf
COPY supervisord.conf /etc/supervisor
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
#CMD ["flask", "run"]