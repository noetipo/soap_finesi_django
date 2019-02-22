from django.urls import include, path
from rest_framework import routers
from quickstart import views

from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import path
from rest_framework_simplejwt import views as jwt_views
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'estudiantes', views.EstudianteViewSet)
router.register(r'notas', views.NotasCursoViewSet)
router.register(r'cursos', views.CursoViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('estudiantesApi/', views.EstudianteList.as_view()),
    path('consulta-nota/', views.ConsultaApi.as_view()),
path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]