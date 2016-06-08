# -*- coding: utf-8 -*-
from openerp import models, fields, api

class res_partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    
    identifier = fields.Char(string=u"Numéro du client", readonly=True, size = 128)
    
    @api.model
    def create(self, vals):
        if not (vals.has_key('identifier') and vals['identifier']) and (vals.has_key('customer') and vals['customer']):
            company = self.env.user.company_id
            if vals.has_key('company_id') and vals['company_id']:
                company = self.env['res.company'].browse(vals['company_id'])
            if company.partner_number_sequence:
                vals['identifier'] = self.env['ir.sequence'].get(company.partner_number_sequence.code)
            else:
                vals['identifier'] = self.env['ir.sequence'].get('res.partner')
        return super(res_partner, self).create(vals)
    
    @api.model
    def default_get(self, fields):
        res = super(res_partner, self).default_get(fields)
        is_company = self.env.context and not (self.env.context.get('is_contact', False) or self.env.context.get('default_parent_id', False) != False or self.env.context.get('default_customer', False) != False)
        res.update({'is_company': is_company})
        return res
    
    @api.model
    def fields_view_get(self, view_id=None, view_type=False, toolbar=False, submenu=False):
        if (not view_id) and (view_type=='form') and self.env.context and self.env.context.get('is_contact', False):
            view_id = self.env['ir.ui.view'].search([('name', '=', 'res.partner.contact.form')]).id
        return super(res_partner,self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: