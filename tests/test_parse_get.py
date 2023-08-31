from parse_get import decode


def test1_good_get():
    http_request = open("../http_requests/test1_good_get.txt", "r").read()
    assert decode(http_request) == {
        "type": "HTTP",
        "http_version": "1.1",
        "method": "GET",
        "raw_path": "/hello.htm",
        "headers": [
            {
                "User-Agent": "Mozilla/4.0 (compatible; MSIE5.01; Windows NT)",
                "Host": "www.tutorialspoint.com",
                "Accept-Language": "en-us",
                "Accept-Encoding": "gzip, deflate",
                "Connection": "Keep-Alive",
            }
        ],
    }


def test2_good_post():
    http_request = open("../http_requests/test2_good_post.txt", "r").read()
    assert decode(http_request) == {
        "type": "HTTP",
        "http_version": "1.1",
        "method": "POST",
        "raw_path": "/cgi-bin/process.cgi",
        "headers": [
            {
                "User-Agent": "Mozilla/4.0 (compatible; MSIE5.01; Windows NT)",
                "Host": "www.tutorialspoint.com",
                "Content-Type": "application/x-www-form-urlencoded",
                "Content-Length": "length",
                "Accept-Language": "en-us",
                "Accept-Encoding": "gzip, deflate",
                "Connection": "Keep-Alive",
            }
        ],
        "body": "licenseID=string&content=string&/paramsXML=string",
    }


def test3_good_post_longbody():
    http_request = open("../http_requests/test3_good_post_longbody.txt", "r").read()
    assert decode(http_request) == {
        "type": "HTTP",
        "http_version": "1.1",
        "method": "POST",
        "raw_path": "/cgi-bin/process.cgi",
        "headers": [
            {
                "User-Agent": "Mozilla/4.0 (compatible; MSIE5.01; Windows NT)",
                "Host": "www.tutorialspoint.com",
                "Content-Type": "application/x-www-form-urlencoded",
                "Content-Length": "length",
                "Accept-Language": "en-us",
                "Accept-Encoding": "gzip, deflate",
                "Connection": "Keep-Alive",
            }
        ],
        "body": "licenseID=string&content=string&/paramsXML=string\nlicenseID=string&content=string&/paramsXML=string",
    }
