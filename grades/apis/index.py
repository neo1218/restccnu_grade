# coding: utf-8

from coroutx import route
from .. import app


headers = {'Content-Type': 'application/json'}


@route(app, '/api/')
@app.tojson
def api_index():
    return {
        'meta': {
            'project': 'restccnu',
            'version': 'v1',
            'source code': 'https://github.com/Muxi-Studio/restccnu',
            'author': ['@neo1218', '@kasheemlew'],
        },
        'apis': {
            'Information Portal Login': '/api/info/login/',
            'Library': [
                {'library login': '/api/lib/login/'},
                {'book search': '/api/lib/search/?keyword=xxx&page=n'},
                {'book detail': '/api/lib/?id=xxxxxx&book=xxxx&author=xxxxx'},
                {'my library': '/api/lib/me/'},
            ],
            'Class Schedule': [
                {'class schedule query': '/api/table/?xnm=n&xqm=n'},
                {'add personal class': '/api/table/'},
                {'delete personal class': '/api/table/id/'}
            ],
            'Grade Query': {
                'query': '/api/grade/search/?xnm=n&xqm=n',
                'detail query': '/api/grade/detail/search/?xnm=x&xqm=x&course=x&jxb_id=x'
            },
            'Info API': '/api/info/',
            'Electric bill API': '/api/ele/',
            'Apartment info API': '/api/apartment/',
            'Static Management': [
                {'banner api': '/api/banner/'},
                {'calendar api': '/api/calendar'}
            ],
            'Version Management': {
                'app version management': [
                    {'all ccnubox version': '/api/app/'},
                    {'add a new version': '/api/app/'},
                    {'delete a specific version': '/api/app/'},
                    {'ccnubox latest version': '/api/app/latest/'}
                ],
                'patch version management': [
                    {'all ccnubox patches version': '/api/patch/'},
                    {'add a new patch version': '/api/patch/'},
                    {'delete a specific patch version': '/api/patch/'},
                    {'latest ccnubox patch version': '/api/patch/latest/'}
                ],
            },
        },
    }, headers
