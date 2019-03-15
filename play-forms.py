#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange



class TestForm(Form):
    name = StringField(validators=[Length(max=3)])
    age = IntegerField(validators=[NumberRange(min=10, max=15)], default=12)


form = TestForm(request.form)
res = form.validate()
if res:
    print(form.name.data)
    print(form.age.data)
else:
    print('error')
