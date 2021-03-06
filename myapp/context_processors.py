# in project/app/context_processors.py
from myapp.models import *

def profile(request):
	profile_picture=""
	profile_name=""
	profile_id = 0
	noti= ""
	list_noti = []
	read = True
	
	try :
		profile = Profile.objects.get(user=request.user)
		profile_picture = profile.profile_picture.url
		try :
			temp = DisabilityInfo.objects.get(profile=profile)
			profile_name = temp.first_name
			profile_id = temp.id

			noti = Notifications.objects.filter(tarket=profile).order_by('-created_at')
			noti = noti[:5]
			
			for i in noti:

			
				temp = {'name': '', 'action': '', 'obj':'','time':None,'img':None,'is_read': False,
				'job_name':"",'job_id':0,'noti_id':0}
				p = Profile.objects.get(user=i.user)
				dis = CompanyInfo.objects.get(profile=p)
				# job = Job.objects.get(company=dis,job=i.job)
				temp['job_name'] = i.job.title_th
				temp['job_id'] = i.job.id
				temp['name'] = dis.th_name
				temp['action'] = i.action
				temp['obj'] = i.obj
				temp['time'] = i.created_at
				temp['is_read'] = i.is_read
				temp['img'] = p.profile_picture.url
				temp['noti_id'] = i.id
				print(temp ,"554555555555555")
				
				if temp['is_read'] == False and read:
					read = False

				list_noti.append(temp)
			
		except :
			# raise

			temp = CompanyInfo.objects.get(profile=profile)	
			profile_name = temp.th_name

			noti = Notifications.objects.filter(tarket=profile).order_by('-created_at')
			noti = noti[:5]
		
			for i in noti:

				temp = {'name': '', 'action': '', 'obj':'','time':None,'img':None,'is_read': False,
				'job_name':"",'job_id':0,'noti_id':0}

				p = Profile.objects.get(user=i.user)
				actor = DisabilityInfo.objects.get(profile=p)
				temp['name'] = actor.first_name
				temp['img'] =  p.profile_picture.url
				temp['action'] = i.action
				temp['obj'] = i.obj
				temp['time'] = i.created_at
				temp['is_read'] = i.is_read
				temp['job_name'] = i.job.title_th
				temp['job_id'] = i.job.id
				temp['noti_id'] = i.id
				if temp['is_read'] == False and read:
					read = False
				list_noti.append(temp)




		


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