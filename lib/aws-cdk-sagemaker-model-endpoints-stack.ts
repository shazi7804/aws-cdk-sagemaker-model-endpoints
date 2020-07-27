import * as cdk from '@aws-cdk/core';
import * as ecr from '@aws-cdk/aws-ecr';
import * as sagemaker from '@aws-cdk/aws-sagemaker';
import * as iam from '@aws-cdk/aws-iam';

export interface CdkSagemakerModelEndpointsStackProps extends cdk.StackProps {
  readonly ecrRepository: string;
  readonly modelEndpointName: string;
  readonly modelDataUrl: string;
  readonly modelInstanceType: string;
  readonly modelInstanceCount: number;
  readonly modelInitialVarianWeight: number;
  readonly modelInitialVarianName: string;
}

export class CdkSagemakerModelEndpointsStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props: CdkSagemakerModelEndpointsStackProps) {
    super(scope, id, props);

    // Import from existing ecr repository on current account.
    // e.g. sample of amazon image: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html
    //
    // const ecrRepository = ecr.Repository.fromRepositoryName(this, '<your_own_ECR>', );

    // create execution role for model
    const sagemakerExecutionRole = new iam.Role(this, 'demoSagemakerExecutionRole', {
      roleName: 'demoSageMakerExecutionRole',
      assumedBy: new iam.ServicePrincipal('sagemaker.amazonaws.com')
    });
    sagemakerExecutionRole.addManagedPolicy(iam.ManagedPolicy.fromAwsManagedPolicyName('AWSCodeCommitFullAccess'));
    sagemakerExecutionRole.addManagedPolicy(iam.ManagedPolicy.fromAwsManagedPolicyName('AmazonEC2ContainerRegistryFullAccess'));
    sagemakerExecutionRole.addManagedPolicy(iam.ManagedPolicy.fromAwsManagedPolicyName('AmazonEC2ContainerServiceFullAccess'));
    sagemakerExecutionRole.addManagedPolicy(iam.ManagedPolicy.fromAwsManagedPolicyName('AmazonS3FullAccess'));
    sagemakerExecutionRole.addManagedPolicy(iam.ManagedPolicy.fromAwsManagedPolicyName('AmazonTextractFullAccess'));
    sagemakerExecutionRole.addManagedPolicy(iam.ManagedPolicy.fromAwsManagedPolicyName('AmazonSageMakerFullAccess'));

    // create model
    const modelName = 'demoModel';
    const model = new sagemaker.CfnModel(this, 'demoModelResource', {
      executionRoleArn: sagemakerExecutionRole.roleArn,
      modelName: modelName,
      primaryContainer: {
        // e.g. 811284229777.dkr.ecr.us-east-1.amazonaws.com/blazingtext:latest
        // image: ecrRepository.repositoryUri,
        image: props.ecrRepository,
        // e.g. s3://bucketname/model.tar.gz
        modelDataUrl: props.modelDataUrl
      }
    });

    // create endpoint config
    const endpointConfigName = 'demoEndpointConfig';
    const endpointConfig = new sagemaker.CfnEndpointConfig(this, 'demoEndpointConfigResource', {
      endpointConfigName: endpointConfigName,
      productionVariants: [{
        initialInstanceCount: props.modelInstanceCount,
        initialVariantWeight: props.modelInitialVarianWeight,
        instanceType: props.modelInstanceType,
        modelName: modelName,
        variantName: props.modelInitialVarianName
      }]
    });
    // wait model to complete
    endpointConfig.addDependsOn(model);

    // deploy endpoint, and write endpoint to lambda
    const endpoint = new sagemaker.CfnEndpoint(this, 'demoEndpointResource', {
      endpointConfigName: endpointConfigName,
      endpointName: props.modelEndpointName
    });
    // wait config
    endpoint.addDependsOn(endpointConfig);

  }
}
