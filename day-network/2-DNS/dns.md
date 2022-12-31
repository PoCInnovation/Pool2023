In this exercise, you will create a program that performs advanced DNS lookups for a given domain name. The program should prompt the user for the domain name and the IP address of the DNS server to use, and should allow the user to specify the DNS record type to request (e.g. A, MX, CNAME, etc.). The program should display the results of the lookup for the specified record type.

To perform the lookup, you can use the socket module to send and receive DNS messages. You can use the gethostbyname() function to resolve a domain name to an IP address, and the getaddrinfo() function to resolve a domain name to a list of address info structures. Each address info structure contains an IP address and other relevant information such as the socket type and protocol.

In addition to performing basic DNS lookups, your program should also implement the following features:

1.  Support for performing recursive DNS lookups. The program should follow DNS referrals and resolve names that are not in the local cache by sending additional queries to the appropriate DNS servers.

2.  A simple DNS cache to store the results of previous DNS lookups. The program should check the cache before sending a query to a DNS server, and should update the cache with the results of the lookup.

3.  The ability to perform a DNS zone transfer to retrieve the complete list of records for a given domain. The program should parse the response and display the records in a user-friendly way.

4.  Support for EDNS (Extension mechanisms for DNS) to allow the program to send larger DNS packets and receive extended DNS responses.

5.  Support for DNSSEC (Domain Name System Security Extensions) to allow the program to verify the authenticity and integrity of DNS responses using digital signatures and public key encryption.

Hint: Use the AF_INET and SOCK_DGRAM constants from the socket module to create a UDP socket, and use the sendto() and recvfrom() functions to send and receive DNS messages. You can use the DNS header and DNS question structures defined in the struct module to create and parse DNS messages. You can also use the dnslib library to assist with advanced DNS features such as EDNS and DNSSEC.