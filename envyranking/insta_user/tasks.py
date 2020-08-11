from time import sleep
from celery import shared_task
from .models import *
from igramscraper.instagram import Instagram
from rank import DenseRank, UpperRank, Rank

#proxies = {
#            'http': 'http://163.172.127.163 :5836',
#            'https': 'http://146.120.168.53:8181',
#                }

instagram = Instagram()
#instagram.set_proxies(proxies)

insta_user_all = insta_user_Data.objects.values('username')
rank_list = insta_user_all.annotate(rank=Rank('number_followers'))

instagram.with_credentials('art2ist', 'ssb9393!!')
instagram.login()    

def update_insta_user_data():
    #instagram = Instagram()
    #insta_user_all = {'username':'art2ist'}
    #insta_user_all = insta_user_Data.objects.values('username')
    #instagram.with_credentials('art2ist', 'ssb9393!!')
    #instagram.login()
    for i in insta_user_all.values():
    #account = instagram.get_account('art2ist')
        account = instagram.get_account(i["username"])
        #id_number = account.identifier
        #username = i["username"]
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
        data = {'username':username,
                #'fullname':fullname, 
               'biograghy':biograghy, 'profilepic_url':profilepic_url, 'external_url':external_url, 
                'number_published':number_published, 'number_followers':number_followers, 'is_private':is_private, 'is_verified':is_verified
        }
        print(data)
        insta_user_Data.objects.filter(username=username).update(**data)
        sleep(2)



while True:
    update_insta_user_data()
    print('updating !! ..')

