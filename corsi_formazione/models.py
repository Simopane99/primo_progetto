from django.db import models

class Corso(models.Model):
    titolo=models.CharField(max_length=30)
    descrizione=models.TextField()
    data_inizio=models.DateField(blank=True)
    data_fine=models.DateField(blank=True)
    posti_disponibili=models.IntegerField(default=0)

    def __str__(self):
        return self.titolo+" "+self.descrizione
    
    class Meta:
        verbose_name="Corso"
        verbose_name_plural="Corsi"
