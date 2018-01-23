# in project/app/context_processors.py
from myapp.models import *

def profile(request):
	profile_picture=""
	profile_name=""
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

			noti = Notifications.objects.filter(user=request.user)
			for i in noti:
			
				temp = {'name': '', 'action': '', 'obj':'','time':None,'img':None,'is_read': False}
				print(temp)
				
				dis = CompanyInfo.objects.get(profile=i.tarket)

				temp['name'] = dis.th_name
				temp['action'] = i.action
				temp['obj'] = i.obj
				temp['time'] = i.created_at
				temp['is_read'] = i.is_read
				temp['img'] = i.tarket.profile_picture.url

				if temp['is_read'] == False and read:
					read = False


				print(temp)
				list_noti.append(temp)
			
		except :
			raise
			# temp = CompanyInfo.objects.get(profile=profile)	
			# profile_name = temp.th_name
			# print(profile_name,"5555")

		


	except:
		pass
	return {'profile': profile_picture,'name':profile_name,'noti':list_noti,'read':read} # of course some filter here


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