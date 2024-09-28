from django.urls import path
from .views import (
    UserSignupView,
    UserLoginView,
    AddItem,
    ItemDetailView,
    ItemUpdateView,
    ItemDeleteView,
)

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('add_item/', AddItem.as_view(), name='add-item'),
    path('items/<int:item_id>/', ItemDetailView.as_view(), name='item-detail'),
    path('update_items/<int:item_id>/', ItemUpdateView.as_view(), name='item-update'),
    path('delete/<int:item_id>/', ItemDeleteView.as_view(), name='item-delete'),
]
