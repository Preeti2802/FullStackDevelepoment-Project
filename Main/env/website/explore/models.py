
from django.db import models

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=255)

    def __str__(self):
        return self.cat_name

class Location(models.Model):
    loc_id = models.AutoField(primary_key=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='locations')
    loc_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.loc_name}, {self.country}"

# class Programs(models.Model):
#     prog_id = models.AutoField(primary_key=True)
#     cat = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='programs')
#     prog_name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.prog_name

class University(models.Model):
    university_id = models.AutoField(primary_key=True)  # New primary key
    university_name = models.CharField(max_length=255)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='universities')
    loc = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='universities')
    #prog = models.ForeignKey(Programs, on_delete=models.CASCADE, related_name='universities')

    def __str__(self):
        return f"{self.university_name} (ID: {self.university_id})"

class FieldOfStudy(models.Model):
    fos_id = models.AutoField(primary_key=True)
    fos_name = models.CharField(max_length=255)
    #prog = models.ForeignKey(Programs, on_delete=models.CASCADE, related_name='fields_of_study')
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='fields_of_study')
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='fields_of_study')

    def __str__(self):
        return self.fos_name
    
class User(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)

