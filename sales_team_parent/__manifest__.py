# -*- coding: utf-8 -*-
{
    'name': 'Parent Team & Targets',
    'version': '0.1',
    'category': 'Sales',
    'summary': 'Sales Team Targets and Parent Teams',
    'sequence': 150,
    'author': 'Odoolibre',
    'company': 'Odoolibre',
    'website': '',
    'depends': ['crm', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/parent_team.xml',
        'views/sales_man_target.xml',
        'views/sales_team_target.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,

}
