import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings') # 需對應 wsgi.py
django.setup()
# 更多操作請參考官方文檔: https://docs.djangoproject.com/en/3.1/topics/db/models/
from mysite.models import Post
import json
from django.core.serializers.json import DjangoJSONEncoder
#=============================================================================#
posts = Post.objects.all()
post_dict_list = []
for post in posts:
    post_dict = {}
    post_dict['K_time'] = post.K_time
    post_dict['K_location'] = post.K_location
    post_dict['K_death'] = post.K_death
    post_dict['K_injure'] = post.K_injure
    post_dict_list.append(post_dict)
post_json = json.dumps(post_dict_list, cls=DjangoJSONEncoder)
print(f'{post_dict_list}\n')
print(f'{post_json}\n')

with open('Post.json', 'w') as fp:
    fp.write(post_json)


