# -*- coding: utf-8 -*-

from odoo import models, fields


class EtageChambre(models.Model):
        _name = 'hotel.etagechambre'
        name = fields.Char('IntituleEtageChambre')
        code = fields.Char('NombreEtageChambre')

