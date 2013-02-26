LEMP-Ninja
==========

Welcome to LEMP-Ninja, the simplest way to manage your LEMP VM (also the most badass.)
LEMP-Ninja is designed to make it easy to deploy apps and sites on simple [LEMP](http://library.linode.com/lemp-guides) infrastructure.

Core Concepts
-------------

LEMP-Ninja uses the following modules to achieve this goal:

1. Recipes - Recipes are the highest level of definition for a deployment, you would have a recipe for each type of web app/site you work with, e.g., [Wordpress](http://wordpress.org)
2. Instructions - Recipes are made up of Instructions, they can include filling out config templates, fetching latest versions of base libraries, and symlinking compiled configs.
3. Templates - LEMP-Ninja uses the familiar Jinja2 templating library to define and render config templates, templates can be arbitrarily complex or simple, and the dialog is generated from the template tags you use.
4. Actions - LEMP-Ninja supports a few verbs, based primarily around deploying Wordpress sites, as that is what it was designed for.

This is a sample recipe, it shows a simple Wordpress deployment.

>template wordpress.sql

>template wordpress-http.cfg

>tarextract http://wordpress.org/latest.tar.gz

>template wp-config.cfg wp-config.php



>template wordpress.sql

This line tells LEMP-Ninja to load the mysql template "wordpress.sql", LEMP-Ninja will parse the template, locate all tags, then request you for values for each tag.

>template wordpress-http.cfg

Now we do the same for the nginx sites-available config file, values for tags already used will not be requested.

>tarextract http://wordpress.org/latest.tar.gz

Here we curl or wget the latest version of Wordpress, into the directory we've set as our root, in the example templates, it's the domain-name sub-folder in the htdocs folder.

>template wp-config.cfg wp-config.php

We render the wp-config, here, overwriting the recently extracted version.


