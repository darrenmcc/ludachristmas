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
    family_list = load_data()
    Family = Family(family_list)
    create_pollyanna(family_list)

def jsonify(family_list):
    output = {}
    for member in family_list:
        output[member.name: member]


def write_data(family_list):
    with open("data_list.json", "w+") as f:
        try:
            data = json.dumps(family_list) # pretty print json? 
            f.write(data)
        except ValueError:
            print "Could not write json to file"

def create_pollyanna(family_list):

    # new strategy
    # create list of people someone can be matched with, check
    # randomly pick from that list
    # remove that pick from everyone else's list

    potential_match_dict = Family.potential_matches

    for member in Family.family_members:
        choice = random.choice(member.potential_matches)
        member.pollyanna = choice

        for potential_matches in potential_match_dict.itervalues()():
            if choice in potential_matches:
                potential_matches.remove(choice)

    if all_matched(Family.family_members):
        print "Completed on attempt: {n}\n{line}".format(n=i+1, line="-"*20)
        current_year = str(datetime.now().year)
        filename = current_year + ".txt"
        with open(filename, "w") as f:
            # f.write("name,pollyanna\n")
            for member in family_list:
                f.write("{},{}\n".format(member.name, member.pollyanna))
                print "  {} --> {}".format(member.name, member.pollyanna)
    else:
        print "Pollyanna not created"


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


    print "Completed on attempt: {n}\n{line}".format(n=i+1, line="-"*20)
    current_year = str(datetime.now().year)
    filename = current_year + ".txt"
    with open(filename, "w") as f:
        f.write("name,pollyanna\n")
        for member in family_list:
            f.write("{},{}\n".format(member.name, member.pollyanna))
            print "  {} --> {}".format(member.name, member.pollyanna)

    return True 

def all_matched(family_list):
    return all([member.pollyanna for member in family_list])

def reset():
    with open("data.json","r") as f:
        family_members = json.loads(f.read())
        for _, info in family_members:
            info["last_pollyanna"] = info["pollyanna"]
            info["pollyanna"] = ""

def naughty(member):
    member["pollyanna"] = "Brad McCleary"
    # set brad 

def nice(member):
    member["pollyanna"] = "Barbara McCleary"
    # set barbara 

if __name__ == '__main__':
    run()
