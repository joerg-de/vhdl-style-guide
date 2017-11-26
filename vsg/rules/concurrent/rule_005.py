
from vsg.rules.concurrent import concurrent_rule

import re


class rule_005(concurrent_rule):
    '''
    Concurrent rule 005 checks for labels on concurrent assignments.
    '''

    def __init__(self):
        concurrent_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Remove label on concurrent assignment.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isConcurrentBegin:
                if re.match('^\s*\w+\s*:\s*\w+\s*<=', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(oLine.line[oLine.line.find(':') + 1:])