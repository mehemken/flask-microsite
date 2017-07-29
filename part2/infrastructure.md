# Infrastructure

To run a Flask app on a server you will need SSH access. Ideally you will be using some sort of linux instance such as Ubuntu, CentOS, RedHat, Fedora etc. AWS offers all of these. The simplest way to run your app requires only one server. For this series that's all we will be working with.

To follow along here I recommend you have an Ubuntu 16.x server and an RSA key pair that allows you to SSH into the instance. If you're on a \*nix machine that's all you need. If you're on a Windows machine you'll need to download and install PuTTY. PuTTY is a well known way to control a linux machine from a windows machine.

AWS (and I assume Google Cloud, Azure etc.) makes it very easy to spin up a server. They have tutorials on how to do it so I won't mention that here. One option that is not so obvious to describe your infrastructure as code and have the cloud provider spin up the instances you describe. This way you can write a short script to spin up a single instance or a long script to build VPCs, subnets, Internet access gateways etc. It may take a little longer to do at first, but you write once, use many times.

I recommend two tools here for this

* CloudFormation
* Terraform

CloudFormation is a tool provided by AWS that allows you to describe your infrastructure in JSON or YAML. I prefer YAML because writing it requires zero curly braces and it is easier to read. CloudFormation also comes with a visualization tool on the AWS platform. Using this you can get a marketing grade graphic that allows you to see what you've described. However, updates to your environment are a bit opaque, meaning, you can't ask CloudFormation to tell you what it's going to do before it does it.

Terraform is a tool written by HashiCorp. It aims to be platform agnostic, which allows you to use the same syntax to describe infrastructure on AWS, Google Cloud etc. This one is very easy to use and has some nice features like, letting you see the effects of changes you've made to your code, before you apply them to your live environment. However, it does not provide a nice visualization tool like CloudFormation.
