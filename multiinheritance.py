#multi path inheritance
class student:
    def name(self):
        print("name....")
class academic(student):
    def acad_score(self):
        print('academic score 90% above')
class EEE(student):
    def EEE_score(self):
        print('EEE score----60% and above')
class result(academic,EEE):
    def eligibility(self):
        print('_________eligibility to apply_________')
        self.acad_score()
        self.EEE_score()
r=result()
r.eligibility()
