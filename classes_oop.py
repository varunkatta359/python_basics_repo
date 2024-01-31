class employee:

    def __init__(self,first,last,age,salary):
        self.first = first
        self.last = last
        self.age = age
        self.salary = salary

    def email(self):
        return f'{self.first}{self.last}@email.com'
    
    def fullname(self):
        return f"{self.first} {self.last}"
    
    @classmethod
    def from_string(cls,emp_details):
        first,last,age,salary = emp_details.split('-')
        return cls(first,last,age,salary)
    #in static method we don't need to define the self instance 
    @staticmethod
    def is_holiday(day):
        if day.weekday() == 6 or day.weekday() == 7:
          return True
        else :
          return False
#inheritance
class developer(employee):
    def __init__(self,first,last,age,salary,proglang):
        super().__init__(first,last,age,salary)
        self.proglang = proglang

    

dev_1=developer('varun','kumar',25,'$600','python')
emp_2=employee('sree','lakshmi',40,'$10000')

emp_str_1 = 'krishna-govardhan-125-$1000'

print(dev_1.proglang)
emp_3 = employee.from_string(emp_str_1)

print(employee.fullname(emp_3))
print(emp_3.email())
#functions in classes are calles methods
print(emp_2.fullname())
#this is just an attribute of employee 1

import datetime
my_date= datetime.date(2023,9,10)

print(employee.is_holiday(my_date)) 

