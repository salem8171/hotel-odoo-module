# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Ville(models.Model):
    _name = 'hotel.ville'
    _rec_name = 'intitule_ville'

    intitule_ville = fields.Char()
    hotel_ids = fields.One2many(comodel_name='hotel.hotel', inverse_name='ville_id')
    num_hotels = fields.Integer(string='Nombre d\'hotels', compute='comp_hotels')

    def comp_hotels(self):
        self.num_hotels = len(self.hotel_ids)
