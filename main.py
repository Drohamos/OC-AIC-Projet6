from fabric import Connection

pc1 = Connection('linuxlocal@192.168.1.156')

result = pc1.run('hostname -s', hide=True)
print(result.stdout)