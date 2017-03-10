all_skills = []
studied_skills = []
class LearningMap(object):
    def __init__(self):
        pass
    
    def add_skills(self):
        print ("======= Enter the number of skills======")
    
        skills = input("How many skills do you want to add? ")
        for  skills in range(int(skills)):
            self.skill_name = input("Add skill: ")
            all_skills.append(self.skill_name)

    def  view_skills(self):
    	for skill in all_skills:
    		print (skill)
    def add_skill_studied(self):
        print ("====== Kindly add the skills you have studied =========")
        skills = input("How many skills have you studied so far? ")
        for  skills in range(int(skills)):
            self.skill_name = input("Skill name: ")
            studied_skills.append(self.skill_name)
    	
    def view_skills_studied(self):
    	for skill in studied_skills:
    		print (skill)

    def view_skills_not_studied(self):
    	set1 = set(all_skills)
    	set2 = set(studied_skills)
    	list_not_studied = list(set1 - set2)
    	for skills in list_not_studied:
    		print(skills)
    	

    def view_learning_map(self):
    	print ("======" +"View my learningmap "+"======")

    	print ("======" +"This is what I planned to study "+"======")
    	for skills in all_skills:
    		print(skills)
    	print ("=======" +"This what I have studied" +"=======")
    	for skills in studied_skills:
    		print(skills)
    	print ("===================" +"This what I have not yet studied" + "====================")
    	self.view_skills_not_studied()	
