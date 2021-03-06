import unittest
from orthrus.commands import *
from orthrusutils.orthrusutils import *

class TestOrthrusDestroy(unittest.TestCase):

    description = 'Test harness'
    orthrusdirname = '.orthrus'

    def test_destroy(self):
        args = parse_cmdline(self.description, ['destroy'])
        cmd = OrthrusDestroy(args, self.config, 'y')
        self.assertTrue(cmd.run())

    def setUp(self):
        self.config = {'orthrus' : {'directory': self.orthrusdirname}}
        args = parse_cmdline(self.description, ['create', '-asan'])
        cmd = OrthrusCreate(args, self.config)
        cmd.run()