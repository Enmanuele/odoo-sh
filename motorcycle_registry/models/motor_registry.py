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
	
	certificate_title = fields.Binary('Titulo de la propiedad')
	current_mileage = fields.Float('Millaje Actual')
	first_name = fields.Char('Nombre', required=True)
	last_name = fields.Char('Apellido', required=True)
	license_plate = fields.Char('Matricula')
	registry_date = fields.Date('Fecha de Registro')
	registry_number = fields.Char('Numero de registro', readonly=True)
	vehicle_image = fields.Binary('Foto del Vehiculo')
	vin = fields.Char('Numero de VIN', required=True)
	
	_sql_constraints = [
		('vin_unique', 'UNIQUE(vin)', 'VIN debe ser único')
	]
	
	@api.model
	def create(self, vals):
		vals["registry_number"] = (
			self.env["ir.sequence"].next_by_code("moto-cod") or "Nuevo Reg."
		)
		return super(MotorcycleRegistry, self).create(vals)
	
	@api.constrains('license_plate', 'vin')
	def _restricciones_campos(self):
		pattern_license = "^[A-Z]{1,3}\d{1,4}[A-Z]{0,2}$"
		pattern_vin = "^[A-Z]{4}\d{2}[A-Z0-9]{2}\d{5}$"
		
		for record in self:
			match_licence = re.match(pattern_license, record.license_plate)
			match_vin = re.match(pattern_vin, record.vin)
			
			_logger.warning('/////////////////////')
			_logger.warning(match_licence)
			_logger.warning(match_vin)
			
			if record.license_plate != match_licence:
				pass
				#raise ValidationError(_('MATRICULA no coincide con el FORMATO requerido'))
				
			if record.vin != match_vin:
				pass
				#raise ValidationError(_('VIN no coincide con el FORMATO requerido'))
		
		

