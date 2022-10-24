from django.db.models import Subquery


class Array(Subquery):
    template = 'ARRAY(%(subquery)s)'
