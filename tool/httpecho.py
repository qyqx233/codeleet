import logging
logging.basicConfig(level=logging.DEBUG)
from apistar import http, Route, App


def echo_request_info(request: http.Request) -> dict:
    logging.debug(request.headers)
    logging.debug(request.body)
    logging.debug(request.url)
    return {
        'method': request.method,
        'url': request.url,
        'headers': dict(request.headers),
        'body': request.body.decode('utf-8')
    }

routes = [
    Route('/', method='POST', handler=echo_request_info),
]

app = App(routes=routes)


if __name__ == '__main__':
    app.serve('127.0.0.1', 5000, debug=True)    