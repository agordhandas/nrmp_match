__author__ = "Ankit"

import numpy as np
import random
import pickle
import match_algo
programs = pickle.load (open ('programs.p', 'rb'))[0:5]
applicants = ['appl_'+str(x) for x in range(1000)]

invited_applicants = {program: [applicants[x] for x in np.unique(np.random.choice(np.arange(0, 70), random.randint(40, 60)))] for program in programs}

ranked_applicants = {program: ([invited_applicants[program][x] for x in np.unique(np.random.choice(len(invited_applicants[program]), random.randint(15, 25)))]) for program in programs}
ignore = {program: random.shuffle(ranked_applicants[program]) for program in programs}

applicant_rankings = {applicant: ([program for program in programs if applicant in invited_applicants[program]]) for applicant in applicants}
ignore = {applicant: random.shuffle(applicant_rankings[applicant]) for applicant in applicants}

program_list = {program: {'positions': random.randint (2, 8),
                          'rankings': ranked_applicants[program]}
                  for program in programs}

pickle.dump (program_list, open ('program_list.p', 'wb'))
pickle.dump (applicant_rankings, open ('applicant_rankings.p', 'wb'))

a = match_algo.run_algo (applicant_rankings, program_list)
#pickle.dump (a, 'simulation_result.py')
