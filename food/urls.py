from . import views
from django.urls import path 
from django.urls import reverse_lazy

app_name='food'
urlpatterns=[
    path('',views.IndexClassView.as_view(),name='index'),
    path('item/',views.item,name='item'),
    # path('<int:item_id>/',views.detail,name='detail'), function based
    path('<int:pk>/',views.FoodDetail.as_view(),name='detail'), #class based
    path('add/',views.CreateItem.as_view(),name='create_item'),
    path('update/<int:id>/',views.update_item,name='update_item'),
    path('delete/<int:id>',views.delete_item,name='delete_item'),
]