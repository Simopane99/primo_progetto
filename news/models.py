from django.db import models

# Create your models here.
class Giornalista(models.Model):
    nome=models.CharField(max_length=20)
    cognome=models.CharField(max_length=20)
    anno_di_nascita=models.DateField(blank=True)

    def __str__(self):
        return self.nome+" "+self.cognome
    
    class Meta:
        verbose_name="Giornalista"
        verbose_name_plural="Giornalisti"

class Articolo(models.Model):
    """ il modello generico di un articolo di news """
    titolo=models.CharField(max_length=100)#necessita della lunghezza massima 
    contenuto = models.TextField()
    giornalista = models.ForeignKey(Giornalista, on_delete= models.CASCADE, related_name="articoli")
    data=models.DateField(blank=True)
    visualizzazioni=models.IntegerField(default=0,blank=True)

    def __str__(self):
        return self.titolo
    
    class Meta:
        verbose_name="Articolo"
        verbose_name_plural="Articoli"