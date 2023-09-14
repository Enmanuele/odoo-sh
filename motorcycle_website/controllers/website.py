#from odoo import models, fields

from odoo import http, _

class MotorcycleController(http.Controller):
	@http.route('/compare', auth='public', website=True)
	def comparedatas(self, **kw):
		motores = http.request.env['product.template'].search([('detailed_type', '=', 'motorcycle')])
		
		return http.request.render('motorcycle_website.report_compare_motorcicle_product', {
			'motors': motores
		})
		