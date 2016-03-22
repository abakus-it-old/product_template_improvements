from openerp import models, fields, api

class product_template_improvements(models.Model):
    _inherit = ['product.template']
    
    @api.onchange('default_code')
    def check_default_code(self):
        if self.default_code and len(self.default_code)>0:
            cr = self.env.cr
            uid = self.env.user.id
            product_template_obj = self.pool.get('product.template')
            product_templates = product_template_obj.search(cr, uid, [('default_code', '=', self.default_code)])
            if product_templates:
                return {'warning': {'title': 'Internal Reference Failure', 'message': 'The internal reference already exists'},}
    
    @api.onchange('ean13')
    def check_ean13(self):
        if self.ean13 and len(self.ean13)>0:
            cr = self.env.cr
            uid = self.env.user.id
            product_template_obj = self.pool.get('product.template')
            product_templates = product_template_obj.search(cr, uid, [('ean13', '=', self.ean13)])
            if product_templates:
                return {'warning': {'title': 'EAN13 Barcode Failure', 'message': 'The EAN13 barcode already exists'},}