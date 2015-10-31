from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('game.views',

#yunwei
   # url(r'^data/$', 'game.game_data', name='game_data'),
    url(r'^install/$', 'game.game_install', name='game_install'),
    url(r'^log/$', 'game.game_read_log_file', name='game_read_log'),
    url(r'^clean/$','game.game_clean_log',name="game_clean_log"),
   # url(r'^test/$','game.form_test',name="form_test"),
    url(r'^jindutiao/$','game.jindutiao',name="jindutiao"),
    url(r'^jindutiao_read/$','game.jindutiao_game_read_log_file',name="read_jindutiao"),
    #url(r'^game_info/$','game.game_info',name="game_info"),
    url(r'^info/en/$','game.game_info',name="game_en"),
    url(r'^info/qq/$','game.game_info',name="game_qq"),
    url(r'^info/android/$','game.game_info',name="game_android"),
)

