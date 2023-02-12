# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Pelicula(models.Model):
    _name = 'alquiler.pelicula'
    _description = 'Módulo para guardar las películas'

    name = fields.Char(string='Título de la película', help='Título', required=True)
    #he puesto movie_id como one2many porque es un préstamo digital, así que una peli puede generar muchos préstamos
    pelicula_id = fields.One2many('alquiler.prestamo', 'pelicula_id', required=True)
    director = fields.Char(string='Director', help='Director', required=True)
    year = fields.Integer(string='Año', help='Año')
    description = fields.Text(string='Descripción', string='Breve descripción')
    rented = fields.Boolean(string='Alquilado', string='¿Está alquilada?', required=True, default=False)
    genre_id = fields.Many2one('alquiler.genero', 'id', string="ID del género", required=True, readonly=True)


class Genero(models.Model):
    _name = 'alquiler.genero'
    _description = 'Módulo para almacenar los géneros'

    name = fields.Char(string='Género', help='Nombre del género', required=True)
    description = fields.Text(string='Descripción', string='Breve descripción')
    id = fields.One2many('alquiler.pelicula', string="ID del género")


class Cliente(models.Model):
    _name = 'alquiler.cliente'
    _description = 'Módulo para almacenar los clientes'

    name = fields.Char(string='Nombre', help='Nombre del cliente', required=True)
    surname = fields.Char(string='Apellidos', help='Apellidos del cliente', required=True)
    id = fields.One2many('alquiler.prestamo', 'client_id', required=True)
    prestamos = fields.Integer(string='Préstamos', help='Número de préstamos acumulados', required=True, readonly=True, compute=contar_prestamos)
    type = fields.Selection([(1,'Afiliado'),(2,'Premium'),(3,'Estándar')],string="Tipo", help='Clase de cliente')

#esta función usa un decorador que la hace depender de prestamo_ids
    @api.depends('prestamo_ids')
    def contar_prestamos(self):
        for cliente in self:
            cliente.prestamos = len
     
class Prestamo(models.Model):
    _name = 'alquiler.prestamo'
    _description = 'Módulo para almacenar los prestamos'

    pelicula_id = fields.Many2one('alquiler.pelicula', string = 'ID de película')
    id = fields.Integer(string='Nombre del género', help='Nombre', required=True)
    client_id = fields.Many2one('alquiler.cliente', 'id', string = 'ID del cliente')
    type = fields.Selection([(1,'Un día'),(2,'Dos días'),(3,'Una semana')],string="Tipo", help='Clase de préstamo')
     