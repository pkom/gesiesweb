from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import filters

class AuthenticateMixin(object):

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend,)
#    paginate_by = 10
#    max_paginate_by = 100
#    paginate_by_param = 'page_size'
    ordering_param = 'ordering'
