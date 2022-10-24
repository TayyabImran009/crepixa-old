import factory

from django.contrib.auth import get_user_model


class UserFactory(factory.DjangoModelFactory):
    email = factory.Sequence(lambda o: 'user{}@example.com'.format(o))
    username = factory.Sequence(lambda o: 'user{}'.format(o))
    is_active = True
    is_staff = False
    is_superuser = False

    class Meta:
        model = get_user_model()
