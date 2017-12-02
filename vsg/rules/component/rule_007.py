
from vsg.rules.component import component_rule
from vsg import check
from vsg import fix

import re


class rule_007(component_rule):
    '''Component rule 007 checks for a single space before the "is" keyword.'''

    def __init__(self):
        component_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'Remove extra spaces before "is" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentDeclaration and len(oLine.line.split()) > 2:
                check.is_single_space_before(self, 'is', oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            fix.enforce_one_space_before_word(self, oLine, 'is')
