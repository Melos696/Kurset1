from django.db import models

class Kurs(models.Model):
    titulli = models.CharField(max_length=100)
    pershkrimi = models.TextField()
    data_fillimit = models.DateField()
    cmimi = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.titulli
