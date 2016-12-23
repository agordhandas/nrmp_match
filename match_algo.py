__author__ = 'Ankit'

from match_classes import Applicants
from match_classes import tempMatchBuffer

def run_algo(applicant_rankings, program_list):
    applicants_class = Applicants(applicant_rankings)
    program_class = tempMatchBuffer(program_list)

    while not applicants.isEmpty:
        applicant = applicants_class.pop()
        for program in applicant_class.applicantRankingList(applicant):
            if program_class.didProgramRank(program, applicant):
                lower_candidate = program_class.lowerRankedCandidate(program, applicant)
                if program_class.checkProgramHasSpace(program):
                    program_class.tempMatch(program, applicant)
                elif lower_candidate:
                    program_class.unseatCandidate(program, lower_candidate)
                    applicants_class.reinsertApplication(lower_candidate)
                    program_class.tempMatch(program, applicant)
    return program_class.match_buffer

