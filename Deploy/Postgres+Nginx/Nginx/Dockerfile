FROM nginx:latest
RUN apt-get update && apt-get install gettext-base
ENV PROXY_PROTOCOL=http PROXY_UPSTREAM=example.com
COPY ./Nginx/proxy.conf /etc/nginx/sites-available/default.template
COPY ./Nginx/start.sh /
CMD ["/start.sh"]