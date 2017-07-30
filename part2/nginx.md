# Nginx

Nginx is a webserver program that stands between your Flask app and the general public. It is free and open source and written in C. It is lightweight and very fast. Faster than the wsgi server that delivers your Flask app. It is widely used as a load balancer and reverse proxy.

It is quite simple to use. Once you've installed it, you can control it using some configuration files in the `/etc/nginx` directory. There are quite a few files in that directory but to get started you only need to pay attention to one.

    /etc/nginx/
    ├── nginx.conf
    ├── sites-available
    │   └── default
    └── sites-enabled
        └── default

The file we really need to pay attention to is the `default` server block in the `sites-available` directory. That is the file that controls the default webserver when nginx is initially installed. Normally we would point it at something like `/var/www/html` where we would keep static html files that make up a website. We will point it instead to the localhost port that is displaying the Flask app.

    # file: /etc/nginx/sites-available/default

    server {
        listen 80 default_server;
        server_name _;

        location {
            proxy_pass http://localhost:5000/;
        }
    }

With that, all we do is test that nginx likes the new configuration and then reload the server.

    sudo nginx -t
    sudo nginx -s reload

Now if we go to the DNS of the instance, we should see our site.

