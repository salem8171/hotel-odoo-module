# -*- coding: utf-8 -*-

from odoo import models, fields, api

class hotel(models.Model):
    _name = 'hotel.localisation_hotel'

    numero_localisation_hotel = fields.Integer()
    intitule_localisation_hotel = fields.Char()