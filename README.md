# How to build a single page site with Flask

This repo contains some code and commentary for building a single page site with Flask. I've made the choice to go with Twitter Bootstrap as the main provider of JavaScript.

Each example adds a feature to the site.

### Part I

* Basic - Hello world example
* Templating - how to render a page in html
* Useful-templating - how to pass variable values to a template
* Styling - How to add CSS
* Javascript - How to add JavaScript
* Forms - Add a safe form using WTForms
* Bootstrap - Use twitter bootstrap to make it look nice
* More templating - Base/child templates, loops, context variable

### Part II

* Infrastructure - How to set up an instance on AWS (pending)
* Python environment - How to set up python and flask (pending)
* Nginx - How to serve the site to the internet (pending)

The idea here is to go down the list in order. The first few items are fairly simple. They just show how to structure a site when you're starting a new project. Pay attention to the `templates` and `static` directories. That's where Flask knows to look for stuff.

The Forms chapter gets a bit more complicated. You'll have to `pip install` the [FlaskWTF][1] module. It also relies on the Flask `secret_key` that is set in the configuration. It is not set by default and the FlaskWTF documentation does not explain it very well. But as long as you include the `app.secret_key = 'some string'` line in your `app.py` file, you'll be fine.

For the bootstrap chapter, you'll need to download bootstrap. The full download will get you a bunch of files, but in these examples I'm only using the min.css and min.js ones. I'm also using the default html from one of the examples on the bootstrap examples page.

[1]: https://flask-wtf.readthedocs.io/en/stable/index.html "FlaskWTF"
