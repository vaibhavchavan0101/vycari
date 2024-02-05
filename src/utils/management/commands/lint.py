from django.core.management.base import BaseCommand

from pylint.lint import Run
# from pylama.main import check_path, parse_options

ERROR_COUNT = 5
CONVENTION_COUNT = 5
WARNINGS = 5
CODEBASE = './src/'
THRESHOLD_LINT_SCORE = 9.5


class Command(BaseCommand):

    def run_pylint(self, path):

        results = Run(['--load-plugins=pylint_django',
                       '--rcfile=pylintrc', path], do_exit=False)
        if results.linter.stats.error > ERROR_COUNT \
            or results.linter.stats.convention > CONVENTION_COUNT \
            or results.linter.stats.warning > WARNINGS:
            print(
                "Codebase has failed set standards, Please correct above mentioned issues,"
                  f"Current Score is: {results.linter.stats.global_note}, "
                  f"Errors: {results.linter.stats.error}, "
                  f"Convention issues: {results.linter.stats.convention}, "
                  f"Warnings: {results.linter.stats.warning}"
            )

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, nargs='?', default=CODEBASE)

    def handle(self, *args, **options):
        """
        Overridden get handler method, call run_pylint for static analysis of code
        """
        self.run_pylint(options['path'])
