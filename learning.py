from learning_cli import LearningMap




def main():
    while True:
        print("\n\n")
        print("******Welcome to my learning Map\n\n******")
        print(" 1. Add skills\n 2. View all skills\n 3. Add studied Skill \n 4. View Studied Skill\n 5. View skill not studied \n 6. View my learning map\n 7. Exit\n \n")
        action = input('Enter your choice: ')
        learning = LearningMap()
        if action == "1":
            learning.add_skills()
        elif action == "2":
            learning.view_skills()
        elif action == "3":
            learning.add_skill_studied()
        elif action == "4":
            learning.view_skills_studied()
        elif action == "5":
            learning.view_skills_not_studied()
        elif action == "6":
            learning.view_learning_map()
        elif action == "7":
            break
        else:
            print("Invalid choice")
        

if __name__ == '__main__': main()