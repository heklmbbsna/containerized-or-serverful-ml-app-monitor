curl 'http://35.247.19.1:8080/' \
  -H 'Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryOazCL6O13gIo9X7Z' \
  -H 'Cookie: csrftoken=ST4xLvnExntnw0TCKKYd1g6UCkaf5Azr' \
  --data-raw $'------WebKitFormBoundaryOazCL6O13gIo9X7Z\r\nContent-Disposition: form-data; name="input_data"\r\n\r\n{ "male":0, "age":49, "salary":61000, "price":2000 }\r\n------WebKitFormBoundaryOazCL6O13gIo9X7Z--\r\n'
