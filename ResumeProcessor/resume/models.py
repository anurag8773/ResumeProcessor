from django.db import models

class Candidate(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    email = models.EmailField(unique=True, verbose_name="Email Address")
    mobile_number = models.CharField(max_length=15, verbose_name="Mobile Number")

    class Meta:
        verbose_name = "Candidate"
        verbose_name_plural = "Candidates"

    def __str__(self):
        return f"{self.first_name} ({self.email})"
