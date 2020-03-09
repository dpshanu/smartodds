from flask import Flask, jsonify, render_template, request, url_for, redirect
import logging
from db.models import get_session, Tennis
app = Flask(__name__, template_folder='../templates')



@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200

@app.route('/', methods=['GET','POST'])
def display_tennis_data():
    """

    :return: support the displays of the tennis data
    """
    session = get_session()
    tennis_data = session.query(Tennis).all()

    return render_template(
        "tennis_data.html",
        tennis_data=tennis_data,
    )

@app.route('/get-tennis-data', methods=['GET'])
def get_tennis_data():
    """

    :return: json for the REST API
    """
    session = get_session()
    tennis_data = session.query(Tennis).all()
    data = []
    for row in tennis_data:
        try:
            output_schema = \
                {
                    'ATP': row.atp,
                    'Location': row.location,
                    'Tournament': row.tournament,

                }
        except Exception as e:
            logging.exceptin("none")
            return row

        data.append(output_schema)

    return jsonify(data)


@app.route('/set-tennis-data/<id>', methods=['GET', 'POST'])
def set_tennis_data(id):
    """

    :param id: primary key in tennis_data table
    :return: write-back to db
    """
    session = get_session()

    if request.method == 'POST':

        def get_data_from_form(form):
            data = []
            data.append(
                {
                    "atp": form["atp"],
                    "location": form["location"],
                    "tournament": form["tournament"],
                }
            )
            return data

        data = get_data_from_form(request.form)
        session.query(Tennis).filter_by(id=request.form['id']).update(data[0])
        session.commit()

        return redirect(url_for("display_tennis_data"))

    selected_record = session.query(Tennis).filter_by(id=id).one()
    return render_template("selected_tennis_data_record.html", srecord=selected_record)


if __name__ == "__main__":
   app.run(debug=False, host='0.0.0.0', port=8080)