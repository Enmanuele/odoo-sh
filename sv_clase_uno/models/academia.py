# -*- coding: utf-8 -*-

from odoo import models, fields

class Academia(models.Model):
	_name = 'mia.academia'
	
	name = fields.Char()
	
	