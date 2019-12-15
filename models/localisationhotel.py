# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LocalisationHotel(models.Model):
    _name = 'hotel.localisation_hotel'

    intitule_localisation_hotel = fields.Char()
    hotel_ids = fields.One2many(comodel_name='hotel.hotel', inverse_name='localisation_id')

    num_hotels = fields.Integer(string='Nombre d\'hotels', compute='comp_hotels')

    def comp_hotels(self):
        self.num_hotels = len(self.hotel_ids)
