def decode(http_request):
    http_request = http_request.decode()
    rows = http_request.split("\n")
    method, raw_path, req_params = rows[0].strip().split()
    type, http_version = req_params.split("/")

    headers = []
    last_indx = 0
    for indx, header in enumerate(rows[1:]):
        if not header.strip():
            last_indx = indx
            break
        k, v = header.split(":",1)
        headers.append([k, v.strip()])

    request = {
        "type": type,
        "http_version": http_version,
        "method": method,
        "path": raw_path.split("?")[0],
        "raw_path": raw_path,
        "headers": headers,
    }
    if len(rows) > last_indx + 2 and last_indx != 0:
        body = []
        for body_str in rows[last_indx + 2 :]:
            if body_str.strip():
                body.append(body_str)

        body = "\n".join(body)
        request["body"] = body

    return request

