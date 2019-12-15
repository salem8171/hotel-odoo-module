# -*- coding: utf-8 -*-

from odoo import models, fields, api

class hotel(models.Model):
    _name = 'hotel.vue_chambre'
    numero_vue_chambre = fields.Integer()
    intitule_vue_chambre = fields.Char()