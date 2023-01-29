FROM php:7.4-apache

# Set flag secret key, the flag is also in the config.php
ENV FLAG=PoC{f1LTEREvErytHIngIsNIce}

COPY template/ /var/www/html/
EXPOSE 80
CMD ["apache2-foreground"]