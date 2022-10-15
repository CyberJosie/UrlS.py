import time
import requests
import argparse


STATUS_CODES = {

    # Informational
    100: 'Continue',
    101: 'Switching Protocols',
    102: 'Processing',
    102: 'Early Hints',

    # Successful
    200: 'OK',
    201: 'Created',
    202: 'Accepted',
    203: 'Non-Authoritative Information',
    204: 'No Content',
    205: 'Reset Content',
    206: 'Partial Content',
    207: 'Multu-Status (WebDAV)',
    208: 'Already Reported (WebDAV)',
    226: 'IM Used',

    # Redirection
    300: 'Multiple Choices',
    301: 'Moved Permanently',
    302: 'Found',
    303: 'See Other',
    304: 'Not Modified',
    305: 'Use Proxy (deprecated)',
    306: 'Unused',
    307: 'Temporary Redirect',
    308: 'Permanent Redirect',

    # Client Errors
    400: 'Bad Request',
    401: 'Unauthorized',
    402: 'Payment Required',
    403: 'Forbidden',
    404: 'Not Found',
    405: 'Method Not Allowed',
    406: 'Not Acceptible',
    407: 'Proxy Authentication Required',
    408: 'Request Timeout',
    409: 'Conflict',
    410: 'Gone',
    411: 'Length Required',
    412: 'Precondition Failed',
    413: 'Payload Too Large',
    414: 'URI Too Long',
    415: 'Unsupported Media Type',
    416: 'Range Not Satisfyable',
    417: 'Expectation Failed',
    418: 'I\'m a Teapot',
    421: 'Misdirected Request',
    422: 'Unprocessable Entity (WebDAV)',
    423: 'Locked (WebDAV)',
    424: 'Failed Dependency (WebDAV)',
    425: 'Too Early',
    426: 'Upgrade Required',
    428: 'Precondition Required',
    429: 'Too Many Requests',
    431: 'Request Header Fields Too Large',
    451: 'Unavailable For Legal Reasons',

    # Server Errors
    500: 'Internal Server Error',
    501: 'Not Implemented',
    502: 'Bad Gateway',
    503: 'Service Unavailable',
    504: 'Gateway Timeout',
    505: 'HTTP Version Not Supported',
    506: 'Variant Also Negotiates',
    507: 'Insufficient Storage (WebDAV)',
    508: 'Loop Detected (WebDAV)',
    510: 'Not Extended',
    511: 'Network Authentication Required',

}


class Color:
    def __init__(self):
        self.reset = "\u001b[0m"
        self.red = "\u001b[31m"
        self.green = "\u001b[32m"
        self.yellow = "\u001b[33m"
        self.blue = "\u001b[34m"
        self.magenta = "\u001b[35m"
        self.cyan = "\u001b[36m"
        self.white = "\u001b[37m"

class EndpointResult:
    content = None
    success = False
    response_content_type = "Unknown"
    response_size = 0
    status_code = 0
    error = None

