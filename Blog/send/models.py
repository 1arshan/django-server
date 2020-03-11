from django.db import models

class Mail(models.Model):

    
    subject =models.CharField(blank =True,max_length =250)
    body =models.TextField(blank=True)
    from_email =models.EmailField()
    to_email =models.EmailField()
    sent_file =models.FileField(blank =True)

    def __str__(self):
        return self.subject

