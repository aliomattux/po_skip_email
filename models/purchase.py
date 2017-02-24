from openerp.osv import osv, fields

class PurchaseOrder(osv.osv):
    _inherit = 'purchase.order'

    def skip_email(self, cr, uid, ids, context=None):
	return self.write(cr, uid, ids, {'state': 'sent'})
