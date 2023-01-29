FROM php:7.4-apache

# Set flag secret key
ENV FLAG=PoC{cRLf_C4n_BE_H4rd_7o_UndEr57AND}

COPY template/ /var/www/html/
EXPOSE 80
CMD ["apache2-foreground"]