import requests

def decode(http_request):
    rows = http_request.split("\n")
    method,raw_path,req_params= rows[0].split()
    type,http_version = req_params.split("/")

    headers = {}
    for header in rows[1:]:
        k,v = header.split(":")
        headers[k] = v

    request = {
        "type": type,
        "http_version": http_version,
        "method": method,
        "raw_path": raw_path,
        "headers": [headers],
    }
    return request

http_request = "GET /hello.htm HTTP/1.1 \n" \
               "User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT) \n" \
               "Host: www.tutorialspoint.com \n" \
               "Accept-Language: en-us \n" \
               "Accept-Encoding: gzip, deflate \n" \
               "Connection: Keep-Alive"


print(decode(http_request))
