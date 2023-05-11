# -*- coding: utf-8 -*-
{
    'name': "GEI_dashboard",

    'summary': "A dashboard for the server´s resources"
        """Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': "This module shows a dashboard with a server's resources, such as used RAM and total RAM, how
                    "many users are connected, how many users are in total, etc. It also shows alerts."
        """Long description of module's purpose
    """,

    'author': "GEI Project",
    'website': "https://gei-project.odoo.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
