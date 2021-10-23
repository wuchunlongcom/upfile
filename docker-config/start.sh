#!/bin/bash

[ -f /home/www/upfile/src/mysite/data/init.sh ] && sh /home/www/upfile/src/mysite/data/init.sh

nginx
/usr/bin/supervisord -c /etc/supervisor/supervisord.conf
