# -*- coding: utf-8 -*-
# Copyright 2017 Gabriel Lopez Alarcon https://www.facebook.com/gabo.Lop.A
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    "name" : "Paquete",
    "summary": "Product Combo Bundle Pack",
    "version" : "10.0.1.1.0",
    "description": """
		This module allows you to combine individual products into another 
		new one. That is, saling a combo/bundle of different (or same) 
		products. Various quantity can be sets.
    """,
    "category": "Sales",
    "website": "https://www.facebook.com/gabo.Lop.Al",
    "author": "Gabriel Lopez Alarcon",
    "installable": True,
    "application": False,
    "depends" : [
		"sale",
		"account",
	],
    "data": [
        "views/pack.xml",
    ],
}
