#from odoo import models, fields

from odoo import http
class MotorcycleController(http.Controller):
	@http.route('/compare', auth='public', website=True)
	def comparedatas(self, **kw):
		motores = http.request.env['product.template'].search([('detailed_type', '=', 'motorcycle')])
		
		return http.request.render('motorcycle_website.report_compare_motorcycle_product', {
			'motors': motores
		})
