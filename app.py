from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)



notes = {}
note_id = 1

@app.route('/')
def home():
    return render_template('home.html', notes=notes)


@app.route('/add_note', methods=['POST'])
def add_note():
    global note_id
    note = request.form['note']
    notes[note_id] = note
    note_id += 1
    return redirect(url_for('home'))

@app.route('/delete_note/<int:id>', methods=['POST'])
def delete_note(id):
    if id in notes:
        del notes[id]
    return redirect(url_for('home'))

@app.route('/update_note/<int:id>', methods=['GET', 'POST'])
def update_note(id):
    if request.method == 'POST':
        note = request.form['note']
        notes[id] = note
        return redirect(url_for('home'))
    return render_template('update.html', id=id, note=notes[id])

@app.route('/replace_note/<int:id>', methods=['POST'])
def replace_note(id):
    new_note = request.form['note']
    notes[id] = new_note
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)