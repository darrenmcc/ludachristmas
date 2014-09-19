import sys
import copy
import json
import random
from datetime import datetime

from models import Family, FamilyMember

# email: mccleary.ludachristmas@gmail.com

# TODO:
# write/store data (redis?)
# naughty/nice system
# deploy to heroku

def run():
    F = Family()
    F.create_pollyanna()






    # attempts = 100 # 100 to be safe, most I've seen it take is 8
    # familylist_duplicate = copy.deepcopy(family_list)
    # # initial shuffle
    # random.shuffle(familylist_duplicate)
    # for i in xrange(attempts):
    #     for member in family_list:
    #         random.shuffle(familylist_duplicate)
    #         # if not member.pollyanna: # already has a pollyanna, likely from naughty/nice algorithm
    #         for choice in familylist_duplicate:
    #             # shuffled so each next element should be random
    #             print "attempting to match:",member.name.upper(),"and",choice.name.upper()
    #             if member.can_match(choice):
    #                 member.pollyanna = choice.name
    #                 familylist_duplicate.remove(choice)
    #                 break # pollyanna found for this family member, stop looking
    #         else:
    #             # that person couldn't be matched with anyone, start over
    #             break 
    #     if all_matched(family_list):
    #         break
    # # no break = failed in attempts allotted 
    # else: 
    #     print "Could not create the Pollyanna in {} attempts. Check yo data.".format(i+1)
    #     return False
    # break = success, everyone matched
    # print "Completed on attempt: {n}\n{line}".format(n=i+1, line="-"*20)
    # current_year = str(datetime.now().year)
    # filename = current_year + ".txt"
    # with open(filename, "w") as f:
    #     f.write("name,pollyanna\n")
    #     for member in family_list:
    #         f.write("{},{}\n".format(member.name, member.pollyanna))
    #         print "  {} --> {}".format(member.name, member.pollyanna)
    # return True 




if __name__ == '__main__':
    run()
