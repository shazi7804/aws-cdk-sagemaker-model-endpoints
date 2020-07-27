# AWS CDK SageMaker Model Endpoint Deployment

This repository is create SageMaker model and invoke endpoint.

## Requirements

- Training Model

## Change your own

- Change model data url, ecr repo and more.

```
# cdk.context.json
{
    "ecr_blazing_text_reponame": "<your_ecr_repo>",
    "model_data_url": "<your_model_path>"
}
```

## Deploy Stack

```
cdk diff
cdk deploy
```

## Deploy with different AWS_PROFILE

```
cdk --profile another diff
```

## Deploy into a different AWS region

```
AWS_REGION=us-west-1 cdk diff
```

## Author

@shazi7804