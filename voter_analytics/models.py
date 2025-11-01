#File: models.py
#Author: Nathan Moges (bmoges18@bu.edu) 10/3/25
#Description: The model.py creates the model that we need to create our app


from django.db import models

# Create your models here.
class Voter(models.Model):

    last_name = models.TextField()
    first_name = models.TextField()
    street_number = models.TextField()
    street_name = models.TextField()
    apt_number = models.TextField()
    zip_code = models.CharField(max_length=5, blank=True)
    dob = models.TextField()
    date_of_registration = models.TextField()
    party_affilitation =  models.CharField(max_length=2, blank=True)
    precinct_number = models.CharField(max_length=3, blank=True)
    v20state = models.BooleanField(default=False)
    v21town = models.BooleanField(default=False)
    v21primary = models.BooleanField(default=False)
    v22general = models.BooleanField(default=False)
    v23town = models.BooleanField(default=False)
    voter_score = models.IntegerField()

    def load_data():
        '''Function to load data records from CSV file into the Django database.'''
        Voter.objects.all().delete()
        filename = '/Users/nathanmoges/Downloads/newton_voters.csv'
        f = open(filename, 'r')
        f.readline()
        for line in f:
            fields = line.split(',')
        
            try:
                votes = Voter(last_name=fields[1],
                                first_name=fields[2],
                                street_number=fields[3],
                                street_name = fields[4],
                                apt_number = fields[5],
                                zip_code = fields[6],
                                
                                dob = fields[7],
                                date_of_registration = fields[8],
                                precinct_number = fields[9],
    
                                party_affilitation = fields[10],
                                v20state = fields[11].strip().upper() == 'TRUE',
                                v21town = fields[12].strip().upper() == 'TRUE',
                        
                                v21primary = fields[13].strip().upper() == 'TRUE',
                                v22general = fields[14].strip().upper() == 'TRUE',
                                v23town = fields[15].strip().upper() == 'TRUE',
                                voter_score = fields[16].strip().upper() == 'TRUE',
                            )
            
    
    
                votes.save() # commit to database
                print(f'Created result: {votes}')
                
            except:
                print("Something went wrong!")
                print(f"line={line}")


