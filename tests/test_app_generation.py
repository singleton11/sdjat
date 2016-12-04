import unittest
from unittest import TestCase

import sh
from cookiecutter.main import cookiecutter


class AppGenerationTestCase(TestCase):
    """Test case for app generation"""

    def tearDown(self):
        sh.rm('-rf', '/tmp/polls')

    def test_generation(self):
        """Test standard app generation"""
        cookiecutter('../', no_input=True, output_dir='/tmp',
                     overwrite_if_exists=True)

        file_list = (
            (
                sh.ls('/tmp/polls'),
                (
                    'apps.py',
                    '__init__.py',
                    'models.py',
                )
            ),
            (
                sh.ls('/tmp/polls/tests'),
                (
                    '__init__.py',
                    'test_models.py'
                )
            )
        )

        for ls in file_list:
            for file in ls[1]:
                self.assertIn(file, ls[0])

    if __name__ == '__main__':
        unittest.main()