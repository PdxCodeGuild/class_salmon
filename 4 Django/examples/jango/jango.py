import json
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
# 
# Abstraction
#

class NotFoundError(BaseException):
    pass

# Very crude url dispatching
def dispatch(request, urlpatterns):
    for url in urlpatterns:
        if request.path == url['path']:
            return url['view'](request)

    raise NotFoundError(f'404: "{request.path}" Not Found')

# Very crude template rendering
def render(request, template_path, context):
    with open(template_path) as template:
        return template.read().format(**context)

# Very crude reverse
def reverse(name, urlpatterns):
    for url in urlpatterns:
        if url['name'] == name:
            return url['path']


def home(request):
    context =  {
        'title': 'Hello Jango!',
        'body': 'Tiny gimped version of Django',
        'date': datetime.now()
    }

    return render(request, './home.html', context)

def about(request):
    return json.dumps({
        'message': 'Jango Works!~'
    })

urlpatterns = [
    {'path': '/', 'view': home, 'name': 'home'},
    {'path': '/about', 'view': about, 'name': 'about'}
]

class JangoRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            response = dispatch(self, urlpatterns)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes(response, 'utf8'))

        except NotFoundError:
            self.send_response_only(404)


def run(server_class=HTTPServer, handler_class=JangoRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == '__main__':
    run()
