__author__ = 'AnkitAthos'
import pickle


def no_more_than_once(match_results):
    """
    Make sure that each student is matched at most once
    :param match_results: the pickle dump from match_algo
    :return: True or False
    """
    applicants = match_results['applicants']
    programs = match_results['programs']
    results = match_results['results']

    candidate_perspective = {applicant: [program for program in programs.keys() if applicant in results[program]]
                             for applicant in applicants.keys()}
    more_than_one = [candidate_perspective[candidate] for candidate in candidate_perspective.keys()
                     if len(candidate_perspective[candidate]) > 1]

    if more_than_one:
        print "SC001 failed\n: %s" % more_than_one
        return False
    else:
        print "SC001 Passed: No candidate appears more than once"
        return True


def no_more_than_capacity(match_results):
    """
    Make sure that each program has only as many residents as it can handle
    :param match_results: the pickle dump from match_algo
    :return: True or False
    """
    programs = match_results['programs']
    results = match_results['results']

    size_check = {program: len(results[program]) <= programs[program]['positions'] for program in results.keys()}
    more_than_capacity = {program for program in size_check.keys() if not size_check[program]}

    if more_than_capacity:
        print "SC002 failed\n %s" % more_than_capacity
        return False
    else:
        print "SC002 Passed: No program has more candidates than it can handle"
        return True

if __name__ == "__main__":
    match_results = pickle.load(open('match_results.p', 'rb'))
    no_more_than_once(match_results)
    no_more_than_capacity(match_results)