class EndpointRecon:
    def __init__(self):
        self.use_headers = {}
        self.use_proxy = {}
        self.use_data = {}
        self.use_timeout = 10

    def try_get(self, url, headers={"Accept": "*"}, proxy={}, data={}, timeout=10,):
        result = EndpointResult()
        response = None
        try:
            response = requests.get(
                url,
                verify=False,
                data=data,
                headers=headers,
                proxies=proxy,
                timeout=timeout)
        except requests.exceptions.RequestException as re_err:
            result.error = re_err
            return result
        except Exception as py_err:
            result.error = py_err
            return result
        
        if response != None:
            # No errors, yey!
            result.success = True
            # Save Response Content
            result.content = response.content.decode('utf8','ignore')
            result.response_size = len(result.content)
            # Save Response Status
            result.status_code = int(response.status_code)
            # Save Response Content Type
            ct = response.headers.get('Content-Type') or ''
            result.response_content_type = ct
        else:
            result.error = "Unknown Error"
        
        return result
    
    def try_post(self, url, headers={"Accept": "*"}, proxy={}, data={}, timeout=10,):
        result = EndpointResult()
        response = None
        try:
            response = requests.post(
                url,
                verify=False,
                data=data,
                headers=headers,
                proxies=proxy,
                timeout=timeout)
        except requests.exceptions.RequestException as re_err:
            result.error = re_err
            return result
        except Exception as py_err:
            result.error = py_err
            return result
        
        if response != None:
            # No errors, yey!
            result.success = True
            # Save Response Content
            result.content = response.content.decode('utf8','ignore')
            result.response_size = len(result.content)
            # Save Response Status
            result.status_code = int(response.status_code)
            # Save Response Content Type
            ct = response.headers.get('Content-Type') or ''
            result.response_content_type = ct
        else:
            result.error = "Unknown Error"
        
        return result
    
    def try_put(self, url, headers={"Accept": "*"}, proxy={}, data={}, timeout=10,):
        result = EndpointResult()
        response = None
        try:
            response = requests.put(
                url,
                verify=False,
                data=data,
                headers=headers,
                proxies=proxy,
                timeout=timeout)
        except requests.exceptions.RequestException as re_err:
            result.error = re_err
            return result
        except Exception as py_err:
            result.error = py_err
            return result
        
        if response != None:
            # No errors, yey!
            result.success = True
            # Save Response Content
            result.content = response.content.decode('utf8','ignore')
            result.response_size = len(result.content)
            # Save Response Status
            result.status_code = int(response.status_code)
            # Save Response Content Type
            ct = response.headers.get('Content-Type') or ''
            result.response_content_type = ct
        else:
            result.error = "Unknown Error"
        
        return result
    
    def try_head(self, url, headers={"Accept": "*"}, proxy={}, data={}, timeout=10,):
        result = EndpointResult()
        response = None
        try:
            response = requests.head(
                url,
                verify=False,
                data=data,
                headers=headers,
                proxies=proxy,
                timeout=timeout)
        except requests.exceptions.RequestException as re_err:
            result.error = re_err
            return result
        except Exception as py_err:
            result.error = py_err
            return result
        
        if response != None:
            # No errors, yey!
            result.success = True
            # Save Response Content
            result.content = response.content.decode('utf8','ignore')
            result.response_size = len(result.content)
            # Save Response Status
            result.status_code = int(response.status_code)
            # Save Response Content Type
            ct = response.headers.get('Content-Type') or ''
            result.response_content_type = ct
        else:
            result.error = "Unknown Error"
        
        return result
    
    def try_delete(self, url, headers={"Accept": "*"}, proxy={}, data={}, timeout=10,):
        result = EndpointResult()
        response = None
        try:
            response = requests.delete(
                url,
                verify=False,
                data=data,
                headers=headers,
                proxies=proxy,
                timeout=timeout)
        except requests.exceptions.RequestException as re_err:
            result.error = re_err
            return result
        except Exception as py_err:
            result.error = py_err
            return result
        
        if response != None:
            # No errors, yey!
            result.success = True
            # Save Response Content
            result.content = response.content.decode('utf8','ignore')
            result.response_size = len(result.content)
            # Save Response Status
            result.status_code = int(response.status_code)
            # Save Response Content Type
            ct = response.headers.get('Content-Type') or ''
            result.response_content_type = ct
        else:
            result.error = "Unknown Error"
        
        return result
    
    def try_options(self, url, headers={"Accept": "*"}, proxy={}, data={}, timeout=10,):
        result = EndpointResult()
        response = None
        try:
            response = requests.options(
                url,
                verify=False,
                data=data,
                headers=headers,
                proxies=proxy,
                timeout=timeout)
        except requests.exceptions.RequestException as re_err:
            result.error = re_err
            return result
        except Exception as py_err:
            result.error = py_err
            return result
        
        if response != None:
            # No errors, yey!
            result.success = True
            # Save Response Content
            result.content = response.content.decode('utf8','ignore')
            result.response_size = len(result.content)
            # Save Response Status
            result.status_code = int(response.status_code)
            # Save Response Content Type
            ct = response.headers.get('Content-Type') or ''
            result.response_content_type = ct
        else:
            result.error = "Unknown Error"
        
        return result
    
    def try_patch(self, url, headers={"Accept": "*"}, proxy={}, data={}, timeout=10,):
        result = EndpointResult()
        response = None
        try:
            response = requests.patch(
                url,
                verify=False,
                data=data,
                headers=headers,
                proxies=proxy,
                timeout=timeout)
        except requests.exceptions.RequestException as re_err:
            result.error = re_err
            return result
        except Exception as py_err:
            result.error = py_err
            return result
        
        if response != None:
            # No errors, yey!
            result.success = True
            # Save Response Content
            result.content = response.content.decode('utf8','ignore')
            result.response_size = len(result.content)
            # Save Response Status
            result.status_code = int(response.status_code)
            # Save Response Content Type
            ct = response.headers.get('Content-Type') or ''
            result.response_content_type = ct
        else:
            result.error = "Unknown Error"
        
        return result

        
    def begin(self, url, except_: list=[ 'OPTIONS', 'PATCH', ]):
        scan_results = {}
        except_ = [e.upper() for e in except_]

        begin = time.time()

        # HTTP: GET
        if 'GET' not in except_:
            get_scan_result = self.try_get(
                url,
                headers = self.use_headers,
                proxy = self.use_proxy,
                data = self.use_data,
                timeout = self.use_timeout )
            
            scan_results['GET'] = get_scan_result

        # HTTP: POST
        if 'POST' not in except_:
            post_scan_result = self.try_post(
                url,
                headers = self.use_headers,
                proxy = self.use_proxy,
                data = self.use_data,
                timeout = self.use_timeout )
            scan_results['POST'] = post_scan_result

        # HTTP: PUT
        if 'PUT' not in except_:
            put_scan_result = self.try_put(
                url,
                headers = self.use_headers,
                proxy = self.use_proxy,
                data = self.use_data,
                timeout = self.use_timeout )
            scan_results['PUT'] = put_scan_result

        # HTTP: HEAD
        if 'HEAD' not in except_:
            head_scan_result = self.try_head(
                url,
                headers = self.use_headers,
                proxy = self.use_proxy,
                data = self.use_data,
                timeout = self.use_timeout )
            scan_results['HEAD'] = head_scan_result

        # HTTP: DELETE
        if 'DELETE' not in except_:
            delete_scan_result = self.try_delete(
                url,
                headers = self.use_headers,
                proxy = self.use_proxy,
                data = self.use_data,
                timeout = self.use_timeout )
            scan_results['DELETE'] = delete_scan_result


        # === [ Arbitrary ] ===

        # HTTP: OPTIONS
        if 'OPTIONS' not in except_:
            options_scan_result = self.try_options(
                url,
                headers = self.use_headers,
                proxy = self.use_proxy,
                data = self.use_data,
                timeout = self.use_timeout )
            scan_results['OPTIONS'] = options_scan_result

        # HTTP: PATCH
        if 'PATCH' not in except_:
            patch_scan_result = self.try_patch(
                url,
                headers = self.use_headers,
                proxy = self.use_proxy,
                data = self.use_data,
                timeout = self.use_timeout )
            scan_results['PATCH'] = patch_scan_result

        end = time.time()
        duration: float = round(end - begin, 3)
        
        return scan_results, duration


