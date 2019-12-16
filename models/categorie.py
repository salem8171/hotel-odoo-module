# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CategorieChambre(models.Model):
    _name = 'hotel.categorie'

    intitule_categorie = fields.Char()
    chambre_ids = fields.One2many(comodel_name='hotel.chambre', inverse_name='categorie_id')
    num_chambres = fields.Integer(string='Nombre de chambres', compute='comp_chambres')

    def comp_chambres(self):
        self.num_chambres = len(self.chambre_ids)
