# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-21 13:05
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import weblate.utils.fields
import weblate.utils.render


class Migration(migrations.Migration):

    replaces = [
        ("accounts", "0001_initial"),
        ("accounts", "0002_auto_20140923_1543"),
        ("accounts", "0003_auto_20141104_1159"),
        ("accounts", "0004_auto_20150108_1424"),
        ("accounts", "0005_auto_20150330_1358"),
        ("accounts", "0006_profile_hide_completed"),
        ("accounts", "0007_auto_20150427_1505"),
        ("accounts", "0008_profile_hide_source_secondary"),
        ("accounts", "0009_auto_20150630_1213"),
        ("accounts", "0010_auto_20150819_1457"),
        ("accounts", "0011_auto_20150916_0952"),
        ("accounts", "0012_auto_20151112_0738"),
        ("accounts", "0013_auto_20151222_1006"),
        ("accounts", "0014_auto_20160302_1025"),
        ("accounts", "0015_auto_20160304_1418"),
        ("accounts", "0016_add-api-keys"),
        ("accounts", "0017_anonymous_profile"),
        ("accounts", "0018_autogroup_users"),
        ("accounts", "0019_auto_20160520_1358"),
        ("accounts", "0020_remove_projects_dashboard"),
        ("accounts", "0021_auto_20160520_1401"),
        ("accounts", "0022_auto_20160520_1434"),
        ("accounts", "0023_auto_20161021_1502"),
        ("accounts", "0024_auto_20161024_0902"),
        ("accounts", "0025_auto_20170211_1609"),
        ("accounts", "0026_profile_special_chars"),
        ("accounts", "0027_auto_20170317_1441"),
        ("accounts", "0028_auto_20170323_0838"),
        ("accounts", "0029_auto_20170503_1257"),
        ("accounts", "0030_auditlog"),
        ("accounts", "0031_auto_20170503_1414"),
        ("accounts", "0032_auto_20170605_2025"),
        ("accounts", "0033_auto_20171025_1453"),
        ("accounts", "0034_auto_20171129_1438"),
        ("accounts", "0035_user_agent"),
        ("accounts", "0036_auto_20180201_1059"),
        ("accounts", "0037_auto_20180416_1406"),
    ]

    initial = True

    dependencies = [
        ("trans", "0058_componentlist"),
        ("lang", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("social_django", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        blank=True,
                        choices=settings.LANGUAGES,
                        max_length=10,
                        verbose_name="Interface Language",
                    ),
                ),
                ("suggested", models.IntegerField(db_index=True, default=0)),
                ("translated", models.IntegerField(db_index=True, default=0)),
                (
                    "subscribe_any_translation",
                    models.BooleanField(
                        default=False, verbose_name="Notification on any translation"
                    ),
                ),
                (
                    "subscribe_new_string",
                    models.BooleanField(
                        default=False,
                        verbose_name="Notification on new string to translate",
                    ),
                ),
                (
                    "subscribe_new_suggestion",
                    models.BooleanField(
                        default=False, verbose_name="Notification on new suggestion"
                    ),
                ),
                (
                    "subscribe_new_contributor",
                    models.BooleanField(
                        default=False, verbose_name="Notification on new contributor"
                    ),
                ),
                (
                    "subscribe_new_comment",
                    models.BooleanField(
                        default=False, verbose_name="Notification on new comment"
                    ),
                ),
                (
                    "subscribe_merge_failure",
                    models.BooleanField(
                        default=False, verbose_name="Notification on merge failure"
                    ),
                ),
                (
                    "subscribe_new_language",
                    models.BooleanField(
                        default=False,
                        verbose_name="Notification on new language request",
                    ),
                ),
                (
                    "languages",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Choose which languages you prefer to translate. These will be offered to you on the dashboard to have easier access to chosen translations.",
                        to="lang.Language",
                        verbose_name="Translated languages",
                    ),
                ),
                (
                    "secondary_languages",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Choose languages you can understand, strings in those languages will be shown in addition to the source string.",
                        related_name="secondary_profile_set",
                        to="lang.Language",
                        verbose_name="Secondary languages",
                    ),
                ),
                (
                    "subscriptions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="You can receive notifications for watched projects and they are shown on the dashboard by default.",
                        to="trans.Project",
                        verbose_name="Watched projects",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "hide_completed",
                    models.BooleanField(
                        default=False,
                        verbose_name="Hide completed translations on the dashboard",
                    ),
                ),
                (
                    "secondary_in_zen",
                    models.BooleanField(
                        default=True,
                        verbose_name="Show secondary translations in the Zen mode",
                    ),
                ),
                (
                    "hide_source_secondary",
                    models.BooleanField(
                        default=False,
                        verbose_name="Hide source if there is secondary language",
                    ),
                ),
                (
                    "dashboard_component_list",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="trans.ComponentList",
                        verbose_name="Default component list",
                    ),
                ),
                (
                    "dashboard_view",
                    models.IntegerField(
                        choices=[
                            (1, "Watched translations"),
                            (2, "Your languages"),
                            (6, "Component lists"),
                            (4, "Component list"),
                            (5, "Suggested translations"),
                        ],
                        default=1,
                        verbose_name="Default dashboard view",
                    ),
                ),
                (
                    "editor_link",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="Enter custom URL to be used as link to open source code. You can use %(branch)s for branch, %(file)s and %(line)s as filename and line placeholders. Usually something like editor://open/?file=%(file)s&line=%(line)s is good option.",
                        max_length=200,
                        validators=[weblate.utils.render.validate_editor],
                        verbose_name="Editor link",
                    ),
                ),
                (
                    "special_chars",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="You can specify additional special characters to be shown in the visual keyboard while translating. It can be useful for chars you use frequently but are hard to type on your keyboard.",
                        max_length=30,
                        verbose_name="Special characters",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="VerifiedEmail",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                (
                    "social",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="social_django.UserSocialAuth",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AuditLog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "activity",
                    models.CharField(
                        choices=[
                            ("auth-connect", "auth-connect"),
                            ("auth-disconnect", "auth-disconnect"),
                            ("connect", "connect"),
                            ("failed-auth", "failed-auth"),
                            ("locked", "locked"),
                            ("login", "login"),
                            ("login-new", "login-new"),
                            ("password", "password"),
                            ("register", "register"),
                            ("removed", "removed"),
                            ("reset", "reset"),
                            ("reset-request", "reset-request"),
                            ("tos", "tos"),
                        ],
                        db_index=True,
                        max_length=20,
                    ),
                ),
                ("params", weblate.utils.fields.JSONField()),
                ("address", models.GenericIPAddressField(null=True)),
                ("timestamp", models.DateTimeField(auto_now_add=True, db_index=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("user_agent", models.CharField(default="", max_length=200)),
            ],
            options={"ordering": ["-timestamp"]},
        ),
    ]
