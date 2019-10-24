from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views

schema_view = get_schema_view(
    openapi.Info(
        title='Music API',
        default_version='v1',
        description='음악 관련 API 서비스입니다.',
    )
)

app_name = 'musics'
# url 순서 주의...
urlpatterns = [
    path('musics/', views.music_list, name='music_list'),
    # 행동은 method 로 
    path('musics/<int:music_pk>/', views.music_detail_and_update_and_delete, name='music_detail_and_update_and_delete'),
    path('musics/<int:music_pk>/comments/', views.comments_create, name='comments_create'),
    path('artists/', views.artist_list, name='artist_list'),
    path('artists/<int:artist_pk>/', views.artist_detail, name='artist_detail'),
    path('comments/', views.comment_list, name='comment_list'),
    path('comments/<int:comment_pk>/', views.comments_update_and_delete, name='comments_update_and_delete'),

    path('docs/', schema_view.with_ui('redoc'), name='api_docs'),
    path('swagger/', schema_view.with_ui('swagger'), name='swagger')
]
