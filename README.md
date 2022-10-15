# URL_S.py
URL S.PY Quickly gathers information on an HTTP endpoint about different available request methods.

# URL SPY

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
