from django.db import models

# Create your models here.


class Share(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    share_id = models.CharField(max_length=10)
    share_data = models.TextField()

    def createNewShare(self, user_id, share_id, share_data):
        self.user_id = user_id
        self.share_data = share_data
        self.share_id = share_id

    def __str__(self):
        return str(self.share_id + "-" + self.user_id)


