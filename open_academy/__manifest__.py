# -*- coding: utf-8 -*-
# noinspection PyStatementEffect






{
    'name': "open_academy",

    'author': "My Company",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/course_view.xml',
        'views/student_view.xml',
        'views/instructor_view.xml',
        'views/open_academy_main_menu.xml',

    ],
    # # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    "application":True
}
