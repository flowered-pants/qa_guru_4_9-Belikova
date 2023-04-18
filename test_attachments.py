import allure
from allure import attachment_type
import json
def test_attachmants():
    allure.attach('text', name='text', attachment_type=attachment_type.TEXT)
    allure.attach('<h2> Тэг <h2>', name='html', attachment_type=attachment_type.HTML)
    allure.attach('{first:1, second:2} ', name='jsom', attachment_type=attachment_type.JSON)

