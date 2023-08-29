# -*- coding: utf-8 -*-

from odoo import fields, models

class ResPartner(models.Model):
	_inherit = 'res.partner'
	_description = 'Contacto'
	
	municipality_id = fields.Many2one('res.municipality', 'Municipio', required=True)