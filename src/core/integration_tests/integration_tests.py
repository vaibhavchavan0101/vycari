from django.test.runner import DiscoverRunner
from django.test import TestCase

class NoDbTestRunner(TestCase, DiscoverRunner):
  """ A test runner to test without database creation """
  # def __init__(self, *args, **kwargs):
  #     # Ensure the 'verbosity' argument is not passed to the parent class
  #     super().__init__(*args, **kwargs)

  def setup_databases(self, **kwargs):
    """ Override the database creation defined in parent class """
    pass

  def teardown_databases(self, old_config, **kwargs):
    """ Override the database teardown defined in parent class """
    pass