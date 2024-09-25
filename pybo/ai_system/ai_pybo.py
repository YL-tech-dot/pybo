# ai_pybo.py start_ai가 있던 함수 페이지.

# from pybo.ai_system.lye.ai_system import setup_system
from pybo.ai_system.ai_system import setup_system
# from django.conf import settings     # 기존 Path 모듈을 대체한 settings. 장고에서 url 관련을 나타낼때는 path보다 이 모듈을 사용한다고 함.
#
# import logging # 개발자용 디버깅용 로깅 모듈
#
# import numpy as np
# import pickle
# ai_system.py ocode 제작 모듈
# : AI 시스템 설정을 위한 데코레이터 가져오기

"""
이름변동 사항

1 setup_django_system -> load_config
2 start_ai -> ai_view


setup_django_system 추가사항
1 config 함수화 : load_config
2 사용자 선택 detector 모델 불러오기 조건식 : help_load_detectors
3 사용자 선택 predictor모델 불러오기 조건식 : help_load_predictors
"""


@setup_system  # setup_django_system 데코레이터를 사용해, Django 환경설정에 이어서 ai_view 함수를 사용.
def start_ai(request, image_path, face_recognition_system, target_encodings,*args, **kwargs):
    """ func(request, image_path, ai_system, target_encodings, *args, **kwargs)
    AI 얼굴 인식 시스템을 사용하여 이미지를 처리하고 결과를 반환합니다.
    """
    # 얼굴 인식 시스템을 사용하여 이미지를 처리하고, 결과 이미지의 경로를 받음
    output_path = face_recognition_system.process_image(image_path, target_encodings)
    # 처리된 이미지의 경로를 반환
    print('------------------------------------------------------')
    print('This is output_path ==> ',output_path)
    print('------------------------------------------------------')
    return output_path



""" 하단의 코드는 디버깅을 위한 코드들임. 
    작성중이던 코드였음. 실제로 실행되려면 더 작업 또는 삭제해야하는 코드임. -이예은"""
# from django.test import TestCase ## django 제공 디버깅 모듈
# settings.configure(
#     DEBUG=True,
#     DATABASES={
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': 'mydatabase',
#         }
#     },
    # 다른 설정 값들...
# )
# class AiViewTests(TestCase):
#     def test_ai_view(self):
#         # ai_view 함수의 동작을 검증하는 테스트 코드
#         response = self.client.post('/your-url/', {'detectors': ['dlib']})
#         self.assertEqual(response.status_code, 200)
#
# def validate_config(config):
#     required_keys = ['dlib_model_path', 'yolo_model_path', ...]
#     for key in required_keys:
#         if key not in config:
#             raise ValueError(f"필수 설정 값이 누락되었습니다: {key}")
#
#
# import logging
#
# logger = logging.getLogger(__name__)
#
# class RequestLoggerMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         # 요청 로그 기록
#         logger.debug(f"Request method: {request.method}")
#         logger.debug(f"Request path: {request.path}")
#         logger.debug(f"Request GET data: {request.GET}")
#         logger.debug(f"Request POST data: {request.POST}")
#
#         # 응답 가져오기
#         response = self.get_response(request)
#
#         # 응답 로그 기록
#         logger.debug(f"Response status code: {response.status_code}")
#
#         return response
#
#
# selected_detectors  = 'yolo','cnn'
# selected_predictors = 'fairface'
#
# ai_view(request, image_path, selected_detectors, selected_predictors)