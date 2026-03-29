from __future__ import absolute_import

import io
import logging
import unittest

from pycropml.transpiler.logger import configure_logging, get_logger
from pycropml.transpiler.main import Main


class TestLoggerConfiguration(unittest.TestCase):
    def test_configure_logging_debug_level(self):
        logger = configure_logging('DEBUG')

        self.assertEqual(logger.level, logging.DEBUG)
        self.assertTrue(logger.isEnabledFor(logging.DEBUG))

        child = get_logger('tests')
        self.assertTrue(child.isEnabledFor(logging.DEBUG))

    def test_configure_logging_does_not_duplicate_handlers(self):
        logger = configure_logging('INFO')
        before = len(logger.handlers)

        configure_logging('INFO')
        after = len(logger.handlers)

        self.assertEqual(before, after)

    def test_logs_emitted_for_transpile_failure_path(self):
        logger = configure_logging('DEBUG')
        stream = io.StringIO()
        handler = logging.StreamHandler(stream)
        handler.setFormatter(logging.Formatter('%(levelname)s [%(name)s] %(message)s'))
        logger.addHandler(handler)

        code = """
def test_array(toto):
    cdef float temps[10]
    return temps
"""

        try:
            c = Main(code, 'py')
            c.parse()
            c.to_ast(code)
        except Exception:
            pass
        finally:
            logger.removeHandler(handler)

        output = stream.getvalue()
        self.assertIn('DEBUG [pycropml.transpiler.main] Parsing source input', output)
        self.assertIn('DEBUG [pycropml.transpiler.main] Building AST', output)
        self.assertIn("ERROR [pycropml.transpiler.ast_transform] Variable 'toto' is not declared", output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
