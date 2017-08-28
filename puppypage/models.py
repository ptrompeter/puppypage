"""Models for Puppypage backend."""

from django.conf import settings
from django.db import models


class Workshop(models.Model):
    """Defines a workshop to which sessions and tokens will be added."""

    name = models.CharField("Workshop Name", max_length=200)
    start_date = models.DateField()
    frequency = models.CharField(max_length=200, null=True, blank=True)
    max_clients = models.IntegerField("maximum clients", null=True, blank=True)
    instructors = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    null=True,
                                    default=None,
                                    )


class Session(models.Model):
    """Defines an individual workshop session, to which tokens are assigned."""

    workshop = models.ForeignKey(Workshop,
                                 on_delete=models.CASCADE,
                                 related_name='sessions',
                                 null=False,
                                 default=None,
                                 )
    date = models.DateTimeField('date and time')
    instructors = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    null=True,
                                    default=None,
                                    )
    max_tokens = models.IntegerField()


class Token(models.Model):
    """Defines a flexible unit that assigns a user to a class."""

    workshop = models.ForeignKey(Workshop,
                                 on_delete=models.CASCADE,
                                 null=True,
                                 blank=True,
                                 )
    created = models.DateTimeField('date created')
    locked = models.BooleanField(default=False)
    assigned = models.BooleanField(default=False)
    session = models.ForeignKey(Session,
                                null=True,
                                blank=True,
                                related_name='tokens',
                                )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             null=False,
                             default=None,
                             )
