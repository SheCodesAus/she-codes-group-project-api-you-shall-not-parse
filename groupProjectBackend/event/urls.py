from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('events/', views.EventList.as_view()),
    path('events/<int:pk>/', views.EventDetailApi.as_view()),
    path('modules/', views.ModuleList.as_view()),
    path('roles/', views.RoleList.as_view()),
    path('event_modules/', views.EventModuleList.as_view()),
    path('event_modules/<int:pk>/populate', views.event_module_populate),
    path('event_module_roles/', views.EventModuleRoleList.as_view()),
    path('event_module_roles/<int:pk>/', views.EventModuleRoleDetailApi.as_view()),
    path('filter_event_modules/<int:event_pk>/', views.FilteredEventModule.as_view()),
    path('filter_event_module_roles/<int:event_module_pk>/', views.FilteredEventModuleRole.as_view()),
    path('filter_event_module_roles/<int:event_module_pk>/<int:role_pk>/', views.ChooseEventModuleRole.as_view()),
    path('filter_event_module_roles_user/<int:mentor_pk>/', views.FilteredEventModuleRoleUser.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)