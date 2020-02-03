from flask import render_template, request
from flask_mail import Mail, Message, Attachment
from octopus.core import app

# Flask-Mail version of email service from util.py
def send_mail(to, subject, fro=None, template_name=None, bcc=None, files=None, msg_body=None, **template_params):
    bcc = [] if bcc is None else bcc
    files = [] if files is None else files

    # ensure that email isn't sent if it is disabled
    #if not app.config.get("ENABLE_EMAIL", False):
     #   return

    assert type(to) == list
    assert type(files) == list
    if bcc and not isinstance(bcc, list):
        bcc = [bcc]

    #if app.config.get('CC_ALL_EMAILS_TO', None) is not None:
     #   bcc.append(app.config.get('CC_ALL_EMAILS_TO'))

    # ensure everything is unicode
    unicode_params = {}
    for k, v in template_params.items():
        unicode_params[k] = to_unicode(v)

    # Get the body text from the msg_body parameter (for a contact form),
    # or render from a template.
    # TODO: This could also find and render an HTML template if present
    appcontext = True
    if msg_body:
        plaintext_body = msg_body
    else:
        try:
            plaintext_body = render_template(template_name, **unicode_params)
        except:
            appcontext = False
            with app.test_request_context():
                plaintext_body = render_template(template_name, **unicode_params)

    if fro is None:
        fro = app.config.get("MAIL_FROM_ADDRESS")

    subject = app.config.get("MAIL_SUBJECT_PREFIX", "") + subject

    # create a message
    msg = Message(subject=subject,
                  recipients=to,
                  body=plaintext_body,
                  html=None,
                  sender=fro,
                  cc=None,
                  bcc=bcc,
                  attachments=files,
                  reply_to=None,
                  date=None,
                  charset=None,
                  extra_headers=None
    )

    if appcontext:
        mail = Mail(app)
        mail.send(msg)
    else:
        with app.test_request_context():
            mail = Mail(app)
            mail.send(msg)

def to_unicode(val):
    if isinstance(val, str):
        return val
    elif isinstance(val, str):
        try:
            return val.decode("utf8", "replace")
        except UnicodeDecodeError:
            raise ValueError("Could not decode string")
    else:
        return val

def make_attachment(filename, content_type, data, disposition=None, headers=None):
    """
    Provide a function which can make attachments, insulating the caller from the flask-mail
    underlying implementation.
    :param filename:
    :param content_type:
    :param data:
    :param disposition:
    :param headers:
    :return:
    """
    return Attachment(filename, content_type, data, disposition, headers)