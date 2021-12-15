from django.urls import path
from .views import BackgroundView,Back_Photos,Back_Photos2,BackgroundCreateView

urlpatterns = [
	path('photos',Back_Photos, name='back_photos'),
	path('photos2',Back_Photos2, name='bphotos'),
	path('add_background/<int:pk>',BackgroundView.as_view(), name='backgrounds'),
	path('create_bg',BackgroundCreateView.as_view(), name='create_bg'),

    ]