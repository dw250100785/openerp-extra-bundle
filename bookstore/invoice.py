# -*- encoding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################

from osv import fields,osv

class account_invoice(osv.osv):

    _inherit = "account.invoice"
    _columns = {
        'export_date': fields.datetime("Export time"),
        }

    _defaults = {
        #'price_type': lambda *a: 'tax_included',
    }


    def _refund_cleanup_lines(self, cr, uid, lines):
        for line in lines:
            if 'account_analytic_id' in line:
                line['account_analytic_id'] = line.get('account_analytic_id', False) and line['account_analytic_id'][0]
            if 'production_lot_id' in line:
                line['production_lot_id'] = line.get('production_lot_id', False) and line['production_lot_id'][0]
        res = super(account_invoice,self)._refund_cleanup_lines(cr, uid, lines)
        return res
    


account_invoice()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

