class CSE:
    def __init__(self, branch_name):
        self.branch = branch_name
    
    def show_details_main(self):
        print(self.branch)

class ECSE (CSE):
    def __init__(self,branch_name,branch_id):

        CSE.__init__(self,branch_name)

        self.id = branch_id
    def show_details_ECSE(self):
        print(self.id)

class EE (ECSE):
    def __init__ (self,branch_name, branch_id, college):
        ECSE.__init__(self,branch_name, branch_id)
        self.college = college  

    def show_details_EE(self):
        print(self.college)

instance = EE("All Branch",55,"TECHNO COLLEGE")
instance.show_details_main()
instance.show_details_ECSE()
instance.show_details_EE()