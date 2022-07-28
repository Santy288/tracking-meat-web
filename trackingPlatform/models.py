import hashlib
from django.db import models
from django.conf import settings
from django.utils import timezone
from trackingPlatform.wallet import sendTransaction


class Lot(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    product_name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now())
    track_code = models.CharField(max_length=6, default=None, null=True)
    txId = models.CharField(max_length=32, default=None, null=True)

    def writeOnChain(self):
        self.hash = hashlib.sha256(f"{self.track_code},"
                                   f"{self.description}".encode('utf-8')).hexdigest()

        self.txId = sendTransaction(self.hash)
        self.save()
        return self.txId
