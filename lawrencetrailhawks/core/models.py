import urlparse

from django.conf import settings
from django.core import urlresolvers
from django.db import models

from shorturls import default_converter as converter


class CommentMixin(models.Model):
    enable_comments = models.BooleanField(default=True)

    class Meta:
        abstract = True


class MachineTagMixin(models.Model):

    class Meta:
        abstract = True

    def get_machine_tags(self):
        machine_tag_namespace = getattr(settings, 'MACHINE_TAG_NAMESPACE', 'trailhawks')
        machine_tags = ['{0}:{1}={2}'.format(machine_tag_namespace, self._meta.module_name, self.pk)]
        return machine_tags


class ShortUrlMixin(object):

    def get_prefix(self):
        if not hasattr(self.__class__, '_prefixmap'):
            self.__class__._prefixmap = dict((m, p) for p, m in settings.SHORTEN_MODELS.items())
        key = str('%s.%s' % (self._meta.app_label, self.__class__.__name__)).lower()
        return self.__class__._prefixmap[key]

    # @models.permalink
    def get_short_url(self):
        try:
            prefix = self.get_prefix()
        except (AttributeError, KeyError):
            return ''

        tinyid = converter.from_decimal(self.pk)

        if hasattr(settings, 'SHORT_BASE_URL') and settings.SHORT_BASE_URL:
            return urlparse.urljoin(settings.SHORT_BASE_URL, prefix + tinyid)

        try:
            return urlresolvers.reverse('shorturls.views.redirect', kwargs={
                'prefix': prefix,
                'tiny': tinyid
            })
        except urlresolvers.NoReverseMatch:
            if hasattr(self, 'get_absolute_url'):
                return self.get_absolute_url()
            else:
                return None
