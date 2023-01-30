class person:
    def name(self):
        print('name is...')
class teacher(person):
    def qual(self):
        print('qualification is phd')
class hod(teacher): #class derived from teacher   person->teacher ->hod
    def expe(self):
        print('experience is 22 yrs')
HOD=hod()
HOD.name()
HOD.qual()
HOD.expe()
