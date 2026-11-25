class student():
    name = input("enter name:")
    age = 14
    schoolclass = 7
    classteacher = "mr.bean"
    
    def show_Details(self):
        print("\nThe Details of the students are: ")
        print('Name: ',self.name)
        print('Age: ',self.age)
        print('Name of teacher: ',self.classteacher)
        print('Class: ', self.schoolclass)
        
    def change_details(self):
        print("\nPLS update your age: ")
        self.age = int(input())
        self.name = input("\nPLS update ur name: ")
        print('\n Details updated')
    
    
#print attributes of class stubent 
print("\n Age of student: ", student.age)
print("\n Name of teacher: ", student.classteacher)

#to call a func of a class, we have to create objects
#creating objects / instances
student1 = student()

#calling func - to get student details
student1.show_Details()

#calling & changing func
student1.change_details()

#to print updated vers
student1.show_Details()