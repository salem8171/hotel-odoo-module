# -*- coding: utf-8 -*-

from odoo import models, fields, api

class VueChambre(models.Model):
    _name = 'hotel.vue_chambre'
    _rec_name = 'intitule_vue_chambre'

    intitule_vue_chambre = fields.Char()
    chambre_ids = fields.One2many(comodel_name='hotel.chambre', inverse_name='vue_chambre_id')
    num_chambres = fields.Integer(string='Nombre de chambres', compute='comp_chambres')

    def comp_chambres(self):
        self.num_chambres = len(self.chambre_ids)
