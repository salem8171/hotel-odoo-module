# -*- coding: utf-8 -*-

from odoo import models, fields


class hotel(models.Model):
        _name = 'hotel.etagechambre'
        name = fields.Char('IntituleEtageChambre')
        code = fields.Integer('NombreEtageChambre')

