# -*- coding: utf-8 -*-

from common.data_generator import random_int
from model.project import Project

def test_add_new_project(app):
    old_projects = app.project_helper.get_project_list()

    expected_project = Project(name=f'Тест имя проекта{random_int(1,1000)}')
    app.project_helper.create(project=expected_project)

    old_projects.append(expected_project.set_default_value())
    new_projects = app.project_helper.get_project_list()

    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)



