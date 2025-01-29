from django.db import models

class Evento(models.Model):
    titolo=models.CharField(max_length=40)
    data=models.DateField(blank=True)
    descrizione=models.TextField()
    partecipanti= models.IntegerField(default=0,blank=True)

    def __str__(self):
        return self.titolo+" "+self.data+" "+self.descrizione+" "+self.partecipanti

    class Meta:
        verbose_name="Evento"
        verbose_name_plural="Eventi"