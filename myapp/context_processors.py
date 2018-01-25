# in project/app/context_processors.py
from myapp.models import *

def profile(request):
	profile_picture=""
	profile_name=""
	profile_id = 0
	noti= ""
	list_noti = []
	read = True
	print("do")
	try :
		profile = Profile.objects.get(user=request.user)
		profile_picture = profile.profile_picture.url
		try :
			temp = DisabilityInfo.objects.get(profile=profile)
			profile_name = temp.first_name
			profile_id = temp.id

			noti = Notifications.objects.filter(tarket=profile)
	
			for i in noti:

			
				temp = {'name': '', 'action': '', 'obj':'','time':None,'img':None,'is_read': False,
				'job_name':"",'job_id':0,'noti_id':0}
				print(temp)
				p = Profile.objects.get(user=i.user)
				dis = CompanyInfo.objects.get(profile=p)
				job = Job.objects.get(company=dis)
				temp['job_name'] = job.title_th
				temp['job_id'] = job.id
				temp['name'] = dis.th_name
				temp['action'] = i.action
				temp['obj'] = i.obj
				temp['time'] = i.created_at
				temp['is_read'] = i.is_read
				temp['img'] = i.tarket.profile_picture.url
				temp['noti_id'] = i.id
				if temp['is_read'] == False and read:
					read = False


				print(temp)
				list_noti.append(temp)
			
		except :
			# raise
			temp = CompanyInfo.objects.get(profile=profile)	
			profile_name = temp.th_name
	

		


	except:
		pass
	return {'profile': profile_picture,'name':profile_name,'noti':list_noti,'read':read
	,'id':profile_id} # of course some filter here


# def profile_name(request):
# 	profile_name=""
# 	try :
	
# 		profile_name =  Profile.objects.get(user=request.user).name
# 		print("profile_name",profile_name)
# 	except:
# 		pass
# 	return {'profile_name':profile_name} # of course some filter here	



# def isOwnerShop(request):
# 	profile_name=""
# 	try :
	
# 		store =  StoreByUser.objects.get(user=request.user)
# 		print("profile_name",profile_name)
# 	except StoreByUser.DoesNotExist:
# 		store = None
# 	return {'userstore':store} # of course some filter here		