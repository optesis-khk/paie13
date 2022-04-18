# -*- coding: utf-8 -*-
from datetime import date, datetime
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.tools.misc import format_date


class OptesisPayrollInputs(models.Model):
    _name = "optesis.payslip.input"
    _description = "Model to create inputs for employee"

    name = fields.Char(readonly=True, compute="_get_name")
    input_id = fields.Many2one('hr.payslip.input.type', 'Entrée', required=True)
    employee_id = fields.Many2one('hr.employee', 'Employé', required=True)
    date_from = fields.Date(string='From', required=True,
        default=lambda self: fields.Date.to_string(date.today().replace(day=1)))
    date_to = fields.Date(string='To', required=True,
        default=lambda self: fields.Date.to_string((datetime.now() + relativedelta(months=+1, day=1, days=-1)).date()))
    value = fields.Float('Amount/Quantité', default=0.0)
    
    
    @api.onchange('input_id', 'employee_id')
    def _get_name(self):
        for rec in self:
            if rec.input_id and rec.employee_id:
                rec.name = '%s - %s ' % ('Entrée ' + rec.employee_id.name or '', format_date(rec.env, rec.date_from, date_format="MMMM y"))