#encoding: utf-8
from django.db import models
from django.conf import settings

from config.models import Config

def append_data(request):
    data = get_data(request)
    return dict(data=data)


def get_data(request):

    fields = Config._meta.fields
    config = Config.objects.first()
    context = dict()
    if config:
        for field in fields:
            if (isinstance(field, models.ImageField) or isinstance(field, models.FileField)):
                if getattr(config, field.name):
                    context[field.name] = getattr(config, field.name).url
            else:
                context[field.name] = getattr(config, field.name)
    context['debug'] = settings.DEBUG
    return context
