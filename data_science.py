__author__ = 'AnkitAthos'
import pickle


def which_ranks(match_results):
    """
    For each candidate get the rank he/she assigned of his/her match
    :param match_results: pickle dump from match_algo
    :return: a dictionary where each key is a candidate and value is the matched rank. For unmatched candidates, it will
    be -1
    """
    applicants = match_results['applicants']
    programs = match_results['programs']
    results = match_results['results']
    candidate_perspective = {applicant: [program for program in programs.keys() if applicant in results[program]]
                             for applicant in applicants.keys()}
    matched_ranks = {candidate: applicants[candidate].index(candidate_perspective[candidate][0])
                     if candidate_perspective[candidate] else -1 for candidate in candidate_perspective.keys()}

    return matched_ranks


def unmatched_applicants(match_results):
    """
    Get a list of unmatched applicants
    :param match_results:
    :return:
    """
    applicants = match_results['applicants']
    programs = match_results['programs']
    results = match_results['results']
    candidate_perspective = {applicant: [program for program in programs.keys() if applicant in results[program]]
                             for applicant in applicants.keys()}
    unmatched = [applicant for applicant in candidate_perspective.keys() if not candidate_perspective[applicant]]
    return unmatched