def main(args: list):
    recon = EndpointRecon()
    c = Color()
    url = ''
    except_=[]

    # Select URL from args
    if args.url != None:
        url = str(args.url)
    else:
        print('Error: URL is required.')
        return -1
    
    # Select Proxy from args
    if args.proxy != None:
        recon.use_proxy = {
            'http': str(args.proxy),
            'https': str(args.proxy)}
        
    # Select method exceptions
    if args.exclude != None:
        except_ = [e.strip().upper() for e in str(args.exclude).split(',')]
    
    if args.data != None:
        recon.use_data = args.data
    
    if args.headers != None:
        recon.use_headers = args.headers
    
    if args.timeout != None:
        recon.use_timeout = int(args.timeout)

    
    res, duration = recon.begin(
        url,
        except_=except_
    )
    print('{}URL:{} {}{}{}'.format(c.cyan,c.reset,c.yellow,url,c.reset))
    print('{}Duration:{} {}{}{} seconds'.format(c.cyan,c.reset,c.yellow,str(duration),c.reset))
    print(' \n')

    for k in list(res.keys()):
        print(' {}Request Method:{} {}{}{}'.format(c.cyan,c.reset,c.green,k,c.reset))
        print('  {}Request Completed:{} {}{}{}'.format(c.cyan,c.reset,c.yellow,res[k].success,c.reset))
        print('  {}Status:{} {}{}{} ({})'.format(c.cyan,c.reset,c.yellow,res[k].status_code,c.reset, STATUS_CODES[res[k].status_code] if res[k].status_code in list(STATUS_CODES.keys()) else 'Unknown'))
        print('  {}Response Content Type:{} {}{}{}'.format(c.cyan,c.reset,c.yellow,res[k].response_content_type,c.reset))
        print('  {}Response Size:{} {}Approx. {}{}{} Bytes{}'.format(c.cyan,c.reset,c.white,c.yellow,res[k].response_size,c.white,c.reset))
        print(' \n')

        if res[k].error != None:
            print('Error: {}{}{}'.format(c.red,res[k].error,c.reset))
        

if __name__ == "__main__":
    requests.packages.urllib3.disable_warnings()
    
    parser = argparse.ArgumentParser(
        prog='Endpoint Eye',
        description='Quickly get a glimpse of available HTTP request methods allowed (or not) at a specific endpoint to identify important information for further investigation.'
    )

    parser.add_argument('--url', '-u',
        action='store',
        type=str,
        help='URL (host + endpoint together) to investigate.'
    )

    parser.add_argument('--timeout', '-t',
        action='store',
        type=int,
        help='Max seconds to wait for each server response.'
    )

    parser.add_argument('--exclude', '-ex',
        action='store',
        type=str,
        help='Comma separated list of HTTP request methods to NOT CHECK. (Errors ignored)'
    )

    parser.add_argument('--proxy', '-rp',
        action='store',
        type=str,
        help='Proxy to send requests through.',
    )

    parser.add_argument('--headers', '-rh',
        action='store',
        type=str,
        help='JSON serializable string with custom headers (Optional)'
    )

    parser.add_argument('--data', '-rd',
        action='store',
        type=str,
        help='Custom JSON data (Optional)'
    )

    args = parser.parse_args()
    main(args)
