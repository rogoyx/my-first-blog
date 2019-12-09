from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class MinimumLengthValidator:
    def __init__(self, min_length=5):
        self.min_length = min_length

    def validate(self, password, user=None):
        print('aaa')
        print(len(password), self.min_length)
        if len(password) < self.min_length:
            print('bbb')
            raise ValidationError(
                _("Пароль должен содержать как минимум %(min_length)d символов."),
                code='password_too_short',
                params={'min_length': self.min_length},
            )

    def get_help_text(self):
        return _(
            "Пароль должен содержать как минимум %(min_length)d символов."
            % {'min_length': self.min_length}
        )