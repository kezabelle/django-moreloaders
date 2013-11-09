import re
import hashlib
from django.conf import settings
from django.template.loaders import cached


class Loader(cached.Loader):
    """
    Mostly Cached Loader

    If no `MOSTLYCACHED_EXCLUDES` is found in your Django project's
    settings module, this should behave *identically* to the standard
    ``cached.Loader`` recommended for production.

    If `MOSTLYCACHED_EXCLUDES` is given, and the `template_name` matches
    one of the regular expressions therein, it is *not kept in the
    process' template cache*, instead it is re-read from the origin
    Loader on every usage.

    See `test_settings.py` for example `MOSTLYCACHED_EXCLUDES`,
    and `moreloaders/tests.py` for test cases.
    """
    def load_template(self, template_name, template_dirs=None,
                      exclusions=None):
        """
        Do whatever the `cached.Loader` wants, and then possibly
        through away the cache key.
        """
        if exclusions is None:
            exclusions = getattr(settings, 'MOSTLYCACHED_EXCLUDES', ())

        template_instance, origin = super(Loader, self).load_template(
            template_name=template_name, template_dirs=template_dirs)

        # copied directly from cached.Loader; allows us to kill certain
        # templates even if directories were passed in.
        key = template_name
        if template_dirs:
            key = '-'.join([
                template_name,
                hashlib.sha1('|'.join(template_dirs)).hexdigest()
            ])

        for regex in exclusions:
            delete_confirmations = (
                re.search(pattern=regex, string=template_name),
                key in self.template_cache
            )
            # we've found a match, so subsequent exclusions are irrelevent.
            if all(delete_confirmations):
                del self.template_cache[key]
                break
        return template_instance, origin
