from django.core import checks
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class OrderField(models.PositiveIntegerField):
    
    description = "Ordering field on a unique field"
    
    def __init__(self, unique_for_field=None, *args, **kwargs):
        self.unique_for_field = unique_for_field
        super().__init__(*args, **kwargs)
        
    def check(self, **kwargs):
        return [
            *super().check(**kwargs),
            *self._check_for_field_attribute(**kwargs),
        ]
    
    def _check_for_field_attribute(self, **kwargs):
        if self.unique_for_field is None:
            return [checks.Error("OrderField must define a unique for field")]
        elif self.unique_for_field not in [f.name for f in self.model._meta.get_fields()]:
            return [checks.Error('OrderField entered does not match an existing model field')]
        return []
    
    def pre_save(self, model_instance, add):
        if getattr(model_instance, self.attname, None) is None:
            qs = self.model.objects.all()
            try: 
                query = {
                    self.unique_for_field : getattr(
                        model_instance, self.unique_for_field
                    )
                }
                qs = qs.filter(**query)
            except ObjectDoesNotExist:
                value = 1
            value = 1
            return value
        
        return super().pre_save(model_instance, add)