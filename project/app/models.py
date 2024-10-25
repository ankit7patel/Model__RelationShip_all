from django.db import models


# Create your models here.

# class Aadhar(models.Model):
#     aadhar=models.IntegerField(primary_key=True)

#     def __str__(self):
#         return str(self.aadhar)



# class department(models.Model):
#     dep_name=models.CharField(max_length=50)
#     dep_des=models.TextField()

#     def __str__(self):
#         return str(self.dep_name)
    

# class Student(models.Model):
#     Stu_name=models.CharField(max_length=50)
#     stu_email=models.EmailField()
#     Stu_contact=models.IntegerField()
#     aadhar_no=models.OneToOneField(Aadhar,on_delete=models.CASCADE)
#     dep_name=models.ForeignKey(department,on_delete=models.CASCADE)
    
#     # def __str__(self):
#     #     return str.stu_name



class user(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    address=models.CharField(max_length=50)
    def __str__(self):
        return str(self.name)


class profile(models.Model):
    name=models.OneToOneField(user,on_delete=models.CASCADE)
    quli=models.CharField(max_length=50)
    expe=models.IntegerField()
    skills=models.CharField(max_length=50)
    other=models.CharField(max_length=50)
    def __str__(self):
        return str(self.user)
    

