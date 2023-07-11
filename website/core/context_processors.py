def body_class(request):
    if request.path == '/':
        return {'body_class': 'app ltr landing-page horizontal'}
    if request.path.startswith('/ru/education/course/'):
        return {'body_class': 'app ltr landing-page horizontal'}
    else:
        return {'body_class': 'app ltr sidebar-mini light-mode'}