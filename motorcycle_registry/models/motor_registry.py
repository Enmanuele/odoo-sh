# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import re
from odoo.exceptions import ValidationError

import logging
_logger = logging.getLogger(__name__)


class MotorcycleRegistry(models.Model):
	_name = 'motorcycle.registry'
	_description = 'Motorcycle Registry'
	_rec_name = 'registry_number'
	
	certificate_title = fields.Binary('Título de la propiedad')
	current_mileage = fields.Float('Millaje Actual')
	first_name = fields.Char('Nombre')
	last_name = fields.Char('Apellido')
	license_plate = fields.Char('Matricula')
	registry_date = fields.Date('Fecha de Registro')
	registry_number = fields.Char('Número de registro', readonly=True)
	vehicle_image = fields.Binary('Foto del Vehiculo')
	vin = fields.Char('Número de VIN', required=True)
	
	## Adicionales
	owner_id = fields.Many2one('res.partner', 'Cliente')
	email = fields.Char(related='owner_id.email', string='Correo')
	phone = fields.Char(related='owner_id.phone', string='Teléfono')
	cell_phone = fields.Char(related='owner_id.mobile', string='Móvil')
	
	## Campos calculados
	make = fields.Char('Origen', compute="_compute_make")
	model = fields.Char('Modelo', compute="_compute_make")
	year = fields.Integer('Año', compute="_compute_make")
	
	_sql_constraints = [
		('vin_unique', 'UNIQUE(vin)', 'VIN debe ser único')
	]
	
	def _compute_make(self):
		data = []
		for record in self.filtered(lambda r: r.vin):
			if record.vin:
				for i in range(0,len(record.vin), 2):
					data.append(record.vin[i:i+2])
			
			record.make = data[0]
			record.model = data[1]
			record.year = data[2]
				
	
	@api.model
	def create(self, vals):
		vals["registry_number"] = (
			self.env["ir.sequence"].next_by_code("moto-cod") or "Nuevo Reg."
		)
		return super(MotorcycleRegistry, self).create(vals)
	
	def testboton(self):
		_logger.warning('VAMOS')
	
	@api.constrains('license_plate')
	def _restriccion_licence(self):
		pattern_license = '^[A-Z]{1,3}\d{1,4}[A-Z]{0,2}$'
		
		for record in self.filtered(lambda r: r.license_plate):
			if record.license_plate:
				match_licence = re.match(pattern_license, record.license_plate)
				if not match_licence:
					raise ValidationError(_('MATRICULA no coincide con el FORMATO requerido'))
				
			
	@api.constrains('vin')
	def _restriccion_vin(self):
		pattern_vin = '^[A-Z]{4}\d{2}[A-Z0-9]{2}\d{5}$'
		
		for record in self.filtered(lambda r: r.vin):
			if record.vin:
				match_vin = re.match(pattern_vin, record.vin)
				if not match_vin:
					raise ValidationError(_('VIN no coincide con el FORMATO requerido'))
					