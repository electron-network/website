from django.db import models

from website.models import BaseModel


class Signup(BaseModel):
    email = models.EmailField(max_length=200, db_index=True)
    opt_out = models.BooleanField(default=False, db_index=True)
