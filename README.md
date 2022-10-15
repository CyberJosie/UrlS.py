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
usage: Endpoint Eye [-h] [--url URL] [--timeout TIMEOUT] [--exclude EXCLUDE] [--proxy PROXY]
                    [--headers HEADERS] [--data DATA]

Quickly get a glimpse of available HTTP request methods allowed (or not) at a specific endpoint to
identify important information for further investigation.

optional arguments:
  -h, --help            show this help message and exit
  --url URL, -u URL     URL (host + endpoint together) to investigate.
  --timeout TIMEOUT, -t TIMEOUT
                        Max seconds to wait for each server response.
  --exclude EXCLUDE, -ex EXCLUDE
                        Comma separated list of HTTP request methods to NOT CHECK. (Errors ignored)
  --proxy PROXY, -rp PROXY
                        Proxy to send requests through.
  --headers HEADERS, -rh HEADERS
                        JSON serializable string with custom headers (Optional)
  --data DATA, -rd DATA
                        Custom JSON data (Optional)

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
