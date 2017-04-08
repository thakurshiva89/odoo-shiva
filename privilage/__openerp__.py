# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Privilage',
    'version': '1.1',
    'category': 'Privilage',
    'description': """
Privilage.
    """,
    'website': 'https://www.odoo.com/page/accounting',
    'depends' : ['account'],
    'data': ['security/security.xml' ,
		    'security/ir.model.access.csv',],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
