# UrlS.py
UrlS.py Quickly gathers information available at a URL for multiple HTTP request methods

# Supported Methods:
* GET
* POST
* PUT
* HEAD
* DELETE
* OPTIONS
* PATCH


# Response Information Summary
Information gathered for each method:
* Endpoint availability
* Response Status Code (and English meaning)
* Response Content Type
* Response Content Length

# Installation

```
wget 
python3 eye.py --help
```


# Usage

```
usage: URL Spy [-h] [--url URL] [--url-file URL_FILE] [--timeout TIMEOUT] [--exclude EXCLUDE]
               [--proxy PROXY] [--output OUTPUT] [--output-format OUTPUT_FORMAT]

Quickly check the availability of mulitple HTTP request methods of a URL
and discover necessary information for further analysis.

This is not meant to be a replacement for the existing tools used for this purpose
(e.g Postman), it is meant to be used as a pre-analysis tool intended to save
you time crafing custom HTTP requests and analyzing endpoints. By using this tool
you can quickly identify key attributes of an endpoint.

            * URL Availability
            * Status Code (and English meaning)
            * Response Payload
            * Response Content Type
            * Response Size

optional arguments:
  -h, --help            show this help message and exit
  --url URL, -u URL     
                        URL (host and endpoint together) to investigate.
                        Default: None
                        Required: True
                        
  --url-file URL_FILE, -uf URL_FILE
                        
                        Path to file of URLs to analyze. (URLs are newline separated).
                        Default: None
                        Required: True (If a single URL is not given)
                        
  --timeout TIMEOUT, -t TIMEOUT
                        
                        Max seconds to wait for each server response
                        Default: 10
                        Required: False
                        
  --exclude EXCLUDE, -ex EXCLUDE
                        
                        Comma separated list of HTTP request methods to NOT CHECK. Errors ignored.
                        Default: GET,POST,PUT,HEAD,DELETE,OPTIONS,PATCH
                        Required: False
                        
  --proxy PROXY, -rp PROXY
                        
                        Proxy to send requests through
                        Default: None
                        Required: False
                        
  --output OUTPUT, -o OUTPUT
                        
                        Path to redirect output to.
                        Default: Print to STDOUT
                        Required: False
                        
  --output-format OUTPUT_FORMAT, -fmt OUTPUT_FORMAT
                        
                        Formatting to export output as. Options: JSON, CSV, greppable
                        Default: JSON (If only output flag is given, else there is no default)
                        Required: False
                        

Find on GitHub: https://github.com/CyberJosie/URLs.py

```

# Examples

Scan all methods except `PATCH` over the Tor network using a 15 second max HTTP timeout
```
python3 eye.py \
  --url https://stackoverflow.com/users/login \
  --proxy socks5://127.0.0.1:9050 \
  --timeout 15 \
  --exclude PATCH
```
```
URL: https://stackoverflow.com/users/login
Duration: 21.854 seconds
 

 Request Method: GET
  Request Completed: True
  Status: 200 (OK)
  Response Content Type: text/html; charset=utf-8
  Response Size: Approx. 47365 Bytes
 

 Request Method: POST
  Request Completed: True
  Status: 200 (OK)
  Response Content Type: text/html; charset=utf-8
  Response Size: Approx. 47491 Bytes
 

 Request Method: PUT
  Request Completed: True
  Status: 404 (Not Found)
  Response Content Type: text/html; charset=utf-8
  Response Size: Approx. 44978 Bytes
 

 Request Method: HEAD
  Request Completed: True
  Status: 200 (OK)
  Response Content Type: text/html; charset=utf-8
  Response Size: Approx. 0 Bytes
 

 Request Method: DELETE
  Request Completed: True
  Status: 404 (Not Found)
  Response Content Type: text/html; charset=utf-8
  Response Size: Approx. 44980 Bytes
 

 Request Method: OPTIONS
  Request Completed: True
  Status: 404 (Not Found)
  Response Content Type: text/html; charset=utf-8
  Response Size: Approx. 44980 Bytes

```
