# -*- coding: utf-8 -*-

from odoo import models, fields

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
	registry_number = fields.Char('Numero de registro')
	vehicle_image = fields.Binary('Foto del Vehiculo')
	vin = fields.Char('Numero de VIN', required=True)
	
	_sql_constraints = [
		('vin_unique', 'UNIQUE(vin)', 'VIN debe ser único')
	]
	
	