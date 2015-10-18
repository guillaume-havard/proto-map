import os, os.path
import string

import cherrypy

class StringGenerator(object):

    @cherrypy.expose
    def index(self):
        return open('test-carte.html')

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    webapp = StringGenerator()
    cherrypy.quickstart(webapp, '/', conf)
