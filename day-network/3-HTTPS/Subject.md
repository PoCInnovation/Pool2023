In this exercise, you will add HTTPS support to a simple server that you can found in the repo. The server should be able to serve a static HTML page to clients over a secure HTTPS connection.

To complete this exercise, you will need to do the following:

1.  Generate a self-signed SSL/TLS certificate for your server. This will allow your server to establish an encrypted HTTPS connection with clients.
    
2.  Configure your server to use the SSL/TLS certificate and to listen for HTTPS connections on port 443.
    
3.  Update your server to serve the static HTML page over HTTPS instead of HTTP. The server should still handle GET requests and return a 200 OK status code and the contents of the HTML page when the request URL is '/'.
    
4.  Test your server by using a web browser to make HTTPS requests to the server and verify that it responds correctly. You may need to add an exception in your web browser to trust the self-signed certificate.