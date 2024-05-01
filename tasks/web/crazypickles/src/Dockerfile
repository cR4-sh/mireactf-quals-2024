FROM php:7.4-apache

RUN apt-get update && \
    apt-get install -y libonig-dev libzip-dev zip supervisor && \
    docker-php-ext-install pdo_mysql mbstring zip && \
    a2enmod rewrite 

COPY static /var/www/html/static
COPY templates /var/www/html/templates
COPY calculate.php /var/www/html/
COPY index.php /var/www/html/
COPY somescript.py /var/www/html/


RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

WORKDIR /var/www/html

COPY mailcards.txt /tmp
COPY composer.json ./

RUN composer install --no-plugins --no-scripts

RUN apt install sudo
RUN chmod 777 /usr/lib/python3.9/re.py
RUN chmod 744 /var/www/html/somescript.py
RUN echo "www-data ALL=(root) NOPASSWD: /usr/bin/python3.9 /var/www/html/somescript.py /tmp/mailcards.txt" >> /etc/sudoers

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

ENTRYPOINT ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
