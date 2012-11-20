from django.conf import settings
from django.db import models


class MachineTagMixin(models.Model):
    class Meta:
        abstract = True

    def get_machine_tags(self):
        machine_tag_namespace = getattr(settings, 'MACHINE_TAG_NAMESPACE', 'trailhawks')
        machine_tags = ['{0}:{1}={2}'.format(machine_tag_namespace, self._meta.module_name, self.pk)]
        return machine_tags
