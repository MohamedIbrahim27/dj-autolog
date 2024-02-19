from auditlog.middleware import AuditlogMiddleware

class mohamed(AuditlogMiddleware):
    def process_request(self, request):
        super().process_request(request)
        self.request_user = request.user

    def get_additional_data(self, instance, **kwargs):
        additional_data = super().get_additional_data(instance, **kwargs)

        if 'username' in additional_data:
            username = additional_data['username']

            # Customize the username in the log message based on your condition
            if username == self.request_user.username:
                additional_data['username'] = f'{username} - request.user'

        return additional_data