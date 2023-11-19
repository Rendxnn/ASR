from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from store.models import Ladrillo


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Ladrillo, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product}"

    def get_absolute_url(self):
        return reverse("cart:cart_detail")
