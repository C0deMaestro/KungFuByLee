def decode(http_request):
    rows = http_request.split("\n")
    method,raw_path,req_params= rows[0].split()
    type,http_version = req_params.split("/")

    headers = {}

    for indx,header in enumerate(rows[1:]):
        if header.strip():
            k,v = header.split(":")
            headers[k] = v.strip()
        else:
            break
    request = {
        "type": type,
        "http_version": http_version,
        "method": method,
        "raw_path": raw_path,
        "headers": [headers],}
    if len(rows)>indx+2:
        body = []
        for body_str in rows[indx+2:]:
            if body_str.strip():
                body.append(body_str)

        body = "\n".join(body)
        request["body"] = body

    return request




