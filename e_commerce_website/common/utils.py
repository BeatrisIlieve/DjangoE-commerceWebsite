from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible #in order to be used for models as well not only forms
class ValueInRangeValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if len(value) < self.min_value or len(value) > self.max_value:
            raise ValidationError(
                message=f'Value must be between {self.min_value} and {self.max_value}',
                code='invalid',
            )

    def __eq__(self, other): #in order to be used for models as well not only forms
        return (
            isinstance(other, self.__class__)
            and self.min_value == len(other.min_value)
            and self.max_value == len(other.max_value)
        )