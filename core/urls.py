from django.urls import path
from core import views_auth, views_template,\
    views_invoice, views_cart

urlpatterns = [
    # User
    path('api/whoami', views_auth.whoami),
    path('api/login', views_auth.login),
    path('api/logout', views_auth.logout),

    # Templates
    path('api/templates', views_template.get_templates),
    path('api/template', views_template.template_detail),

    # Cart
    path('api/item_cart', views_cart.item_to_cart),

    # Invoice
    path('api/create_invoice', views_invoice.crate_invoice_order),
]
