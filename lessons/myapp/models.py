from django.db import models

# Create your models here.

# class CoinFlip(models.Model):
#     side = models.CharField(choices=["Heads", "Tails"])
#     timestamp = models.DateTimeField(auto_now_add=True)
#
#     @staticmethod
#     def get_last_flip(n: int):
#         result = CoinFlip.objects.order_by('-timestamp')
#         return result[:n]