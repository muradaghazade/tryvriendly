from django.db import models

class BetaUsers(models.Model):
    full_name = models.CharField(max_length=100)
    company = models.CharField(max_length=180)
    email = models.EmailField(('email adress'), unique=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Beta User'
        verbose_name_plural = 'Beta Users'

    def __str__(self):
        return f'{self.full_name}'
