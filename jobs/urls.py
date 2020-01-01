from .views import start_job, job_deactivate, jobs_index
from django.urls import path

urlpatterns = [

    path('', jobs_index, name='index'),
    path('run_upgrade/', jobs_index),
    path('<miousify_domain_name>/deactivate', job_deactivate, name='pause-job'),
    # path('<miousify_domain_name>/activate', index, name='start-job'),
    # path('<miousify_domain_name>/pause', index, name='pause-job'),
    # path('<miousify_domain_name>/start', index, name='start-job'),

]
