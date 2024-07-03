from django.contrib import admin
from django.urls import re_path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import re_path
from app import views


urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^$index', views.index, name='index'),
    re_path(r'^$', views.Staff, name='Staff'),
    re_path(r'^add_staff$', views.add_staff, name='add_staff'),
    re_path(r'^add_staff_save$', views.add_staff_save, name='add_staff_save'),
    re_path(r'^Customer$', views.Customer, name='Customer'),
    re_path(r'^add_customer$', views.add_customer, name='add_customer'),
    re_path(r'^add_customer_save$', views.add_customer_save, name='add_customer_save'),
    re_path(r'^Deposit$', views.Deposit, name='Deposit'),
    re_path(r'^add_deposit$', views.add_deposit, name='add_deposit'),
    re_path(r'^add_deposit_save$', views.add_deposit_save, name='add_deposit_save'),
    re_path(r'^Loan$', views.Loan, name='Loan'),
    re_path(r'^add_loan$', views.add_loan, name='add_loan'),
    re_path(r'^add_loan_save$', views.add_loan_save, name='add_loan_save'),
    re_path(r'^report$', views.report, name='report'),
    re_path(r'^download/(?P<id>\d+)$', views.download,
        name='download'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)