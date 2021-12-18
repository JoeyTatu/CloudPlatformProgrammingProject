# This generates the secret key for the SQLAchemy DB
# @ref: https://stackoverflow.com/questions/34902378/where-do-i-get-a-secret-key-for-flask

import uuid
print(uuid.uuid4().hex)