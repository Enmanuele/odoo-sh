# -*- coding: utf-8 -*-

{
	"name": "SV Municipality",
	"version": "1.0.0",
	"author": "OdooES El Salvador",
	"category": "Others",
	"summary": "Municipios",
	"license": "LGPL-3",
	"support": "enmanuele777@gmail.com",
	"contributors": [
		'Enmanuel Ortiz <enmanuele777@gmail.com>',
	],
	"maintainer": "Enmanuel Ortiz",
	"website": "https://odooes.com",
	"description": """
Municipios
====================================
Tablas:
--------------------------------------------
	* Municipios res.municipality
	
Relaciones:
--------------------------------------------
	* Provincias res.country.state

	""",
	
	"depends": [
		"contacts",
	],
	"data": [
		"views/municipality_view.xml",
		"views/res_company_view.xml",
		"views/res_partner_view.xml",
		"views/main_view.xml",
		"security/ir.model.access.csv"
	],
	"images": [
	],
	"installable": True,
	"application": False,
	"auto_install": False,
	"sequence": 1,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
