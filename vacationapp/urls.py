from django.urls import path, include
from vacationapp import views
from rest_framework import routers
from .views import AcceptVacationRequestView, RejectVacationRequestView
from .views import EmployeeViewSet, VacationApplicationViewSet
urlpatterns = [
    path('vacation-request/<int:pk>/accept/', AcceptVacationRequestView.as_view(), name='vacation-request-accept'),
    path('vacation-request/<int:pk>/reject/', RejectVacationRequestView.as_view(), name='vacation-request-reject'),

    path('vacationapp/', views.vacation_list),
    path('vacationdetails/<int:pk>/', views.vacation_detail),
]



router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'applications', VacationApplicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
