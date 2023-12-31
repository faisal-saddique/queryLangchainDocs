AWS Step Functions Toolkit
==========================

**AWS Step Functions** are a visual workflow service that helps developers use AWS services to build distributed applications, automate processes, orchestrate microservices, and create data and machine learning (ML) pipelines.

By including a `AWSSfn` tool in the list of tools provided to an Agent, you can grant your Agent the ability to invoke async workflows running in your AWS Cloud.

When an Agent uses the `AWSSfn` tool, it will provide an argument of type `string` which will in turn be passed into one of the supported actions this tool supports. The supported actions are: `StartExecution`, `DescribeExecution`, and `SendTaskSuccess`.

Setup[](#setup "Direct link to Setup")
---------------------------------------

You'll need to install the Node AWS Step Functions SDK:

*   npm
*   Yarn
*   pnpm

    npm install @aws-sdk/client-sfn

    yarn add @aws-sdk/client-sfn

    pnpm add @aws-sdk/client-sfn

Usage[](#usage "Direct link to Usage")
---------------------------------------

### Note about credentials:[](#note-about-credentials "Direct link to Note about credentials:")

*   If you have not run [`aws configure`](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) via the AWS CLI, the `region`, `accessKeyId`, and `secretAccessKey` must be provided to the AWSSfn constructor.
*   The IAM role corresponding to those credentials must have permission to invoke the Step Function.

    import { OpenAI } from "langchain/llms/openai";import {  createAWSSfnAgent,  AWSSfnToolkit,} from "langchain/agents/toolkits/aws_sfn";const _EXAMPLE_STATE_MACHINE_ASL = `{  "Comment": "A simple example of the Amazon States Language to define a state machine for new client onboarding.",  "StartAt": "OnboardNewClient",  "States": {    "OnboardNewClient": {      "Type": "Pass",      "Result": "Client onboarded!",      "End": true    }  }}`;/** * This example uses a deployed AWS Step Function state machine with the above Amazon State Language (ASL) definition. * You can test by provisioning a state machine using the above ASL within your AWS environment, or you can use a tool like LocalStack * to mock AWS services locally. See https://localstack.cloud/ for more information. */export const run = async () => {  const model = new OpenAI({ temperature: 0 });  const toolkit = new AWSSfnToolkit({    name: "onboard-new-client-workflow",    description:      "Onboard new client workflow. Can also be used to get status of any excuting workflow or state machine.",    stateMachineArn:      "arn:aws:states:us-east-1:1234567890:stateMachine:my-state-machine", // Update with your state machine ARN accordingly    region: "<your Sfn's region>",    accessKeyId: "<your access key id>",    secretAccessKey: "<your secret access key>",  });  const executor = createAWSSfnAgent(model, toolkit);  const input = `Onboard john doe (john@example.com) as a new client.`;  console.log(`Executing with input "${input}"...`);  const result = await executor.call({ input });  console.log(`Got output ${result.output}`);  console.log(    `Got intermediate steps ${JSON.stringify(      result.intermediateSteps,      null,      2    )}`  );};

#### API Reference:

*   [OpenAI](/docs/api/llms_openai/classes/OpenAI) from `langchain/llms/openai`
*   [createAWSSfnAgent](/docs/api/agents_toolkits_aws_sfn/functions/createAWSSfnAgent) from `langchain/agents/toolkits/aws_sfn`
*   [AWSSfnToolkit](/docs/api/agents_toolkits_aws_sfn/classes/AWSSfnToolkit) from `langchain/agents/toolkits/aws_sfn`