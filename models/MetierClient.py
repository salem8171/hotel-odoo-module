# -*- coding: utf-8 -*-

from odoo import models, fields, api

class hotel(models.Model):
    _name = 'hotel.metier'

    numero_metier = fields.Integer()
    intitule_metier = fields.Char()