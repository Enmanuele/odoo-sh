# -*- coding: utf-8 -*-

from odoo import fields, models, api

class ResCompany(models.Model):
	_inherit = 'res.company'
	_description = 'Empresa'

	municipality_id = fields.Many2one('res.municipality', 'Municipio', required=True)
	
	@api.onchange('municipality_id', 'state_id', 'country_id')
	def _change_address_info(self):
		self.partner_id.write({
			'municipality_id': self.municipality_id.id,
			'state_id': self.state_id.id,
			'country_id': self.country_id.id
			})