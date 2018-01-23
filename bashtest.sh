#!/bin/bash

BRANCH=$1
SHA1=$2
AWS_ACCOUNT_ID=$3

if [ -z $BRANCH ]
then
    if branch=$(git symbolic-ref --short -q HEAD)
    then
        BRANCH=$branch
    else
        echo "\$BRANCH is empty"
        exit 1
    fi
fi

if [ -z $SHA1 ]
then
    if sha1=$(git rev-parse HEAD)
    then
        SHA1=$sha1
    else
        echo "\$SHA1 is empty"
        exit 1
    fi
fi

if [ -z $AWS_ACCOUNT_ID ]
then
    AWS_ACCOUNT_ID=$(aws sts get-caller-identity --output text --query 'Account')
    if [ -z $AWS_ACCOUNT_ID ]
    then
        echo "\$AWS_ACCOUNT_ID is empty"
        exit 1
    fi
fi

echo BRANCH: $BRANCH
echo SHA1: $SHA1
echo ACCOUNT_ID: $AWS_ACCOUNT_ID