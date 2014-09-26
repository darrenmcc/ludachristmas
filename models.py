import json
import copy
import random

class Family(object): # make singleton?

    def __init__(self, naughty=None, nice=None):
        self.family_members = self.load_data()
        if naughty:
            self.naughty_or_nice(name=name, behavior="naughty")
        if nice:
            self.naughty_or_nice(name=name, behavior="nice")
        self.find_potential_matches() 

    def create_pollyanna(self):

        # sort family members by number 
        self.family_members.sort(key=lambda fm: len(fm.potential_matches))

        potential_match_dict = self.get_potential_matches()
        unmatched = []

        for fm in self.family_members:
            print fm.name + ":",potential_match_dict[fm.name]
            if fm.pollyanna:
                # person already has a pollyanna by being naughty or nice, skip them
                continue
            if len(fm.potential_matches) > 0:
                # randomly pick a potential match
                choice = random.choice(potential_match_dict[fm.name])
            else:
                print "FUCK"
                unmatched.append(fm)
                # find a link in the chain that can be broken
                # for fm in self.family_members:
                #   if fm.pollyanna and fm.pollyanna
                
            # assign them that pick
            fm.pollyanna = choice
            print "CHOICE = {}\n".format(choice)

            # remove that person from everyone else's potential matches
            for potential_matches in potential_match_dict.itervalues():
                if choice in potential_matches:
                    potential_matches.remove(choice)

        if self.all_matched():
            print "Completed\n{}".format("-"*9)
            for fm in self.family_members:
                print "  {} --> {}".format(fm.name, fm.pollyanna)
        else:
            print "Pollyanna not created"

    def all_matched(self):
        """Tests if all family members have a pollyanna"""
        return all([fm.pollyanna for fm in self.family_members])

    def load_data(self):
        """Loads family data from file and returns list of FamilyMember objects"""
        with open("data_list.json","r") as f:
            try:
                family_members = json.loads(f.read())
            except ValueError:
                print "Improperly formatted json file"
                return None

        return [FamilyMember(**info) for info in family_members if info["participating"]]


    def find_potential_matches(self): 
        """Finds all potential matches for each FamilyMember and assigns them"""
        for fm in self.family_members:
            fm.potential_matches = filter(fm.can_match, self.family_members)
            # print fm.potential_matches

    def get_potential_matches(self):
        """Returns potential matches as a dictionary in {name: [matches]} form"""
        return {fm.name: [m.name for m in fm.potential_matches] for fm in self.family_members}

    def get_names(self):
        """Returns a list of string names of family members"""
        return [fm.name for fm in self.family_members]

    def reset(self): # read in data first?
        """Resets all current pollyannas and updates previous year's"""
        for fm in self.family_members:
            fm.last_pollyanna = fm.pollyanna
            fm.pollyanna = ""

        self.write_data()

    def write_data(self):
        """Dumps Family data back to json file"""
        with open("data_list.json", "w+") as f:
            try:
                data = json.dumps(self.family_members) # pretty print json? 
                f.write(data)
            except ValueError:
                print "Could not write json to file"  

    def jsonify(self):
        """Returns FamilyMember objects in json form for file writing"""
        return json.dumps([fm.__dict__ for fm in self.family_members])

    def get_fm_by_name(name):
        for fm in self.family_members:
            if fm.name == name:
                return fm

    def naughty_or_nice(name, behavior):
        if behavior == "naughty":
            pollyanna = "Barbara McCleary"
        elif action == "nice":
            pollyanna = "Brad McCleary"

        member = self.get_fm_by_name(name)
        for fm in self.family_members:
            # give the appropriate person this pollyanna
            if fm.name == pollyanna:
                fm.pollyanna = member.name
            # remove this person from all other potential match lists
            if member in fm.potential_matches:
                fm.potential_matches.remove(member)


class FamilyMember(object):
    def __init__(self, name, immediate_family, pollyanna, 
                last_pollyanna, participating, email, 
                potential_matches={}, naughty=False, nice=False):
        self.name = name
        self.immediate_family = immediate_family
        self.pollyanna = pollyanna
        self.last_pollyanna = last_pollyanna
        self.participating = participating
        self.email = email
        self.potential_matches = potential_matches
        self.naughty = naughty
        self.nice = nice
        
    def can_match(self, fm):
        """Tests if this FamilyMember and another can be each other's pollyanna"""
        return (
            self.name != fm.name 
            and self.last_pollyanna != fm.name
            and fm.name not in self.immediate_family
        )



