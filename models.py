import json

class Family(object):
    # make singleton?

    def __init__(self, family_members=None):
        self.family_members = family_members if family_members else load_data()
        find_potential_matches() # self?

    def load_data():
        with open("data_list.json","r") as f:
            try:
                family_list = json.loads(f.read())
            except ValueError:
                print "Improperly formatted json file"
                return None

        return [FamilyMember(**info) for info in family_list if info["participating"]]

    def find_potential_matches(self): 
        names = get_names()
        for fm in self.family_members:
            fm.potential_matches = filter(fm.can_match, names)

    def get_potential_matches(self):
        return {fm.name: fm.potential_matches for fm in family_members}

    def get_names(self):
        return [fm.name for fm in family_members]

    def reset(self):
        for fm in self.family_members:
            fm.last_pollyanna = fm.pollyanna
            fm.pollyanna = ""

        write_data()

    def write_data(self):
        with open("data_list.json", "w+") as f:
            try:
                data = json.dumps(self.family_members) # pretty print json? 
                f.write(data)
            except ValueError:
                print "Could not write json to file"  

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
        return (
            fm.name in potential_matches 
            or (
                self.name != fm.name 
                and self.last_pollyanna != fm.name
                and fm.name not in self.immediate_family
            )
        )


