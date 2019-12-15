# -*- coding: utf-8 -*-

from odoo import models, fields, api

class hotel(models.Model):
    _name = 'hotel.chambre'

    numero_chambre = fields.Integer()
    intitule_chambre = fields.Char()
    surface_chambre = fields.Integer()
    prix_sejour_une_nuit = fields.Integer()
    numero_intitule_vue_chambre = fields.Integer()
    numero_etage_chambre = fields.Integer()
    numero_categorie_chambre= fields.Integer()
    numero_hotel= fields.Integer()