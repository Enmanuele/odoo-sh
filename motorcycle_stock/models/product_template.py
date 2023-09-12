# -*- coding: utf-8 -*-

from odoo import models, fields

class ProductTemplateInherit(models.Model):
	_inherit = 'product.template'
	
	detailed_type = fields.Selection(selection_add=[('motorcycle', 'Motocicleta')], ondelete={'motorcycle': 'set product'})
	
	horsepower = fields.Float('Caballos de Fuerza')
	top_speed  = fields.Float('Velocidad Maxima')
	torque  = fields.Float('Torque')
	battery_capacity = fields.Selection([('xs', 'Pequeño'), ('0m', 'Mediano'), ('0l','Largo'), ('xl', 'Extra Grande')], string='Capacidad Bateria')
	charge_time = fields.Float('Tiempo de Carga')
	range = fields.Float('Rango')
	curb_weight = fields.Float('Peso')
	make = fields.Char('Marca')
	model = fields.Char('Modelo')
	year = fields.Char('Año')
	
	
	def _detailed_type_mapping(self):
		type_mapping = super()._detailed_type_mapping()
		type_mapping['motorcycle'] = 'product'
		return type_mapping