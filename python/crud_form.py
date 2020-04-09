from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from $1.models import $2


class Add$2Form(FlaskForm):
    $3name = StringField(
        "$4 Name", validators=[DataRequired(), Length(max=150)]
    )
    $3description = TextAreaField(
        label="$4 Description", validators=[DataRequired()]
    )
    submit = SubmitField("Add $4 Type")

    def validate_exp_name(self, exp_name):
        name_exists = $2.query.filter_by(exp_name=exp_name.data).first()
        if name_exists:
            raise ValidationError("An experiment with that name already exists.")


class Update$2Form(FlaskForm):
    $3name = StringField(
        "$4 Name", validators=[DataRequired(), Length(max=150)]
    )
    $3description = TextAreaField(
        label="$4 Description", validators=[DataRequired()]
    )
    submit = SubmitField("Update $4 Type")