#!/usr/bin/env python


"""
@Author: gorywong
@Date: 2019-01-10 00:48:15
@Software: Visual Studio Code
@Last Modified by: gorywong
@Last Modified time: 2019-01-10 00:48:15
@Description:
"""
from django.conf import settings
from lbyledu.utils import get_site_setting
from article.models import Article, Category


def seo_processor(request):
    site_settings = get_site_setting()
    current_parent_id = request.path.split('/')[1]
    current_child_id = request.path.split('/')[2]
    value = {
        'SITE_NAME': site_settings.sitename,
        'SITE_SEO_DESCRIPTION': site_settings.site_seo_description,
        'SITE_KEYWORDS': site_settings.site_keywords,
        'SITE_BASE_URL': request.scheme + '://' + request.get_host() + '/',
        'current_parent_id': current_parent_id,
        'current_child_id': current_child_id,
        'ARTICLE_SUB_LENGTH': site_settings.article_sub_length,
        'nav_category_list': Category.objects.all(),
        'nav_pages': Article.objects.filter(has_check=True, status='p'),
        'BEIAN_CODE': site_settings.beiancode,
        'ANALYTICS_CODE': site_settings.analyticscode,
        "BEIAN_CODE_GONGAN": site_settings.gongan_beiancode,
        "SHOW_GONGAN_CODE": site_settings.show_gongan_code
    }
    return value