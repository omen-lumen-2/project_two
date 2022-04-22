from zeep import Client, exceptions

from model.project import Project, status, view_state


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def get_project_list_for_user(self):
        result = []
        client = Client(f'{self.app.base_url}api/soap/mantisconnect.php?wsdl')
        try:
            projects = client.service.mc_projects_get_user_accessible(self.app.login_sudo, self.app.password_sudo)
        except exceptions.Fault:
            projects = []

        for project in projects:
            result.append(Project(id=project['id'],
                    name=project['name'],
                    state=status[project['status']['id']],
                    is_active=True,
                    use_global_setting=None,
                    visible=view_state[project['view_state']['id']],
                    description="" if project['description'] is None else project['description']))
        return result
