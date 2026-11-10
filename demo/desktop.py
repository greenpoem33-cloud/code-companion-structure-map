APPS = {
    'notepad': {'title': '记事本', 'icon': '▤'},
    'calculator': {'title': '计算器', 'icon': '▦'},
}


def make_launch_request(app_id):
    return {'app_id': app_id, 'window': APPS[app_id]}


def open_app(request):
    return request['window']


def on_start_click(app_id):
    request = make_launch_request(app_id)
    return open_app(request)
