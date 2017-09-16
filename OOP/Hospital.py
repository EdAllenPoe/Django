class Hospital(object):

    def __init__(self,name,allergies,hospital):
        self.id=0
        self.hospital=hospital
        self.patients=[]
        self.name=name
        self.allergies=allergies
        self.bed=0
        self.capacity=3
        self.status=None

    def admit(self):
        self.id+=1
        self.bed=self.id
        if(len(self.patients)>=self.capacity):
            self.status=False
        else:
            self.patients.append(self.name)
            self.status=True
            return self

    def discharge(self):
        return self

    def display_info(self):
        print "Patient ID:",self.id
        print "Name:",self.name
        if self.status==True:
            print "Admission Status: Admitted"
        else:
            print"Admission Status: Denied"
        for allergy in self.allergies:
            print "Allergic to:",allergy
        print "Bed Number:",self.bed

patient1=Hospital("Mathew",["bad music","polyester shirts","toast"],"hospital on the hill").admit()

print patient1.display_info()
