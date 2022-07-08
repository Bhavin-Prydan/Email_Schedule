from email_schedule.celery import app
from .models import Employee
from datetime import datetime,timedelta
import pytz
from django.utils import timezone
from .utils import Util


@app.task(name='send_Reminder')
def send_Reminder():
	try:
		today = timezone.now().date()
		BirthDay_person = []
		for e in Employee.objects.all():
			if e.BirthDay.day == (today.day)+1 and e.BirthDay.month == today.month:  
				BirthDay_person.append(e)
			if e.BirthDay.day == today.day and e.BirthDay.month == today.month: 
				html_content = '<p>Dear '+ e.Name +',</p>' + '<p> We value your special day just as much as we value you. On your birthday, we send you our warmest and most heartfelt wishes.</p> <br><p> We are thrilled to be able to share this great day with you, and glad to have you as a valuable member of the team. We appreciate everything you’ve done to help us flourish and grow.</p><br><p>Our entire corporate family at Prydan wishes you a very happy birthday and wishes you the best on your special day!</p><p>Regards, <br><b>Prydan</b></p>'
				data = { 'to_email': e.Email,'email_subject': f'Happy Birthday {e.Name}'}
				Util.send_email(data,html_content)
			
		for i in BirthDay_person:	
			person = Employee.objects.exclude(Email=i.Email)
			for p in person:
				html_content = "<p>Dear "+ p.Name +",</p>" + "<p>  Just a gentle reminder to everyone that tommorow is <b>"+ i.Name+" </b>'s birthday, so I require lots of attention, please! Gifts are not necessary (although they are very welcome!), the most important part of his birthday is being able to spend time with as many of you as he can! he can't wait to see everyone later to celebrate!</p><p>Regards, <br><b>Prydan</b></p>"
				data = {'to_email': p.Email,'email_subject': f'Happy Birthday {p.Name}'}
				Util.send_email(data,html_content)	 
					
		# 	start = e.Interview_at - timedelta(seconds=60)
		# 	end =  e.Interview_at
		# 	# current = datetime.utcnow().replace(tzinfo=pytz.UTC)
		# 	current = datetime.now()
			
		# 	if start <= current <= end :
		# 		print(e.Name ,e.Interview_at)

		# 	if e.Interview_at == datetime.now() - timedelta(minutes=1):
	except Exception as e:
		print(e)	


# @app.task(name='send_Reminder')
# def send_Reminder():
# 	try:

# 		emp = Employee.objects.all()

# 		for e in emp:

# 			start = e.Interview_at - timedelta(seconds=60)
# 			end =  e.Interview_at
# 			# current = datetime.utcnow().replace(tzinfo=pytz.UTC)
# 			current = datetime.now()
			
# 			if start <= current <= end :
# 				print(e.Name ,e.Interview_at)

# 		# 	if e.Interview_at == datetime.now() - timedelta(minutes=1):
# 	except Exception as e:
# 		print(e)	
