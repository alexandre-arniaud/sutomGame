from django.db import models


class Mot(models.Model):
    id = models.AutoField(primary_key=True)
    mot = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.mot.upper()}"