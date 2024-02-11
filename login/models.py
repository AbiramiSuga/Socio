
from django.db import models


class user(models.Model):
	u_id=models.AutoField(primary_key=True,unique=True)
	u_name=models.CharField(max_length=50)
	u_mailid=models.CharField(max_length=50)
	pswd=models.CharField(max_length=25)
	hobby=models.CharField(max_length=50)
	address=models.CharField(max_length=100)
	profession=models.CharField(max_length=25)
	dob=models.DateField()
	education=models.CharField(max_length=50)
	phone_no=models.CharField(max_length=10)
	pic=models.ImageField(default=None,upload_to="images/")


class chat(models.Model):
	msgsender_id=models.ForeignKey(user,related_name='msge',on_delete=models.CASCADE)
	msgreceiver_id=models.ForeignKey(user,related_name='msgre',on_delete=models.CASCADE)
	message=models.CharField(max_length=500)
	time=models.DateTimeField()

class Req(models.Model):
	reqsender_id=models.ForeignKey(user,related_name='request',on_delete=models.CASCADE)
	reqreceiver_id=models.ForeignKey(user,related_name='requests',on_delete=models.CASCADE)
	req_status=models.IntegerField(default=0)
	time=models.DateTimeField()

