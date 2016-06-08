# -*- coding: utf-8 -*-

import time

from openerp.report import report_sxw
from openerp.osv import osv


class AccountInvoice(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(AccountInvoice, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'group_taxes': self._group_taxes
        })
    
    def _group_taxes(self, invoice):
        taxes = {}
        for tax in invoice.tax_line:
            if tax.amount > 0:
                if tax.name in taxes:
                    taxes[tax.name] += tax.amount
                else:
                    taxes[tax.name] = tax.amount
        result = []
        for tax in taxes:
            result.append({'name': tax, 'amount': taxes[tax], 'currency':invoice.currency_id})
        return result
    
    
        


class report_account_invoice(osv.AbstractModel):
    _name = 'report.account.report_invoice'
    _inherit = 'report.abstract_report'
    _template = 'account.report_invoice'
    _wrapped_report_class = AccountInvoice

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: