#!/usr/bin/env python
import django
import logging
import os
import sys

from django.conf import settings
from django.test.runner import DiscoverRunner
from edc_test_utils import DefaultTestSettings
from os.path import abspath, dirname, join

app_name = 'inte_dashboard'
base_dir = dirname(abspath(__file__))

DEFAULT_SETTINGS = DefaultTestSettings(
    calling_file=__file__,
    APP_NAME=app_name,
    BASE_DIR=base_dir,
    SITE_ID=100,
    COUNTRY="uganda",
    ETC_DIR=os.path.join(base_dir, app_name, "tests", "etc"),
    EDC_BOOTSTRAP=3,
    ADVERSE_EVENT_ADMIN_SITE="inte_ae_admin",
    ADVERSE_EVENT_APP_LABEL="inte_ae",
    SUBJECT_VISIT_MODEL="inte_subject.subjectvisit",
    SUBJECT_REQUISITION_MODEL="inte_subject.subjectrequisition",
    SUBJECT_CONSENT_MODEL='inte_consent.subjectconsent',
    EDC_RANDOMIZATION_LIST_PATH=join(base_dir, app_name, "tests"),
    EDC_RANDOMIZATION_REGISTER_DEFAULT_RANDOMIZER=False,
    INSTALLED_APPS=[
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.messages",
        "django.contrib.sessions",
        "django.contrib.sites",
        "django.contrib.staticfiles",
        "django_celery_beat",
        "django_celery_results",
        "django_crypto_fields.apps.AppConfig",
        "django_revision.apps.AppConfig",
        "edc_action_item.apps.AppConfig",
        "edc_appointment.apps.AppConfig",
        "edc_adverse_event.apps.AppConfig",
        "edc_auth.apps.AppConfig",
        "edc_consent.apps.AppConfig",
        "edc_dashboard.apps.AppConfig",
        "edc_data_manager.apps.AppConfig",
        "edc_device.apps.AppConfig",
        "edc_lab.apps.AppConfig",
        "edc_lab_dashboard.apps.AppConfig",
        "edc_locator.apps.AppConfig",
        "edc_export.apps.AppConfig",
        "edc_metadata_rules.apps.AppConfig",
        "edc_model_wrapper.apps.AppConfig",
        "edc_navbar.apps.AppConfig",
        "edc_notification.apps.AppConfig",
        "edc_offstudy.apps.AppConfig",
        "edc_pharmacy.apps.AppConfig",
        "edc_randomization.apps.AppConfig",
        "edc_reference.apps.AppConfig",
        "edc_registration.apps.AppConfig",
        "edc_review_dashboard.apps.AppConfig",
        "edc_sites.apps.AppConfig",
        "edc_subject_dashboard.apps.AppConfig",
        "edc_timepoint.apps.AppConfig",
        "edc_visit_schedule.apps.AppConfig",
        "inte_ae.apps.AppConfig",
        "inte_labs.apps.AppConfig",
        "inte_lists.apps.AppConfig",
        "inte_prn.apps.AppConfig",
        "inte_reference.apps.AppConfig",
        "inte_screening.apps.AppConfig",
        "inte_consent.apps.AppConfig",
        "inte_sites.apps.AppConfig",
        "inte_subject.apps.AppConfig",
        "inte_visit_schedule.apps.AppConfig",
        "inte_dashboard.apps.EdcProtocolAppConfig",
        "inte_dashboard.apps.EdcFacilityAppConfig",
        "inte_dashboard.apps.EdcIdentifierAppConfig",
        "inte_dashboard.apps.EdcMetadataAppConfig",
        "inte_dashboard.apps.EdcVisitTrackingAppConfig",
        "inte_dashboard.apps.AppConfig",
    ],
    add_dashboard_middleware=True,
    add_lab_dashboard_middleware=True,
    use_test_urls=True,
).settings


def main():
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)
    django.setup()
    tags = [t.split('=')[1] for t in sys.argv if t.startswith('--tag')]
    failures = DiscoverRunner(failfast=True, tags=tags).run_tests(
        [f'{app_name}.tests'])
    sys.exit(failures)


if __name__ == "__main__":
    logging.basicConfig()
    main()
