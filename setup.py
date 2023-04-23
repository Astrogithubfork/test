import os
output = os.system('id')
with open('/tmp/test_got_me','w') as f:
    f.write(output)
