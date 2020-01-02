
# This file is used to commit the docker image for miousify account

#define variables
owner=miousify
imageName=miousify_tower_service
tag=v0.0.1

docker build . -t $owner/$imageName:$tag

echo "Built successfully"

