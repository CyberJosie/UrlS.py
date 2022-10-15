import textwrap
import time
import json
import csv
import requests
import argparse

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



class EndpointResult:
    response_content = None
    request_success = False
    response_content_type = "Not Specificed"
    response_size = 0
    status_code = 0
    error = None

    # def empty(self):
    #     empty = False
    #     if self.response_content == None and self.request_success == False and self.response_content_type == "Not Specificed" and self.response_size == 0 and self.status_code == 0 and self.error == None:
    #         empty = True
    #     return empty
    
              
def export_output(results:list, path:str, format='json', **options):
        
    if format == 'greppable':
        pass

    elif format.lower() == 'json':
        json_objects = []

        for result in results:
            for method in list(result.keys()):

                data = {
                    'Request-Success': result[method].request_success,
                    'Status-Code': result[method].status_code,
                    'Response-Content': result[method].response_content,
                    'Response-Content-Type': result[method].response_content_type,
                    'Response-Size-Bytes': result[method].response_size,
                    'Request-Error': result[method].error,
                }

                json_objects.append(data)

        indent = 2
        if 'indent' in list(options.keys()):
            if type(options['indent']) == int:
                indent = options['indent']
        
        with open(path, 'w') as f:
                f.write(json.dumps(json_objects, indent=indent))
            

    elif format.lower() == 'csv':
        header = [
            'Request-Success',
            'Status-Code',
            'Response-Content',
            'Response-Content-Type',
            'Response-Size-Bytes',
            'Request-Error',
        ]

        
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)

            for result in results:
                for method in list(result.keys()):
                
                    data = [
                        result[method].request_success,
                        result[method].status_code,
                        result[method].response_content or 'No Content',
                        str(result[method].response_content_type).replace(';','&'),
                        result[method].response_size or 0,
                        result[method].error or 'None'
                    ]
                    writer.writerow(data)
                

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

        
    def begin(self, url, except_: list=[]):
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

# MAIN
def main(args: list):
    urls = []
    except_=[]
    output = None
    output_format = None
    c = Color()
    recon = EndpointRecon()

    # Select URL from args
    if args.url != None:
        urls.append(args.url)
    
    elif args.url_file != None:
        lines = []
        try:
            with open(str(args.url_file), 'r', encoding='utf8', errors='ignore') as f:
                lines = f.readlines()
        except Exception as err:
            print("{}Error while reading from URL file: \'{}\'{}".format(c.red,args.url_file,c.reset))
            print(err)
            return -1
        
        [urls.append(url.strip()) for url in lines if url not in ['', ' ', '\n'] and url.startswith('http')]
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
    

    
    if args.timeout != None:
        recon.use_timeout = int(args.timeout)
    
    if args.output != None:
        output = args.output

        if args.output_format != None:
            output_format = args.output_format
        else:
            output_format = 'json'
    
    

    # Run analysis
    results = []
    for url in urls:
        
        res, duration = recon.begin(
            url,
            except_=except_ )
        results.append(res)

        if output == None and output_format == None:
    
            # Print result
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
    
    if output != None and output_format != None:
        export_output(results,output,output_format)

    
        

if __name__ == "__main__":
    c = Color()
    requests.packages.urllib3.disable_warnings()
    
    parser = argparse.ArgumentParser(
        prog='URL Spy',
        formatter_class=argparse.RawTextHelpFormatter,
        # description='Quickly get a glimpse of available HTTP request methods allowed (or not) at a specific endpoint to identify important information for further investigation.',
        description=textwrap.dedent('''
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
            
        '''),
        epilog=textwrap.dedent('''\
            Find on GitHub: https://github.com/CyberJosie/URLs.py
        ''')
    )

    parser.add_argument('--url', '-u',
        action='store',
        type=str,
        help=textwrap.dedent('''
        URL (host and endpoint together) to investigate.
        Default: None
        Required: True\n
        ''')
    )

    parser.add_argument('--url-file', '-uf',
        action='store',
        type=str,
        help=textwrap.dedent('''
        Path to file of URLs to analyze. (URLs are newline separated).
        Default: None
        Required: True (If a single URL is not given)\n
        ''')
    )

    parser.add_argument('--timeout', '-t',
        action='store',
        type=int,
        help=textwrap.dedent('''
        Max seconds to wait for each server response
        Default: 10
        Required: False\n
        ''')        
    )

    parser.add_argument('--exclude', '-ex',
        action='store',
        type=str,
        # help=''
        help=textwrap.dedent('''
        Comma separated list of HTTP request methods to NOT CHECK. Errors ignored.
        Default: GET,POST,PUT,HEAD,DELETE,OPTIONS,PATCH
        Required: False\n
        ''')
    )

    parser.add_argument('--proxy', '-rp',
        action='store',
        type=str,
        help=textwrap.dedent('''
        Proxy to send requests through
        Default: None
        Required: False\n
        ''')
    )

    parser.add_argument('--output', '-o',
        action='store',
        type=str,
        help=textwrap.dedent('''
        Path to redirect output to.
        Default: Print to STDOUT
        Required: False\n
        ''')
    )

    parser.add_argument('--output-format', '-fmt',
        action='store',
        type=str,
        help=textwrap.dedent('''
        Formatting to export output as. Options: JSON, CSV, greppable
        Default: JSON (If only output flag is given, else there is no default)
        Required: False\n
        ''')
    )
    

    args = parser.parse_args()
    main(args)
