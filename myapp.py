import logging


logger = logging.getLogger(__name__)


def app(environ, start_response):
    path = environ.get('PATH_INFO', '')
    if path == '/exception':
        raise Exception('My exception!')

    data_str = "Request on %s \n" % path
    data = data_str.encode('utf-8')
    logger.info(data, extra={'tags': ['role:web', 'env:prod']})
    start_response("200 OK", [
          ("Content-Type", "text/plain"),
          ("Content-Length", str(len(data)))
      ])
    return iter([data])
