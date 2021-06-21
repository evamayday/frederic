import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings') # 需對應 wsgi.py
django.setup()
# 更多操作請參考官方文檔: https://docs.djangoproject.com/en/3.1/topics/db/models/
from mysite.models import Post
import json
#=============================================================================#
with open('Post.json', 'r') as read_file:
    post_json = json.load(read_file)

for i, post_dict in enumerate(post_json):
    K_time = post_dict['K_time']
    K_location = post_dict['K_location']
    K_death = post_dict['K_death']
    K_injure = post_dict['K_injure']
    Post.objects.create(K_time=K_time, K_location=K_location, K_death=K_death, K_injure=K_injure)
#=============================================================================#

    