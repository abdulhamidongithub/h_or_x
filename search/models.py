from django.db import models

class Words(models.Model):
    id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return f"{self.word}"
    class Meta:
        db_table = "words"


class Wrong(models.Model):
    wrong_one = models.CharField(max_length=20, unique=True)
    words_id = models.ForeignKey(Words, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.wrong_one}"
    class Meta:
        db_table = "wrong"
