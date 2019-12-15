# -*- coding: utf-8 -*-

from odoo import models, fields, api

class hotel(models.Model):
    _name = 'hotel.ville'

    numero_ville = fields.Integer()
    intitule_ville = fields.Char()