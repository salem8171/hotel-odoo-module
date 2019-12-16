# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Hotel(models.Model):
    _name = 'hotel.hotel'
    _rec_name = 'intitule_hotel'

    intitule_hotel = fields.Char()
    nombre_etoile = fields.Integer()

    ville_id = fields.Many2one(comodel_name='hotel.ville')
    chambre_ids = fields.One2many(comodel_name='hotel.chambre', inverse_name='hotel_id')
    num_chambres = fields.Integer(string='Nombre de chambres', compute='comp_chambres')

    def comp_chambres(self):
        self.num_chambres = len(self.chambre_ids)
