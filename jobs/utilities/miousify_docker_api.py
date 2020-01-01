import docker
from docker.errors import APIError, NotFound, InvalidVersion
import sys
import os
client = docker.from_env()
# client =  docker.from_env();

image_name = "miousify_store_image:0.0.2"
init_command = "npm start"


#         - "traefik.enable=true"
#         - "traefik.http.routers.whoami.rule=Host(`docker.node-1`)"
#         - "traefik.http.routers.whoami.entrypoints=traefik"
#         - "traefik.http.routers.whoami.service=whoami"
#         - "traefik.http.services.whoami.loadbalancer.server.port=80"
#         - "traefik.http.services.whoami.loadbalancer.server.scheme=http"
#         - "traefik.docker.network=traefik-public"
#         - "traefik.docker.lbswarm=false"

# create serivc
def create_job_service(miousify_domain_name, store_id):

    router= "traefik.http.routers." + miousify_domain_name
    service= "traefik.http.services."+miousify_domain_name

    service = client.services.create(image_name,
                           init_command,
                           name=miousify_domain_name,
                           env=["MIOUSIFY_STORE_ID=" + store_id],
                           networks=["traefik-public"],
                           labels={
                               "traefik.enable": "true",
                               router + ".rule": "Host(`" + miousify_domain_name + ".docker.localhost`)",
                               router + ".entrypoints": "traefik",
                               router + ".service":miousify_domain_name,
                               service+".loadbalancer.server.port":"80",
                               service+".loadbalancer.server.scheme":"http",
                               "traefik.docker.network":"traefik-public",
                               "traefik.docker.lbswarm":"false"
                               })

    print("created")
    print(service.version);
    if bool(service.id) is True:
        return {
            "service_id": service.id,
            "service_version_number":service.version
        }

    else:
        return True

# delete service
def delete_job_service(service_name):
    try:
        check= client.services.get(service_name).remove();
        return check
    except APIError as error:
        print(error)


def pause_service(service_name):
    service = client.services.get(service_id=service_name, insert_defaults=False)
    check = service.scale(0)
    return check

def resume(service_name):
    service = None
    try:
        client.services.get(service_id=service_name, insert_defaults=False)
    except NotFound as error:
        print("not found")
        raise error
        pass
    except APIError as error:
        print("error form api")
        raise error
        pass

    check = service.scale(1)
    return check
