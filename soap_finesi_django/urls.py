from django.urls import include, path
from rest_framework import routers
from quickstart import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'estudiantes', views.EstudianteViewSet)
router.register(r'pagos', views.PagosViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('estudiantesApi/', views.EstudianteList.as_view()),
    path('consulta-pago/', views.ConsultaApi.as_view()),
]