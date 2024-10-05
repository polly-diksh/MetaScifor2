from django.db import models

# Create your models here.
class Team(models.Model):
	title = models.CharField(max_length = 100)

	def __str__(self):
		return self.title

# the player form
class Player(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    AGE_CATEGORY_CHOICES = [
        ('boys_under-15', 'Boys under 15'),
        ('boys_under-19', 'Boys under 19'),
        ('men_under-23', 'Men Under 23'),
        ('men_senior', 'Men Senior'),
    ]

    POSITION_CHOICES = [
        ('batsmen', 'Batsmen'),
        ('bowler', 'Bowler'),
        ('wicketkeeper', 'Wicketkeeper'),
        ('all_rounder', 'All Rounder'),
    ]

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    profile = models.ImageField(upload_to="profiles/")
    nationality = models.CharField(max_length=100)
    dateofbirth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    aadhar = models.CharField(max_length=12)
    aadhar_photo = models.ImageField(upload_to="aadhar_photos/")
    emailid = models.EmailField()
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)
    weight = models.DecimalField(max_digits = 5, decimal_places = 2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    guardian_name = models.CharField(max_length=100)
    relation = models.CharField(max_length=100)
    guardiancontact = models.CharField(max_length=15)
    agecategory = models.CharField(max_length=20, choices=AGE_CATEGORY_CHOICES)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    position = models.CharField(max_length=20, choices=POSITION_CHOICES)
    role = models.CharField(max_length=100)
    handiness = models.CharField(max_length=100)
    disease = models.CharField(max_length=100)
    allergies = models.TextField(blank = True, null = True)
    additional_information = models.TextField(blank = True, null = True)


    def __str__(self):
    	return f"{self.firstname} {self.lastname}"



# create form stuff
class Form(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank = True)
    IsDelete = models.BooleanField(default=False)

class Question(models.Model):
    QUESTION_TYPES = [
        ('short_answer', "Short Answer"),
        ('paragraph', "Paragraph"),
        ('multiple_choice', "Multiple Choice"),
        ('checkbox', "Check Boxes"),
        ('dropdown', "Dropdowns"),
        ('file_upload', "File Upload"),
        ('date', "Date"),
        ('time', "Time"),
    ]

    form = models.ForeignKey(Form, related_name = "questions", on_delete=models.SET_NULL, null = True)
    question_text = models.CharField(max_length=255)
    question_type = models.CharField(max_length=100, choices=QUESTION_TYPES)

    def __str__(self):
        return self.question_text

class Multiple_choice(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)

    def __str__(self):
        return self.choice_text

class Response(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Response for {self.form.title}"




