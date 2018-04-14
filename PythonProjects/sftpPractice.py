import pysftp

with pysftp.Connection('demo.wftpserver.com', 'demo-user', 'demo-user') as sftp:
    with sftp.cd('public'):
        sftp.put('C:\Users\Kevin\PythonProjects')
        sftp.get('Report19022018.docx')
        


