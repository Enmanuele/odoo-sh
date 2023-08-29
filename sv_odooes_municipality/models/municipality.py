# -*- coding: utf-8 -*-

from odoo import models, fields

class municipalitySV(models.Model):
	_name = 'res.municipality'
	_description = 'Municipios'

	active = fields.Boolean(string='Activo', default=True)
	code = fields.Char(string='Código', required=True)
	name = fields.Char(string='Valores', required=True)
	
	res_country_state_id = fields.Many2one('res.country.state', 'Provincias', required=True)
	
	_sql_constraints = [
        ('code_id_municipality_unique', 'unique(res_country_state_id, code)', 'Código debe ser único por departamento')
    ]
	