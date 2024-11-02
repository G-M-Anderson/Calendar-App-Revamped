from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app import db
from app.models import Event
from app.forms import EventForm

calendar_bp = Blueprint('calendar', __name__)

@calendar_bp.route('/')
@login_required
def index():
    events = Event.query.filter_by(user_id=current_user.id).all()
    return render_template('events/calendar.html', events=events)

@calendar_bp.route('/event/new', methods=['GET', 'POST'])
@login_required
def new_event():
    form = EventForm()
    if form.validate_on_submit():
        event = Event(
            title=form.title.data,
            description=form.description.data,
            start_time=form.start_time.data,
            end_time=form.end_time.data,
            user_id=current_user.id
        )
        db.session.add(event)
        db.session.commit()
        flash('Event created!', 'success')
        return redirect(url_for('calendar.index'))
    return render_template('events/new_event.html', form=form)
