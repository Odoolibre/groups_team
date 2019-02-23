# -*- coding: utf-8 -*-
{
    'name': 'Parent Team & Targets',
    'version': '0.1',
    'category': 'Sales',
    'summary': 'Sales Team Targets and Parent Teams',
    'author': 'Odoolibre',
    'company': 'Odoolibre',
    'website': '',
    'depends': ['crm', 'sale'],
    'images': [],
    'data': [
        'security/ir.model.access.csv',
        'views/parent_team.xml',
        'views/sales_man_target.xml',
        'views/sales_team_target.xml',
    ],
    'installable': True,
    'auto_install': False,
}
