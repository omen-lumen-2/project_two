# -*- coding: utf-8 -*-
from random import choice

from model.project import Project


def test_delete_project(app):
    app.project_helper.project_must_exist()
    raw_projects = app.project_helper.get_project_list()
    project = choice(raw_projects)

    app.project_helper.delete_project_by_id(id=project.id)

    update_projects = app.project_helper.get_project_list()
    raw_projects.remove(project)
    assert sorted(raw_projects, key=Project.id_or_max) == sorted(update_projects, key=Project.id_or_max)
