import six
import waffle

from django.utils.functional import SimpleLazyObject
from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module


def import_attribute(import_path=None, options=None):
    if import_path is None:
        raise ImproperlyConfigured('No import path was given.')
    try:
        dot = import_path.rindex('.')
    except ValueError:
        raise ImproperlyConfigured("%s isn't a module." % import_path)
    module, classname = import_path[:dot], import_path[dot + 1:]
    try:
        mod = import_module(module)
    except ImportError as e:
        raise ImproperlyConfigured('Error importing module %s: "%s"' %
                                   (module, e))
    try:
        return getattr(mod, classname)
    except AttributeError:
        raise ImproperlyConfigured(
            'Module "%s" does not define a "%s" class.' % (module, classname))


class LazyBackend(SimpleLazyObject):

    def __init__(self, import_path, options):
        backend = import_attribute(import_path)
        super(LazyBackend, self).__init__(lambda: backend(**options))


class ProxyStorage(object):

    local = 'django.core.files.storage.FileSystemStorage'
    remote = 'storages.backends.s3boto.S3BotoStorage'
    local_options = None
    remote_options = None

    def __init__(self, local=None, remote=None, local_options=None, remote_options=None):
        self.local_path = local or self.local
        self.local_options = local_options or self.local_options or {}
        self.local = self._load_backend(backend=self.local_path,
                                        options=self.local_options)

        self.remote_path = remote or self.remote
        self.remote_options = remote_options or self.remote_options or {}
        self.remote = self._load_backend(backend=self.remote_path,
                                         options=self.remote_options)

    def _load_backend(self, backend=None, options=None, handler=LazyBackend):
        if backend is None:  # pragma: no cover
            raise ImproperlyConfigured("The ProxyStorage class '%s' "
                                       "doesn't define a needed backend." %
                                       (self, backend))
        if not isinstance(backend, six.string_types):
            raise ImproperlyConfigured("The ProxyStorage class '%s' "
                                       "requires its backends to be "
                                       "specified as dotted import paths "
                                       "not instances or classes" % self)
        return handler(backend, options)

    def get_storage(self):
        """
        Returns the storage backend instance responsible for the file
        with the given name (either local or remote). This method is
        used in most of the storage API methods.

        :param name: file name
        :type name: str
        :rtype: :class:`~django:django.core.files.storage.Storage`
        """
        if waffle.switch_is_active('use_s3_for_storage_switch'):
            return self.remote
        else:
            return self.local

    def accessed_time(self, name):
        return self.get_storage().accessed_time(name)

    def created_time(self, name):
        return self.get_storage().created_time(name)

    def delete(self, name):
        return self.get_storage().delete(name)

    def exists(self, name):
        return self.get_storage().exists(name)

    def get_available_name(self, name):
        return self.get_storage().get_available_name(name)

    def get_valid_name(self, name):
        return self.get_storage().get_valid_name(name)

    def listdir(self, path):
        return self.get_storage().listdir(path)

    def modified_time(self, name):
        return self.get_storage().modified_time(name)

    def open(self, name, mode='rb'):
        return self.get_storage().open(name, mode='rb')

    def path(self, name):
        return self.get_storage().path(name)

    def save(self, name, content):
        return self.get_storage().save(name, content)

    def size(self, name):
        return self.get_storage().size(name)

    def url(self, name):
        return self.get_storage().url(name)
