from django.urls import path
from .views import *

urlpatterns = [
	path("", home, name="home"),
	path("add_player/", add_player, name="add_player"),
	path("details/", player_details, name="details"),
	path("player/<int:pk>/", player_detail, name="player_detail"),
	path("create_form/", create_form, name = "create_form"),
	path('add_questions/<int:form_id>', add_questions, name="add_questions"),
	path('list_forms/', list_forms, name="list_forms"),
	path('form_detail/<int:form_id>/', form_detail, name="form_detail"),
	path("delete_form/<int:form_id>/", delete_form, name="delete_form"),
	path('recyclebin/', recycle_data, name="recycle"),
	path("restore/<int:form_id>/", restore_data, name="restore"),
	path("delete/<int:form_id>/", delete_data, name = "delete"),
	

]