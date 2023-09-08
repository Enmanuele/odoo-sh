# -*- coding: utf-8 -*-

{
	"name": "Motorcycle Registry",
	"version": "0.0.1",
	"author": "OdooES El Salvador",
	"category": "Kawiil",
	"summary": "Manage Registration of Motorcycle",
	"license": "OPL-1",
	"support": "enmanuele777@gmail.com",
	"maintainer": "Enmanuel Ortiz",
	"website": "https://odooes.com",
	"description": """Motorcycle Registry
====================
This Module is used to keep track of the Motorcycle Registration and Ownership of each motorcycled of the brand.
""",
	
	"depends": [
		"base",
	],
	"data": [
		"data/category_groups.xml",
		"security/motor_groups.xml",
		"security/ir.model.access.csv",
		"data/demo.xml",
		"data/sequence_data.xml",
		"views/motorcycle_view.xml",
	],
	"demo": [
		"data/demo.xml",
	],
	"images": [
	],
	"installable": True,
	"application": True,
	"auto_install": False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
