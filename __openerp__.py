{
    'name': 'Customize login page',
    'version': '1.0',
	'description': "This module will change the display of login page",
    'category': 'web',
    'complexity': "easy",
    'description': """
This module will change this login page.
=================
Change login homepage, logo and some CSS properties.

    """,
    'author': 'ERPTalk.net',
    'website': 'http://erptalk.net',
    'installable': True,
    'active': False,
	'depends': ['web'],
    'qweb' : [
        "static/src/base.xml",
    ],
	'css': [
		"static/src/css/login.css",
	],
}