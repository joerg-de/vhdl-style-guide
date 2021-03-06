import os
import unittest

from vsg.rules import case
from vsg import vhdlFile
from vsg.tests import utils


# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','case','case_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)
lFileCase = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'comment_case_test_input.vhd'))
oFileCase = vhdlFile.vhdlFile(lFileCase)

lFileSequential = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','case','case_sequential_test_input.vhd'))
oFileSequential = vhdlFile.vhdlFile(lFileSequential)

class testRuleCaseMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = case.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'case')
        self.assertEqual(oRule.identifier, '001')
        dExpected = utils.add_violation_list([9,33,45,52,70])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = case.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'case')
        self.assertEqual(oRule.identifier, '002')
        dExpected = utils.add_violation_list([9,77])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = case.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'case')
        self.assertEqual(oRule.identifier, '003')
        dExpected = utils.add_violation_list([43,77])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004(self):
        oRule = case.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'case')
        self.assertEqual(oRule.identifier, '004')
        dExpected = utils.add_violation_list([17,29,52])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005(self):
        oRule = case.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'case')
        self.assertEqual(oRule.identifier, '005')
        dExpected = utils.add_violation_list([17,23,66])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006(self):
        oRule = case.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'case')
        self.assertEqual(oRule.identifier, '006')
        dExpected = [utils.add_violation(33)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007(self):
        oRule = case.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'case')
        self.assertEqual(oRule.identifier, '007')
        dExpected = [utils.add_violation(41)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

        oRule = case.rule_007()
        dExpected = []
        oRule.analyze(oFileSequential)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008(self):
        oRule = case.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'case')
        self.assertEqual(oRule.identifier, '008')
        dExpected = [utils.add_violation(43)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_009(self):
        oRule = case.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'case')
        self.assertEqual(oRule.identifier, '009')
        dExpected = [utils.add_violation(70)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_010(self):
        oRule = case.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'case')
        self.assertEqual(oRule.identifier, '010')
        dExpected = [utils.add_violation(33)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_011(self):
        oRule = case.rule_011()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'case')
        self.assertEqual(oRule.identifier, '011')
        dExpected = utils.add_violation_list([46,59])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_012(self):
        oRule = case.rule_012()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'case')
        self.assertEqual(oRule.identifier, '012')
        dExpected = utils.add_violation_list([11,12,16,22,23])
        oRule.analyze(oFileSequential)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_013(self):
        oRule = case.rule_013()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'case')
        self.assertEqual(oRule.identifier, '013')
        dExpected = [utils.add_violation(31)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_014(self):
        oRule = case.rule_014()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'case')
        self.assertEqual(oRule.identifier, '014')
        dExpected = [{'lines':[{'number': 41}], 'words_to_fix': {'CASE'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_015(self):
        oRule = case.rule_015()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'case')
        self.assertEqual(oRule.identifier, '015')
        dExpected = [{'lines':[{'number': 43}], 'words_to_fix': {'IS'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_016(self):
        oRule = case.rule_016()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'case')
        self.assertEqual(oRule.identifier, '016')
        dExpected = [{'lines':[{'number': 45}], 'words_to_fix': {'WHEN'}},
                     {'lines':[{'number': 52}], 'words_to_fix': {'wHEn'}},
                     {'lines':[{'number': 58}], 'words_to_fix': {'wheN'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_017(self):
        oRule = case.rule_017()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'case')
        self.assertEqual(oRule.identifier, '017')
        lExpected = []

        dViolation = utils.add_violation(79)
        dViolation['words_to_fix'] = {'END'}
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_018(self):
        oRule = case.rule_018()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'case')
        self.assertEqual(oRule.identifier, '018')
        lExpected = []
        dViolation = utils.add_violation(70)
        dViolation['words_to_fix'] = {'CASE'}
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_019(self):
        oRule = case.rule_019()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'case')
        self.assertEqual(oRule.identifier, '019')
        lExpected = []
        dViolation = utils.add_violation(87)
        dViolation['label'] = 'MY_LABEL'
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_020(self):
        oRule = case.rule_020()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'case')
        self.assertEqual(oRule.identifier, '020')
        lExpected = []

        dViolation = utils.add_violation(98)
        dViolation['label'] = 'LABEL'
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_021(self):
        oRule = case.rule_021()
        lExpected = [{'lines':[{'number': 19}], 'indent': 3},
                     {'lines':[{'number': 25}], 'indent': 3},
                     {'lines':[{'number': 24}], 'indent': 3},
                     {'lines':[{'number': 23}], 'indent': 3}]
        oRule.analyze(oFileCase)
        self.assertEqual(oRule.violations, lExpected)

