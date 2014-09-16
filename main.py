import sys
import copy
import json
from datetime import datetime
import random

# email: mccleary.ludachristmas@gmail.com

class FamilyMember(object):
    def __init__(self, name, immediate_family, pollyanna, last_pollyanna, participating, email):
        self.name = name
        self.immediate_family = immediate_family
        self.pollyanna = pollyanna
        self.last_pollyanna = last_pollyanna
        self.participating = participating
        self.email = email

def main():
    attempts = 100
    for i in xrange(attempts):
        family_list = load_data()
        create_pollyanna(family_list)
        if all_matched(family_list):
            print "Completed on attempt: {n}\n{line}".format(n=i+1, line="-"*20)
            current_year = str(datetime.now().year)
            filename = current_year + ".txt"
            with open(filename, "w") as f:
                f.write("name,pollyanna\n")
                for member in family_list:
                    f.write("{},{}\n".format(member.name, member.pollyanna))
                    print "  {} --> {}".format(member.name, member.pollyanna)
            break
    else:
        print "Could not create the Pollyanna in {} attempts. Check yo data.".format(i+1)

def write_data():
    with open("data.json", "w+"):
        # open and truncate file
        # get family list
        # write objects back to json string
        # write json string to file
        pass

def load_data():
    with open("data.json","r") as f:
        try:
            family_dict = json.loads(f.read())
        except ValueError:
            print "Improperly formatted json file"
            sys.exit(1)

    return [FamilyMember(name,**info) for name, info in family_dict.items() if info["participating"]]

def create_pollyanna(family_list):
    family_list2 = copy.deepcopy(family_list)

    for member in family_list:
        for _ in enumerate(family_list2):
            choice = random.choice(family_list2)
            print "attempting to match:",member.name,"and",choice.name
            if can_match(member, choice):
                member.pollyanna = choice.name
                family_list2.remove(choice)
                break
        else:
            return False

    return True

def can_match(p1, p2):
    return (p1.name != p2.name 
            and p1.last_pollyanna != p2.name
            and p2.name not in p1.immediate_family)

def all_matched(family_list):
    for member in family_list:
        if not member.pollyanna:
            return False
    return True

def reset():
    with open("data.json","r") as f:
        family_members = json.loads(f.read())
        for _, info in family_members:
            info["last_pollyanna"] = info["pollyanna"]
            info["pollyanna"] = ""

def reward():
    # info["pollyanna"] = "Brad McCleary"
    pass

def punish():
    # info["pollyanna"] = "Barbara McCleary"
    pass

if __name__ == '__main__':
    main()
