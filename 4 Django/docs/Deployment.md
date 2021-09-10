

# Deployment

- [Hosting Services](#hosting-services)
  - [Examples](#examples)
  - [SaaS vs PaaS vs IaaS](#saas-vs-paas-vs-iaas)
  - [Domain Names](#domain-names)
  - [DNS](#dns)
  - [HTTPS](#https)
- [Deploying Django](#deploying-django)
  - [Deploying with PythonAnywhere](#deploying-with-pythonanywhere)
  - [Deploying with Heroku](#deploying-with-heroku)
  - [Deploying with AWS](#deploying-with-aws)
  - [Deploying with DigitalOcean](#deploying-with-digitalocean)

## Hosting Services

### Examples

In order to have your web application accessible on the web, you'll have to find a hosting service. Below are some popular hosting services.

- [PythonAnywhere](https://www.pythonanywhere.com/)
- [Heroku](https://devcenter.heroku.com/articles/deploying-python)
- [WebFaction](https://www.webfaction.com/)
- [NearlyFreeSpeech.net](https://www.nearlyfreespeech.net/)
- [Digital Ocean](https://www.digitalocean.com/)
- [Amazon Web Services (AWS)](https://aws.amazon.com/)
- [Microsoft Azure](https://azure.microsoft.com/en-us/)

### SaaS vs PaaS vs IaaS

SaaS, PaaS, and IaaS are three different types of hosting services. [more info](https://www.bmc.com/blogs/saas-vs-paas-vs-iaas-whats-the-difference-and-how-to-choose/)

|    | description | examples |
|--- |---          |---       |
| SaaS | Software as a Service: they provide nearly everything through an interface of their web application | Wordpress, Squarespace |
| PaaS | Platform as a Service:  they provide the software and hardware, you copy files over and configure | PythonAnywhere, NearlyFreeSpeech, Windows Azure, AWS |
| IaaS | Infrastructure as a Service: they provide the hardware, you install software | Digital Ocean, AWS |
| Self-hosted | You manage all the software and hardware |    |



### Domain Names

Most hosting services will give your website a default domain name, but if you want to use a custom domain name, you'll have to rent it from a domain registrar. You can then add a DNS record to associate it with your server's IP address. You can read more about domains on the [MDN](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_domain_name).

- [Google Domains](https://domains.google/)
- [Hover](https://www.hover.com/)
- [GoDaddy](https://www.godaddy.com/)

### DNS

DNS stands for "[Domain Name System](https://en.wikipedia.org/wiki/Domain_Name_System)" and represents a series of servers which associate domain names with IP addresses. When you type a domain name into your browser's address bar and hit 'enter', the browser first queries the DNS to find out which IP address belongs to that domain name. Then it sends the request to that IP address and displays the response on the page. DNS servers can store different types of records.

|Type|Description|Function|
|--- |--- |--- |
|A|Address record|Returns a 32-bit IPv4 address, most commonly used to map hostnames to an IP address of the host.|
|AAAA|IPv6 address record|Returns a 128-bit IPv6 address, most commonly used to map hostnames to an IP address of the host.|
|CNAME|Canonical name record|Alias of one name to another: the DNS lookup will continue by retrying the lookup with the new name.|
|TXT|Text record|Originally for arbitrary human-readable text in a DNS record, it's now often used to verify domain ownership for SSL.|



### HTTPS

To allow your site to use HTTP, you must install an SSL Certificate on your server. SSL certificates can be purchased from a Commercial Certificate Authority, created with Let's Encrypt, or self-signed.


## Deploying Django

First check out the [Django deployment checklist](https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/) and working with [static files](https://docs.djangoproject.com/en/3.2/howto/static-files/deployment/), then consider these additional steps.

- Set up a [virtual environment](../../1%20Python/docs/Virtual%20Environments.md) with a `requirements.txt` to keep track of your libraries.
- Create a `development_settings.py` and a `production_settings.py` to be able to switch configurations and hide your production environment's [SECRET_KEY](https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-SECRET_KEY).

If you want to generate a new secret key you can use the code below:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

If your project uses Django Channels then deployment is [more complicated](https://channels.readthedocs.io/en/latest/deploying.html).

### Deploying with PythonAnywhere

- [Tutorial](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject) ([video](https://www.youtube.com/watch?v=Y4c4ickks2A))
- [Static Files](https://help.pythonanywhere.com/pages/DjangoStaticFiles)
- [Custom Domains](https://help.pythonanywhere.com/pages/CustomDomains/)
- [HTTPS](https://help.pythonanywhere.com/pages/HTTPSSetup/)
- [Help Pages](https://help.pythonanywhere.com/pages/)

It can be difficult to debug on PythonAnywhere because you do not have access to the process running django and thus cannot see the output of `print()`. However, you can print to the error log with the code below, a link to the error log can be found on the web app's page.

```python
import sys
print('check the error log', file=sys.stderr)
```

### Deploying with Heroku

Check out [this tutorial](https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true)

### Deploying with AWS

Check out [this tutorial](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html)

### Deploying with DigitalOcean

Check out [this tutorial](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04)

