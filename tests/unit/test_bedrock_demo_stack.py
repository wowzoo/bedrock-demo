import aws_cdk as core
import aws_cdk.assertions as assertions

from bedrock_demo.bedrock_demo_stack import BedrockDemoStack

# example tests. To run these tests, uncomment this file along with the example
# resource in bedrock_demo/bedrock_demo_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = BedrockDemoStack(app, "bedrock-demo")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
