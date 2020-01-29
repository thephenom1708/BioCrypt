from django.db import models
import secrets
import hashlib

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    pin_hash = models.CharField(max_length=500)
    fingerprint = models.TextField(default="")
    coordinates = models.CharField(max_length=100, default="")

    def createNewUser(self, name, username, pin):
        self.user_id = secrets.token_hex(10)
        self.name = name
        self.username = username
        sha = hashlib.sha256()
        sha.update(pin.encode('utf-8'))
        self.pin_hash = sha.hexdigest()
        self.fingerprint = ""
        self.coordinates = ""

    def __str__(self):
        return str(self.user_id + '-' + self.username)
