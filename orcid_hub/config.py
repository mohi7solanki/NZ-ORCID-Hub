# -*- coding: utf-8 -*-
"""Application configuration."""

from os import environ, urandom

ENV = environ.get("ENV", "dev")

ORCID_API_BASE = "https://api.sandbox.orcid.org/v2.0/" if ENV != "prod" else "https://api.orcid.org/v2.0/"
ORCID_BASE_URL = "https://sandbox.orcid.org/" if ENV != "prod" else "https://orcid.org/"

SECRET_KEY = environ.get("SECRET_KEY", urandom(42).hex())
SALT = "secret-salt" if ENV.startswith("dev") else (environ.get("TOKEN_PASSWORD_SALT")
                                                    or urandom(5).hex())

# NZ ORCIDHUB API client ID and secret
ORCID_CLIENT_ID = environ.get("ORCID_CLIENT_ID", "APP-42W3G8FS4OHGM562")
ORCID_CLIENT_SECRET = environ.get("ORCID_CLIENT_SECRET")

# Change the URL as per the enviornment
AUTHORIZATION_BASE_URL = 'https://sandbox.orcid.org/oauth/authorize' \
    if ENV != "prod" else "https://orcid.org/oauth/authorize"
TOKEN_URL = 'https://sandbox.orcid.org/oauth/token' if ENV != "prod" else "https://orcid.org/oauth/token"
# TODO: technically it shouldn't be part of configuration.
# TODO: These constans need to be oved to orcid_client.
SCOPE_ACTIVITIES_UPDATE = ['/activities/update']
SCOPE_READ_LIMITED = ['/read-limited']
SCOPE_AUTHENTICATE = ['/authenticate']

# Database connection url
DATABASE_URL = environ.get("DATABASE_URL")
BACKUP_DATABASE_URL = environ.get("BACKUP_DATABASE_URL")

if not DATABASE_URL:
    POSTGRES_PASSWORD = environ.get("POSTGRES_PASSWORD") or environ.get("PGPASSWORD") or "p455w0rd"
    DB_NAME = environ.get("PGDATABASE", "orcidhub")
    DB_USERNAME = environ.get("PGUSER", "orcidhub")
    DB_PASSWORD = POSTGRES_PASSWORD
    DB_HOSTNAME = environ.get("PGHOST", "db")
    DATABASE_URL = "postgresql://" + DB_NAME
    if POSTGRES_PASSWORD:
        DATABASE_URL += ':' + POSTGRES_PASSWORD
    DATABASE_URL += "@" + DB_HOSTNAME + ":5432/" + DB_NAME

# NB! Disable in production
if ENV in ("dev0", ):
    DEBUG = '1'
    MAIL_DEBUG = '1'
    TESTING = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    DEBUG_TB_PROFILER_ENABLED = True
    OAUTHLIB_INSECURE_TRANSPORT = '1'
    environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    TEMPLATES_AUTO_RELOAD = True
    # EXPLAIN_TEMPLATE_LOADING = True

OAUTH2_PROVIDER_TOKEN_EXPIRES_IN = 86400  # Default Bearer token expires time, default is 3600.

# add mail server config
MAIL_PORT = int(environ.get("MAIL_PORT", 25))
MAIL_SUPPRESS_SEND = False
MAIL_DEFAULT_SENDER = environ.get("MAIL_DEFAULT_SENDER", "no-reply@orcidhub.org.nz")
MAIL_SERVER = environ.get("MAIL_SERVER", "gateway")

MEMBER_API_FORM_BASE_URL = "https://orcid.org/content/register-client-application-sandbox" \
    if ENV != "prod" else "https://orcid.org/content/register-client-application-production-trusted-party"

NOTE_ORCID = 'An NZ ORCID Hub integration for'
CRED_TYPE_PREMIUM = 2
APP_NAME = 'NZ ORCID HUB'
APP_DESCRIPTION = 'This is an ORCID integration through the NZ ORCID HUB connecting'
APP_URL = "https://" + (ENV + ".orcidhub.org.nz" if ENV != "prod" else "orcidhub.org.nz")

# External Shibboleth SP login URL (e.g., https://test.orcidhub.org.nz/Tuakiri/login)
EXTERNAL_SP = environ.get("EXTERNAL_SP") if ENV != "prod" else None

DEFAULT_COUNTRY = "NZ"

if ENV == "dev":
    GA_TRACKING_ID = "UA-99022483-1"
elif ENV == "test":
    GA_TRACKING_ID = "UA-99022483-2"
elif ENV == "dev0":
    GA_TRACKING_ID = "UA-99022483-3"
else:
    GA_TRACKING_ID = "UA-99022483-4"

DEFAULT_EMAIL_TEMPLATE = """<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Affiliation Process Update</title>
    <meta name="keywords" content="ORCID HUB,New Zealand,NZ,orcid"/>
  </head>
  <body>
    <div style="font-family: Arial, Verdana, Georgia, and Times New Roman; background-color: white; color: black;">
      <table style="vertical-align: middle; background-color: black; color: white; width: 100%;">
        <tr>
          <td>&nbsp;</td>
          <td align="right">
            <img src="{LOGO}" title="NZ ORCID Hub" alt="NZ ORCID Hub" style="display:block;" />
          </td>
        </tr>
      </table>
      {MESSAGE}
      <p>If you received this email in error, or you have questions about the responsibilities involved, please contact: <a href="mailto:orcid@royalsociety.org.nz">orcid@royalsociety.org.nz</a></p>
      <hr>
      <p>This email was sent to <a href="mailto:{EMAIL}>{EMAIL}</a></p>
      <!--  Footer Details -->
      <table style="vertical-align: top; background-color: black; color: white; width: 100%; margin-top: 25px;">
        <tr>
          <td>
            <p style="vertical-align: top; padding-left: 15px;">
            Contact details for the NZ ORCID Hub<br>
            Phone: (04) 472 7421<br>
            PO Box 598, Wellington 6140<br>
            <b><a style="text-decoration: none; color: white;"
                  href="mailto:orcid@royalsociety.org.nz">orcid@royalsociety.org.nz</a></b>
            </p>
          </td>
          <td style="vertical-align: top;">
            <p class="copyright"><a href="https://creativecommons.org/licenses/by/4.0/" target="_blank"><img
            src="{BASE_URL}/static/images/CC-BY-icon-80x15.png" alt="CC-BY"/></a></p>
          </td>
        </tr>
      </table>
    </div>
  </body>
</html>
"""
