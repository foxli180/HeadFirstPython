from http.server import HTTPServer,CGIHTTPRequestHandler
#配置一个简单的httpserver
port = 8082
httpd = HTTPServer(('',port),CGIHTTPRequestHandler)
print('Starting simple_httpd on port:' +str(httpd.server_port))
httpd.serve_forever()
