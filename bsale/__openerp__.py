# -*- encoding: utf-8 -*-
##############################################################################
#
#   Copyright (C) 2010-2011 BAAMTU SARL (<http://baamtu.sn>). All Rights Reserved
#    $Id$
#   contact: leadsn@baamtu.com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name" : "Gestion Commerciale",
    "version" : "1.1",
    "author" : "Baamtu",
    "category": 'Sales Management',
    "description": """Gestion Commerciale""",
    'website': 'http://www.baamtu.com',
    'init_xml': [],
    "depends" : ['base','sale','account'],
    'data': [
             'data/sequence.xml',
             'res_partner_view.xml',
             'res_company_view.xml',
             'sale_order_view.xml',
             'report/paper_format.xml',
             'report/menu_account_invoice.xml',
             'views/report_invoice.xml',
             'views/report_saleorder.xml',
             'report/menu_sale_order.xml',
             'views/template.xml'
             ],
    'demo_xml': [],
    'installable': True,
    'active': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
