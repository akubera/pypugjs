#!/usr/bin/env bash
while true; do
    echo ""
    echo "=== How big is the version bump? ==="
    echo "===================================="
    echo "1 - major"
    echo "2 - minor"
    echo "3 - patch"
    echo ""
    read yn
    case $yn in
        1 ) bumpversion major; break;;
        2 ) bumpversion minor; break;;
        3 ) bumpversion patch; break;;
        * ) echo "Please answer 1-3.";;
    esac
done
