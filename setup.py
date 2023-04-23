import os
output = os.system('id')
with open('/tmp/test','w') as f:
    f.write(output)
