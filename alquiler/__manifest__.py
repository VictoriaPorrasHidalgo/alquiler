# -*- coding: utf-8 -*-
{
    'name': "alquiler",

    'summary': """
        Gestión de películas.
        Educación""",

    'description': """
        Permite gestionar una colección de películas
    """,

    'author': "Victoria3758890",
    'website': "http://ead.murciaeduca.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
