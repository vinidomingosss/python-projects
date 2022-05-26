from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=120) #String com limite maximo de 120 caracteres
    done = models.BooleanField(default=False) #Sempre que for criado o objeto e nao passar a prop, ele vai ser false
    created_at = models.DateTimeField(auto_now_add=True) #Captura a hora e data que for criado um novo objeto todo