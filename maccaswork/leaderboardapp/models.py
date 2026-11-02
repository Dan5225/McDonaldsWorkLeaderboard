from django.db import models

# Create your models here.
class Firstname(models.Model):
    first_name_text = models.CharField(max_length=20)
    def __str__(self):
        return self.first_name_text

class Lastname(models.Model):
    last_name_text = models.CharField(max_length=20)
    def __str__(self):
        return self.last_name_text
    

class Fullname(models.Model):
    first_name = models.ForeignKey(Firstname, on_delete=models.CASCADE)
    last_name = models.ForeignKey(Lastname, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Tehs(models.Model):
    participant = models.OneToOneField(
        Fullname,
        on_delete=models.CASCADE,
        related_name='tehs'
    )
    tehs = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.participant} - {self.tehs} TEHS"