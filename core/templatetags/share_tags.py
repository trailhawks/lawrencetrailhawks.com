from django.template import Library
from django.template.loader import render_to_string


register = Library()

NETWORK_TEMPLATES = {
    'email': 'mailto:?subject={text}&body={description}%20{url}',
    'facebook': 'http://www.facebook.com/share.php?u={url}',
    'googleplus': 'https://plusone.google.com/_/+1/confirm?hl=en&url={url}',
    'linkedin': 'http://www.linkedin.com/cws/share?url={url}',
    'myspace': 'http://www.myspace.com/index.cfm?fuseaction=postto&t={text}&c={description}&u={url}',
    'pinterest': 'http://pinterest.com/pin/create/button/?url={url}&description={description}',
    'reddit': 'http://reddit.com/submit?url={url}&text={text}',
    'tumblr': 'http://www.tumblr.com/share?v=3&u={url}',
    'twitter': 'https://twitter.com/intent/tweet?url={url}&text={text}',
}


@register.assignment_tag(takes_context=True)
def render_share_link(context, network, url, text=None, description=None):
    if network in NETWORK_TEMPLATES:
        data = NETWORK_TEMPLATES[network]
        data = data.format(
            network=network,
            url=url,
            text=text or '',
            description=description or '',
        )

        return data

    return ''


@register.assignment_tag(takes_context=True)
def render_share_group(context, url, text=None, description=None):
    data = []
    for network in NETWORK_TEMPLATES:
        cmd = render_share_link(context, network, url, text=text, description=description)
        data.append(cmd)
    return data
