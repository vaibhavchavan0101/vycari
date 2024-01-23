from django.test.runner import DiscoverRunner
from django.test import TestCase

class NoDbTestRunner(TestCase, DiscoverRunner):
  """ A test runner to test without database creation """
  
  def setup_databases(self, **kwargs):
    """ Override the database creation defined in parent class """
    pass

  def teardown_databases(self, old_config, **kwargs):
    """ Override the database teardown defined in parent class """
    pass