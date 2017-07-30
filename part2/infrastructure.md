# Infrastructure

To run a Flask app on a server you will need SSH access. Ideally you will be using some sort of linux instance such as Ubuntu, CentOS, RedHat, Fedora etc. AWS offers all of these. The simplest way to run your app requires only one server. For this series that's all we will be working with.

To follow along here I recommend you have an Ubuntu 16.x server and an RSA key pair that allows you to SSH into the instance. If you're on a \*nix machine that's all you need. If you're on a Windows machine you'll need to download and install PuTTY. PuTTY is a well known way to control a linux machine from a windows machine.

AWS (and I assume Google Cloud, Azure etc.) makes it very easy to spin up a server. They have tutorials on how to do it so I won't mention that here. One option that is not so obvious to describe your infrastructure as code and have the cloud provider spin up the instances you describe. This way you can write a short script to spin up a single instance or a long script to build VPCs, subnets, Internet access gateways etc. It may take a little longer to do at first, but you write once, use many times.

I recommend two tools here for this

* CloudFormation
* Terraform

CloudFormation is a tool provided by AWS that allows you to describe your infrastructure in JSON or YAML. I prefer YAML because writing it requires zero curly braces and it is easier to read. CloudFormation also comes with a visualization tool on the AWS platform. Using this you can get a marketing grade graphic that allows you to see what you've described. However, updates to your environment are a bit opaque, meaning, you can't ask CloudFormation to tell you what it's going to do before it does it.

## CloudFormation Example

    Description: >-
      This will build a single EC2 instance and an acompanying
      security group. The Parameter KeyName needs to be entered
      on the AWS CLI and must already exist. Creating the key in
      this file would add too much IAM code to make it a useful
      simple example.

    Parameters:
      KeyName:
        Description: Name of an existing EC2 KeyPair
        Type: 'AWS::EC2::KeyPair::KeyName'
        ConstraintDescription: must be the name of an existing EC2 KeyPair.

    Resources:
      Webserver:
        Type: 'AWS::EC2::Instance'
        Properties:
          ImageId: ami-12345678
          InstanceType: t2.micro
          SecurityGroupIds:
            - !Ref WebserverSG
          KeyName: !Ref KeyName
          Tags:
            - Key: Name
              Value: webserver_1
      WebserverSG:
        Type: 'AWS::EC2::SecurityGroup'
        Properties:
          GroupName: WebserverSG
          GroupDescription: Allows web traffic
          SecurityGroupIngress:
            -
              CidrIp: 0.0.0.0/0
              ToPort: 80
              FromPort: 80
              IpProtocol: 'tcp'
            -
              CidrIp: 0.0.0.0/0
              FromPort: 22
              ToPort: 22
              IpProtocol: 'tcp'
          SecurityGroupEgress:
            -
              CidrIp: 0.0.0.0/0
              ToPort: 80
              FromPort: 80
              IpProtocol: 'tcp'

    Outputs:
      WebserverIpAddress:
        Description: Ip address of the webserver
        Value: !GetAtt Webserver.PublicIp

Terraform is a tool written by HashiCorp. It aims to be platform agnostic, which allows you to use the same syntax to describe infrastructure on AWS, Google Cloud etc. This one is very easy to use and has some nice features like, letting you see the effects of changes you've made to your code, before you apply them to your live environment. However, it does not provide a nice visualization tool like CloudFormation. And if you use vim, you will get better autoindent with file extension .go instead of the required .tf.

You'll notice in the example below that terraform has `count` parameter. CloudFormation does not have something like that at the time of writing. And it is actually quite useful. I've been able to write a multipurpose terraform file that creates instances of varying AMIs with a single resource block. You'll also notice some `"${resource.variable}"` clauses in there. Those are quite useful and there are a lot of them.

## Terraform Example

    ################################### Provider
    provider "aws" {
      shared_credentials_file = "/path/to/creds.csv"
      region = "us-west-2"
    }

    ################################### Variables
    variable "key" {
      type = "string"
      default = "default-key"
    }

    ################################### Servers
    resource "aws_instance" "server" {
      count = 1
      ami = "ami-12345678"
      instance_type = "t2.micro"
      key_name = "${var.key}"
      vpc_security_group_ids = ["${aws_security_group.webserver-sg.id}"]
      tags {
        Name = "terraform-example-${count.index}"
    }

    ################################### Security Group
    resource "aws_security_group" "webserver-sg" {
      name = "webserver-sg"
      description = "Allow all inbound traffic"
      ingress {
        from_port = 22
        to_port = 22
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
      }
      ingress {
        from_port = 80
        to_port = 80
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
      }
      egress {
        from_port = 0
        to_port = 0
        protocol = "-1"
        cidr_blocks = ["0.0.0.0/0"]
      }
      tags {
        Name = "terraform-example"
      }
    }

    ################################### Outputs
    output "server_public_dns" {
      value = "${zipmap(aws_instance.server.*.tags.Name, aws_instance.server.*.public_dns)}"
    }
