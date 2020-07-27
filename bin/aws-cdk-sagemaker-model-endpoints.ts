#!/usr/bin/env node
import * as cdk from '@aws-cdk/core';
import { CdkSagemakerModelEndpointsStack } from '../lib/aws-cdk-sagemaker-model-endpoints-stack';

const app = new cdk.App();
new CdkSagemakerModelEndpointsStack(app, 'CdkSagemakerModelEndpointsStack', {
    ecrRepository: app.node.tryGetContext('ecr_blazing_text_reponame'),
    modelEndpointName: app.node.tryGetContext('model_endpoint_name'),
    modelDataUrl: app.node.tryGetContext('model_data_url'),
    modelInstanceType: app.node.tryGetContext('model_instance_type'),
    modelInstanceCount: app.node.tryGetContext('model_instance_count'),
    modelInitialVarianWeight: app.node.tryGetContext('model_initial_varian_weight'),
    modelInitialVarianName: app.node.tryGetContext('model_initial_varian_name')
});
