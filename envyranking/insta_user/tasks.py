from time import sleep
from celery import shared_task
#from celery.schedules import crontab
#from celery.task import periodic_task
from .models import *
from igramscraper.instagram import Instagram

proxies = {
            'http': 'http://196.54.50.169',
            'http': 'http://54.38.218.212:6582',
                }

instagram = Instagram()
instagram.set_proxies(proxies)

insta_user_all = insta_user_Data.objects.values('username').order_by('-number_followers')

#instagram.with_credentials('art2ist', 'ssb9393!!')
#instagram.login()    

@shared_task
#@periodic_task(run_every=crontab(hour=13, minute=05))
def update_insta_user_data():
    number = 1
    for i in insta_user_all.values():
    #account = instagram.get_account('art2ist')
        account = instagram.get_account(i["username"])
        #id_number = account.identifier
        username = i["username"]
        fullname = account.full_name
        biograghy = account.biography
        profilepic_url = account.get_profile_picture_url()
        external_url = account.external_url
        number_published = account.media_count
        number_followers = account.followed_by_count
        number_follows = account.follows_count
        is_private = account.is_private
        is_verified = account.is_verified
        print('updating insta user data ..')
        data = {
                'rank':number,
                #'username':username,
                'fullname':fullname, 
               'biograghy':biograghy, 'profilepic_url':profilepic_url, 'external_url':external_url, 
                'number_published':number_published, 'number_followers':number_followers, 'is_private':is_private, 'is_verified':is_verified
        }
        print(data)
        insta_user_Data.objects.filter(username=username).update(**data)
        number +=1
        sleep(30)
        


while True:
    try:
        update_insta_user_data()
        print('updating !! ..')
        sleep(1800)
    except :
        sleep(3600)
        continue
    break
