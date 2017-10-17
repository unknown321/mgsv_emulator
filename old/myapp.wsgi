#!/usr/bin/python3
import sys
import os
sys.path.append(os.path.dirname(__file__))
from mgsv_emulator.emulator.server import Server
import urllib.parse
from datetime import datetime


def log_event(text, event_type=0):
        logfile = open('/var/www/mgsv_server/logs/app.log','a')
        logfile.write('[{}] {}: {}\n'.format(datetime.now(), event_type, text))
        logfile.close()

def application(environ, start_response):
        #log_event('--------------------------')
        status = '200 OK'
        output = b""
        if environ['REQUEST_METHOD'] == 'POST':
                server = Server()

                # the environment variable CONTENT_LENGTH may be empty or missing
                try:
                        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
                except (ValueError):
                        request_body_size = 0

                client_ip = environ['REMOTE_ADDR']
                k = environ['wsgi.input'].read(request_body_size)
                d = urllib.parse.parse_qs(k.decode(),True)
                client_request = d.get('httpMsg',[''])[0]

                # log_event(httpMsg)


                output = server.process_request(client_request, client_ip)
                # command = copy.deepcopy(s.__command_get__(str(client_request['data']['msgid'])))
                # append_date(command)
                # log_event(command)
                output = output.encode()
        else:
                # a GET request for eula
                #log_event(environ)
                pass

        response_headers = [('Content-type', 'text/plain'),
                                                ('Content-Length', str(len(output)))]
        start_response(status, response_headers)
        output = [output]
        #log_event(output)
        return output