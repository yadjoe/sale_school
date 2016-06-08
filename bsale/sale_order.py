# -*- coding: utf-8 -*-
from openerp import models, fields, api

class sale_order(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'
    
    date_limit_validity = fields.Date(string=u"Date limite de validité",  copy=False)
    
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: