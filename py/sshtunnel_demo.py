import paramiko
from sshtunnel import SSHTunnelForwarder

# 使用sshtunnel + paramiko ssh到服务器
# local <==ssh==> REMOTE_SERVER_IP <==ssh==> PRIVATE_SERVER_IP
# 参考 https://github.com/pahaz/sshtunnel

REMOTE_SERVER_IP = '52.*.*.*'
PRIVATE_SERVER_IP = '192.168.*.*'

REMOTE_USER = 'ec2-user'
PRIVATE_USER = 'ec2-user'

PKEY_PATH = '~/.ssh/your_remote_server.pem'
PKEY_PATH2 = '~/.ssh/your_private_server.pem'

with SSHTunnelForwarder(
    (REMOTE_SERVER_IP, 22),
    ssh_username=REMOTE_USER,
    ssh_pkey=PKEY_PATH,
    remote_bind_address=(PRIVATE_SERVER_IP, 22),
    local_bind_address=('', 10022)
) as tunnel:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('127.0.0.1', 10022, PRIVATE_USER, key_filename=PKEY_PATH2)
    # do some operations with client session
    stdin, stdout, stderr = client.exec_command('ls -l')
    for line in stdout.readlines():
        print(line, end='')
    client.close()

print('FINISH!')
