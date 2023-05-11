# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import psutil

class DashboardController(http.Controller):

    @http.route('/GEI_dashboard/dashboard/', type='http', auth='user')
    def my_dashboard(self):
        data = self._get_server_data()
        return request.render('GEI_dashboard.dashboard_template', {'data': data})

    def _get_server_data(self):
        # Aquí iría la lógica para obtener los datos del servidor Windows
        cpu_percent = psutil.cpu_percent()
        mem_percent = psutil.virtual_memory().percent
        disk_percent = psutil.disk_usage('/').percent
        data = {
            'cpu_percent': cpu_percent,
            'mem_percent': mem_percent,
            'disk_percent': disk_percent
        }
        return data
