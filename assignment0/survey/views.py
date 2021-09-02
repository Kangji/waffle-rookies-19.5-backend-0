import json
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.db import models

from survey.models import SurveyResult, OperatingSystem
from survey.serializers import serialize_survey_result, serialize_os


def get_survey_results(request):
    if request.method == 'GET':
        os = request.GET.get('os')
        survey_results = SurveyResult.objects.all()
        survey_results = list(map(lambda result: serialize_survey_result(result), survey_results))
        if os is not None:
            survey_results = list(filter(lambda result: result['os']['name'] == os, survey_results))
        return JsonResponse({"surveys": survey_results}, status=200)
    else:
        return HttpResponseNotAllowed(['GET', ])


def get_survey(request, survey_id):
    if request.method == 'GET':
        survey = get_object_or_404(SurveyResult, id=survey_id)
        return JsonResponse(serialize_survey_result(survey))
    else:
        return HttpResponseNotAllowed(['GET', ])


def get_os_all(request):
    if request.method == 'GET':
        all_os = list(map(lambda os: serialize_os(os), OperatingSystem.objects.all()))
        return JsonResponse({"os": all_os}, status=200)
    else:
        return HttpResponseNotAllowed(['GET', ])


def get_os(request, os_id):
    if request.method == 'GET':
        try:
            os = OperatingSystem.objects.get(id=os_id)
            return JsonResponse(serialize_os(os), status=200)
        except models.ObjectDoesNotExist:
            return HttpResponseNotFound(content=json.dumps({"msg": "404 not found"}))
