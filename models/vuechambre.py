# -*- coding: utf-8 -*-

from odoo import models, fields, api

class VueChambre(models.Model):
    _name = 'hotel.vue_chambre'

    intitule_vue_chambre = fields.Char()
    chambre_ids = fields.One2many(comodel_name='hotel.chambre', inverse_name='vue_chambre_id')
