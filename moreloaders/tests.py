import os
import re
from django.conf import settings
from django.conf import settings
from django.test import TestCase
from django.test.utils import override_settings
from django.template import TemplateDoesNotExist, Context, Template
from django.template import loader
try:
    from django.utils._os import upath
except ImportError as e:
    upath = unicode


@override_settings(
    TEMPLATE_LOADERS=(
        ('moreloaders.mostlycached.Loader', (
            'django.template.loaders.app_directories.Loader',
        )),
    )
)
class MostlyCachedTests(TestCase):
    def test_most_things_should_cache(self):
        filename = 'test.html'
        t1, name = loader.find_template(filename)
        self.assertIn(filename,
                      loader.template_source_loaders[0].template_cache)
        self.assertIsNone(name)
        self.assertTrue(isinstance(t1, Template))

    def test_excluding_by_regex_file_extension(self):
        filename = 'test.json'
        t1, name = loader.find_template(filename)
        self.assertNotIn(filename,
                         loader.template_source_loaders[0].template_cache)
        self.assertIsNone(name)
        self.assertTrue(isinstance(t1, Template))

    def test_regex_start_of_path(self):
        filename = 'other.txt'
        t1, name = loader.find_template(filename)
        self.assertNotIn(filename,
                         loader.template_source_loaders[0].template_cache)
        self.assertIsNone(name)
        self.assertTrue(isinstance(t1, Template))

    def test_regex_start_of_path_specific_dirs(self):
        filename = 'other.txt'
        look_in = os.path.join(os.path.dirname(upath(__file__)), 'templates')
        t1, name = loader.find_template(filename, (look_in,))
        self.assertNotIn(filename,
                         loader.template_source_loaders[0].template_cache)
        self.assertIsNone(name)
        self.assertTrue(isinstance(t1, Template))

    def test_regex_character_length(self):
        for filename in ('xab.html', 'xaa.html'):
            t1, name = loader.find_template(filename)
            self.assertNotIn(filename,
                             loader.template_source_loaders[0].template_cache)
            self.assertIsNone(name)
            self.assertTrue(isinstance(t1, Template))

        filename = 'xaaa.html'
        t1, name = loader.find_template(filename)
        self.assertIn(filename,
                      loader.template_source_loaders[0].template_cache)
        self.assertIsNone(name)
        self.assertTrue(isinstance(t1, Template))

    def test_regex_or(self):
        for filename in ('ya.html', 'yb.html'):
            t1, name = loader.find_template(filename)
            self.assertNotIn(filename,
                             loader.template_source_loaders[0].template_cache)
            self.assertIsNone(name)
            self.assertTrue(isinstance(t1, Template))

        filename = 'yc.html'
        t1, name = loader.find_template(filename)
        self.assertIn(filename,
                      loader.template_source_loaders[0].template_cache)
        self.assertIsNone(name)
        self.assertTrue(isinstance(t1, Template))
