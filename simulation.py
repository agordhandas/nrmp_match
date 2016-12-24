__author__ = "Ankit"

import numpy as np
import random
import pickle
import match_algo

#pull down list of programs
programs = pickle.load(open('programs.p', 'rb'))  # pick the first x programs to ensure fast running

#Make a list of 1000 applicants
#TODO: perhaps make it with a bunch of names
applicants = ['appl_' + str(x) for x in range(1600)]  # Generate a list of x applicants

# Each program invites 40 to 60 students from a group of 70 students
invited_applicants = {program: [applicants[x] for x in np.unique(np.random.choice(np.arange(0, 1600), random.randint(40, 60)))] for program in programs}

# Each program randomly ranks between 15 and 25 of the candidates it interviews
ranked_applicants = {program: ([invited_applicants[program][x] for x in np.unique(np.random.choice(len(invited_applicants[program]), random.randint(15, 25)))]) for program in programs}
ignore = {program: random.shuffle(ranked_applicants[program]) for program in programs}

#make a list of programs that each applicant interviewed at, and randomize it (to give a 'rank order list')
applicant_rankings = {applicant: ([program for program in programs if applicant in invited_applicants[program]]) for applicant in applicants}
_ignore = {applicant: random.shuffle(applicant_rankings[applicant]) for applicant in applicants}

#make a dictionary of number of positions that each program has (random number between 2 and 8 and its rankings)
program_list = {program: {'positions': random.randint (2, 8),
                          'rankings': ranked_applicants[program]}
                for program in programs}

#dump the program list and applicant list into a pickle file
pickle.dump(program_list, open ('program_list.p', 'wb'))
pickle.dump(applicant_rankings, open ('applicant_rankings.p', 'wb'))

#Run the match algorithm!
a = match_algo.run_algo (applicant_rankings, program_list)
#pickle.dump (a, 'simulation_result.py')
