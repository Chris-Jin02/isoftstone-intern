# 小组：01
# 作者：金石
# 创建时间：2023/6/13 17:34
# 文件名：app.py
from django.apps import AppConfig

class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'