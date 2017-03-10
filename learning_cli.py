class LearningMap(object):
	all_skills = []
	studied_skills = []

	def __init__(self):
		pass
		

    def add_skills(self, skill_name):
    	print ("======= Enter the number of skills======")
    	skills = input("How many skills do want to add?")
    	for  skills in range(int(skills)):
    		self.skill_name = input("Add skill")
    		all_skills.append(self.skill_name)
    def  view_skills(self):
    	for skill in all_skills:
    		print "The list of all skills added are: %s" %(skill)
    def add_skill_studied(self, skill_name):
    	print "====== Kindly add the skills you have studied ========="
    	self.skill_name = input("Skill name")
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
    	print ("====================" +View my learningmap +"====================")

    	print ("====================" +This iss what I planned to study +"====================")
    	for skills in all_skills:
    		print(skills)
    	print ("====================" +This what I have studied +"====================")
    	for skills in studied_skills:
    		print(skills)
    	print ("====================" +This what I have notyet studied + "====================")
    	view_skills_not_studied()	
