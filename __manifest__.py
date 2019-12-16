# -*- coding: utf-8 -*-
{
    'name': "hotel",

    'summary': """
        Un module erp pour la gestion des hotels.""",

    'description': """
        Un module erp pour la gestion des hotels.""",

    'author': "Yosr Ben Hamida",
    'website': "http://www.yosrbh.msk.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/categorie_views.xml',
        'views/etage_chambre_views.xml',
        'views/hotel_views.xml',
        'views/chambre_views.xml',
        'views/vue_chambre_views.xml',
        'views/ville_views.xml',
        'views/metier_client_views.xml',
        'views/sejour_views.xml',
        'views/client_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
