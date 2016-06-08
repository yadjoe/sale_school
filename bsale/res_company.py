# -*- coding: utf-8 -*-
from openerp import models, fields, api

class res_company(models.Model):
    _name = 'res.company'
    _inherit = 'res.company'
    
    @api.model
    def _get_default_sequence(self):
        sequence_ids = self.env['ir.sequence'].search([('code', '=', 'res.partner')])
        if sequence_ids:
            return sequence_ids[0]
    
    #TODO: set default value    
    partner_number_sequence = fields.Many2one('ir.sequence', string=u"Séquence des numéros de clients")
    highlight_color = fields.Char(string="Couleur des rapports", size = 128, default="#990066")