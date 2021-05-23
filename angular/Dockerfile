FROM nginx:1.17.1-alpine
COPY config/config.conf /etc/nginx/conf.d/default.conf
COPY app/src/sitemap.xml /usr/share/nginx/html/sitemap.xml
COPY app/src/robots.txt /usr/share/nginx/html/robots.txt
COPY app/dist/app /usr/share/nginx/html/
