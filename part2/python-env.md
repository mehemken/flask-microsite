# Python Environment

I recommend here an Ubuntu 16.04 server because it is the one I'm most familiar with and it is quite simple to use. It comes with Python 3.5.1 by default so if you're running legacy Python you'll have to install it manually. But it's better to start any new projects on Python 3.5 at least. Better to just use Python 3.6.

Then you'll need to install your virtual enviromnent and requirements.txt. As it turns out, in the default Ubuntu 16.04 Amazon AMI, you'll need to install a couple Python things before you get started. Then you can do your standard `venv` however you like. 

    sudo apt-get install python3-pip python3-virtualenv

If you're more accustomed to `conda` environments, you'll need to install Anaconda. If you're using Jupyter notebooks, this is the way to go.

    wget {{ latest.anaconda.download }}
    bash {{ the.download }}
    conda create --name myenv flask flaskWTF

You will also need to upload your code. If you're using git, this has been made very easy with GitHub. For something like $7/month you can have unlimited number of private repos and you can `pull` directly from GitHub.

    git clone https://github.com/user/repo.git

It will ask for your credentials if you're using a private repo.

With any luck you'll just need to run your app with a simple

    python app.py

## Automating this with Ansible

If you're just doing this once, this is all you need. However, if you're going to be updating your code or creating new projects based on what you've already done, you'll want to automate these steps. There are several tools that will allow you to do this such as Chef, Puppet, SaltStack and Ansible to name a few. There are pros and cons to each one and at the enterprise level you'll choose one over the rest based on the particular tech stack already in use.

The one I'll show here is Ansible for a few reasons.

* It is written in Python
* It connects to worker nodes via SSH
* It does not require running extra software on the worker nodes
* Worker nodes require Python (which we already have)

We're working with Python here and in the long run, it might just be best to use Ansible because new modules can be easily written in Python. You can also write new modules in other languages so if you need that, it's also available. The master/control node connects via SSH which comes with Linux. Some other configuration management tools require you to run a daemon program on your worker nodes which consumes CPU and memory. Anisble requires only that there exists some version of Python on the worker node.

If you want to run your Flask app on a Windows server, I'd recommend something else. In my brief experience with Ansible, connecting to a Windows host, although doable, is more clunky than connecting to a Linux host. I would also suggest using something like C# and the IIS webserver in the case of Windows. Also be prepared to pay 2x the AWS bill in the case of Windows.
