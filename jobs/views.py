from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Job, PlanConfiguration
from django.shortcuts import get_list_or_404
from .utilities.miousify_docker_api import create_job_service, delete_job_service


# Create your views here.

def jobs_index(req: HttpRequest):
    #return  HttpResponse("is respondeding perfectly");
    if req.method == "GET":
        # jobs= get_list_or_404(Job);
        return HttpResponse(Job.objects.count());
    if req.method == "POST":
        start_job(req);
        return  HttpResponse("Jobs creation not responding at the moment")
    pass

def start_job(req: HttpRequest):
    miousify_domain_name = req.POST["miousify_domain_name"]
    miousify_store_id = req.POST['miousify_store_resource_id']
    plan = req.POST.get("plan")
    is_trial = req.POST['is_trial']

    service_data = create_job_service(miousify_domain_name=miousify_domain_name,
                                      miousify_store_id=miousify_store_id);

    if service_data is not False:
        # get version and service id for this service

        job = Job(miousify_domain_name=miousify_domain_name, miousify_store_id=miousify_store_id, plan="basic",
                  service_id=service_data['service_id'], is_running=True);
        job.save();

        return HttpResponse("Successfully created job for this store")
        pass
    else:
        # return false
        pass

def job_deactivate(request, miousify_domain_name):

    job= Job.objects.get(pk=miousify_domain_name);

    delete_job_service(job.service_id);

    try:
        return HttpResponse("deleted successfully")
        pass
    except:
        pass
