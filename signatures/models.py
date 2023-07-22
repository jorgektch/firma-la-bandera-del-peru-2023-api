from django.db import models
from datetime import datetime   

class Signature(models.Model):
    full_name = models.CharField("Nombre completo", max_length = 50, default = "")
    message_text = models.CharField("Contenido del mensaje", max_length = 280, default = "")
    pub_date = models.DateTimeField("Fecha de publicación", blank=True, default=datetime.now)
    status = models.CharField("Estado", max_length = 20, choices=[('Pendiente', 'Pendiente'), ('Aprobado', 'Aprobado'), ('Desaprobado', 'Desaprobado')], default='Pendiente')
    def __str__(self):
        return self.full_name + " " + self.message_text + " " + self.pub_date.strftime("%d/%m/%Y, %H:%M:%S") + self.status