from django.urls import path
from .views import CreateMarqueeView,UpdateMarqueeView,Scroll

urlpatterns = [
	path('marquee',Scroll, name='scroll'),
	path('create_marquee',CreateMarqueeView.as_view(),name='create_marquee'),
	path('update_marquee/<int:pk>',UpdateMarqueeView.as_view(),name='update_marquee'),
    ]