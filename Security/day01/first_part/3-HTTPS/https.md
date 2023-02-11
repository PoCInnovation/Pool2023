Write a Python program that generates an SSL/TLS certificate and uses it to secure an HTTP server. The program should prompt the user for the necessary information to create the certificate, such as the common name (CN) and organization name (O).

To generate the certificate, you can use a tool such as OpenSSL. The program should generate a private key, create a certificate signing request (CSR) using the private key and the user-provided information, and sign the CSR to create the certificate.

Once the certificate is generated, the program should use it to secure the HTTP server by wrapping the server socket with an ssl.SSLContext object and calling the wrap_socket() method. The program should also allow the user to specify options such as the SSL/TLS protocol to use and the certificate expiration date.

Hint: You can use the openssl command-line tool to generate the private key, CSR, and certificate, or you can use the cryptography library to perform these tasks in Python.