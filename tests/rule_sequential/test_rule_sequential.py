
import unittest
from modules import rule_sequential
from modules import vhdlFile

# Read in test file used for all tests
oFile = vhdlFile.vhdlFile('tests/rule_sequential/sequential_test_input.vhd')

class testRuleSequentialMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = rule_sequential.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'sequential')
        self.assertEqual(oRule.identifier, '001')
        dExpected = [14,20,28,56,66,73,81,89,90]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = rule_sequential.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'sequential')
        self.assertEqual(oRule.identifier, '002')
        dExpected = [26,33,65,83]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = rule_sequential.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'sequential')
        self.assertEqual(oRule.identifier, '003')
        dExpected = [38,40,81,89]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004(self):
        oRule = rule_sequential.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'sequential')
        self.assertEqual(oRule.identifier, '004')
        dExpected = [54,55,74]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

if __name__ == '__main__':
    unittest.main()