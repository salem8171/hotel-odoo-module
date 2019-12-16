# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Hotel(models.Model):
    _name = 'hotel.hotel'

    intitule_hotel = fields.Char()
    nombre_etoile = fields.Integer()

    ville_id = fields.Many2one(comodel_name='hotel.ville')
    localisation_id = fields.Many2one(comodel_name='hotel.localisation_hotel')
    chambre_ids = fields.One2many(comodel_name='hotel.chambre', inverse_name='hotel_id')
    num_chambres = fields.Integer(string='Nombre de chambres', compute='comp_chambres')

    def comp_chambres(self):
        self.num_chambres = len(self.chambre_ids)
