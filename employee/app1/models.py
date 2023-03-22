from django.db import models
# role, dept, employee

# Create
# Read
# Update
# Delete


class Cars(models.Model):
    car_name = models.CharField(max_length=250, null=False)
    speed = models.IntegerField(default=50)

    def __str__(self):
        return self.car_name


class Department(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=150, null=False)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    hire_date = models.DateField()


    def __str__(self):
        return "%s %s %s" % (self.first_name, self.last_name, self.phone)
