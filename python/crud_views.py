from flask import Blueprint, url_for, redirect, render_template, flash, request
from sqlalchemy.exc import IntegrityError
from $2.models import $3
from $2.extentions import db
from $2.$1s.forms import Add$3Form, Update$3Form


$1s = Blueprint("$1s", __name__)


@$1s.route("/view_$1s", methods=["GET", "POST"])
def view_$1s():
    page = request.args.get("page", 1, type=int)
    $1s = $3.query.paginate(per_page=20, page=page)
    return render_template(
        "$1s/view_$1s.html", page=page, $1s=$1s
    )


@$1s.route("/$1/add", methods=["GET", "POST"])
def add_$1():
    form = Add$3Form()
    if form.validate_on_submit():
        new_$1 = $3(
            $4name=form.$4name.data,
            $4description=form.$4description.data,
        )
        db.session.add(new_$1)
        db.session.commit()
        flash(
            f"$3 '{new_$1.$4name}' added.", category="success"
        )
        return redirect(url_for("$1s.view_$1s"))
    return render_template("$1s/add_$1.html", form=form)


@$1s.route("/$1/<int:id>", methods=["GET", "POST"])
def single_$1(id):
    $1 = $3.query.get_or_404(int(id))
    return render_template("$1s/$1.html", $1=$1)


@$1s.route("/$1/<int:id>/update", methods=["GET", "POST"])
def update_$1(id):
    $1 = $3.query.get_or_404(int(id))
    form = Update$3Form()
    if request.method == "GET":
        form.$4name.data = $1.$4name
        form.$4description.data = $1.$4description
    if form.validate_on_submit():
        $1.$4name = form.$4name.data
        $1.$4description = form.$4description.data
        try:
            db.session.add($1)
            db.session.commit()
        except IntegrityError:
            flash(
                f"A session type with name '{$1.$4name}' already exists.",
                category="danger",
            )
            db.session.rollback()
            return redirect(url_for("update_$1"), id=id)
        flash(
            f"Sucesfully updataed $1 '{$1.$4name}'",
            category="success",
        )
        return redirect(url_for("$1s.view_$1s"))
    return render_template("$1s/update_$1.html", form=form)


@$1s.route("/$1/<int:id>/delete", methods=["GET", "POST"])
def delete_$1(id):
    $1 = $3.query.get_or_404(int(id))
    db.session.delete($1)
    db.session.commit()
    flash("Session type deleted", category="success")
    return redirect(url_for("$1s.view_$1s"))