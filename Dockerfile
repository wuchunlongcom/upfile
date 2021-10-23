FROM maodouzi/django:v2.2.6-oracleclient-v19.3
LABEL purpose='Upfile Search'

# Build folder
RUN mkdir -p /home/www/upfile/logs \
    && mkdir -p /home/www/upfile/tool \
    && mkdir -p /home/www/upfile/src
WORKDIR /home/www/upfile
COPY mysite /home/www/upfile/src/mysite
COPY requirements.txt /home/www/upfile/requirements.txt
RUN rm -rf /home/www/upfile/src/mysite/initdb.py \
    && rm -rf /home/www/upfile/src/mysite/syncdb.py \
    && rm -rf /home/www/upfile/src/mysite/static \
    && pip3 install -r /home/www/upfile/requirements.txt \
    && cd /home/www/upfile/src/mysite && python3 manage.py collectstatic

# Setup nginx
RUN rm /etc/nginx/sites-enabled/default
ADD docker-config/nginx.conf /etc/nginx/sites-available/ecustCourseInfo.conf
RUN ln -s /etc/nginx/sites-available/ecustCourseInfo.conf /etc/nginx/sites-enabled/ecustCourseInfo.conf
# RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# # Setup supervisord
# RUN mkdir -p /var/log/supervisor
# COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
# COPY gunicorn.conf /etc/supervisor/conf.d/gunicorn.conf

# run sh. Start processes in docker-compose.yml
#CMD ["/usr/bin/supervisord"]
ADD docker-config/supervisord.conf /etc/supervisor/supervisord.conf
ADD docker-config/supervisor.conf /etc/supervisor/conf.d/ecustCourseInfo.conf
ADD docker-config/start.sh /tmp/start.sh
EXPOSE 80
CMD [ "sh", "/tmp/start.sh" ]
