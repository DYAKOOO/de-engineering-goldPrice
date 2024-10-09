#!/bin/bash

# Fetch the latest version
LATEST_VERSION=$(gcloud container images list-tags gcr.io/de-goldprice/gold-price-producer --format='get(tags)' --sort-by=~tags | grep '^v1\.0\.' | head -n 1)

# Extract and increment patch version
PATCH_VERSION=$(echo $LATEST_VERSION | cut -d. -f3)
NEW_PATCH_VERSION=$((PATCH_VERSION + 1))
NEW_VERSION="v1.0.$NEW_PATCH_VERSION"

# Build and push the new version
docker build -t gcr.io/de-goldprice/gold-price-producer:$NEW_VERSION -f Dockerfile-producer .
docker push gcr.io/de-goldprice/gold-price-producer:$NEW_VERSION

# Output the new version for use in other scripts
echo $NEW_VERSION