alert_system = 'console'        # other value could be email
error_severity = 'critical'     # other values: 'medium' or 'low'
error_message = 'OMG! Something terrible happened!'


def send_email(param, em):
    print('Email sent to:', param, em)


if alert_system == 'console':
    print(error_message)
elif alert_system == 'email':
    if error_severity == 'critical':
        send_email('admin@example.com', error_message)
    elif error_severity == 'medium':
        send_email('support.1@expample.com', error_message)
    elif error_severity == 'low':
        send_email('support.2@example.com', error_message)


