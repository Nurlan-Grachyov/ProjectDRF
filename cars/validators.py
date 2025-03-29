import re

from rest_framework.exceptions import ValidationError


class TitleValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        pattern = re.compile(r'^[A-Za-z0-9\.\-\ ]')
        tmp_val = dict(value).get(self.field)
        if not bool(pattern.match(tmp_val)):
            raise ValidationError("This field is not OK")


