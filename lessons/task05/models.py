from django.db import models


class CoinFlip(models.Model):
    CHOICES = (('H', 'Head'), ('T', 'Tail'))
    side = models.CharField(choices=CHOICES, max_length=1)
    timestamp = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_last_flip(n: int):
        result = CoinFlip.objects.order_by('-timestamp')
        return result[:n]

    def __str__(self):
        return f"Сторона: {self.side}, время: {self.timestamp.strftime('%d-%h-%Y, %H:%M:%S')}."


class DieToss(models.Model):
    result = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_last_toss(n: int):
        result_ = DieToss.objects.order_by('-timestamp')
        return result_[:n]

    def __str__(self):
        return f"Сторона: {self.result}, время: {self.timestamp.strftime('%d-%h-%Y, %H:%M:%S')}."


class RandomNum(models.Model):
    result = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_last_num(n: int):
        result_ = RandomNum.objects.order_by('-timestamp')
        return result_[:n]

    def __str__(self):
        return f"Сторона: {self.result}, время: {self.timestamp.strftime('%d-%h-%Y, %H:%M:%S')}."
