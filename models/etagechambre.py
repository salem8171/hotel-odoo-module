# -*- coding: utf-8 -*-

from odoo import models, fields


class EtageChambre(models.Model):
    _name = 'hotel.etagechambre'

    name = fields.Char('IntituleEtageChambre')
    chambre_ids = fields.One2many(comodel_name='hotel.chambre', inverse_name='etagechambre_id')
    num_chambres = fields.Integer(string='Nombre de chambres', compute='comp_chambres')
    
    def comp_chambres(self):
        self.num_chambres = len(self.chambre_ids)
