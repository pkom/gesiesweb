from django.conf import settings
from django.db import models
from model_utils.models import TimeStampedModel

class Profesor(TimeStampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, db_index=True)
