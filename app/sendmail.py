from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from models import Rows
import datetime
import time


class SendMail:
    def __init__(self):
        self.from_email = settings.DEFAULT_FROM_EMAIL

    def send2manager(self):
        rows = Rows.objects.exclude(onboard_time__lte=datetime.datetime.fromtimestamp(time.time() - 60 * 60 * 24 * 14))
        for row in rows:
            new_hire_id = row.new_hire_id
            new_hire_name = row.new_hire_name
            onboard_time = row.onboard_time
            content = """
            <h4>Hi, Manager</h4>
            <p>It's a reminder. Your new hire will onboard soon, please remember to create accounts that are needed for your new hire.</p>
            <table border='2' cellspacing='2' cellpadding='2'>
                <thead>
                <tr>
                    <th>New Hire ID</th>
                    <th>New Hire Name</th>
                    <th>Onboard Time</th>
                    <th>Reminder age</th>
                </tr>
                </thead>
                <tbody>
                    <tr>
            """ + '<td>' + new_hire_id + \
                      '</td>' + '<td>' + new_hire_name + '</td>' + \
                      '<td>' + row.onboard_time.strftime('%Y-%m-%d') + '</td>' + \
                      '<td>' + '0' + '</td>' + \
                      """
                              </tr>
                          </tbody>
                      </table>
                      <p>For more information please refer to the Jiveon page.</p>
                      <p>If you don't want to receive this email again, please close the case in the link below.</p>
                      <a href='http://10.79.41.56/'>New Hire List</a>
                      <br>
                      <p>For more details, please refer to the new hire Jiveon page:<a href='https://cisco.jiveon.com/groups/xerg-crdc-group/projects/new-hire-orientation'>new-hire-orientation</a></p>
                      <br>
                      <p>Thanks</p>
                      <p>Shuzhan</p>
                      """
            msg = EmailMultiAlternatives('Caser ' + str(row.id), content, self.from_email, ['yonie@cisco.com'])
            msg.content_subtype = "html"
            msg.send()
