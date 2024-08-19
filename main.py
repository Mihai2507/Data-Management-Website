from flask import Flask, render_template, request, redirect, url_for
from adaugare import adauga_inregistrari
from stergere import sterge_inregistrare
from actualizare import actualizeaza_inregistrare

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/adaugare', methods=['GET', 'POST'])
def adaugare():
    if request.method == 'POST':
        if request.form['form_type'] == 'cursant':
            nume = request.form['cursantNume']
            cnp = request.form['cursantCNP']
            judet_sector = request.form['cursantJudetSector']
            localitate = request.form['cursantLocalitate']
            prenume_mama = request.form['cursantParinteMama']
            prenume_tata = request.form['cursantParinteTata']
            anul_nasterii = request.form['cursantAnulNasterii']
            luna_nasterii = request.form['cursantLunaNasterii']
            ziua_nasterii = request.form['cursantZiuaNasterii']
            locul_nasterii = request.form['cursantLocNastere']

            cursant_data = {
                'nume': nume,
                'cnp': cnp,
                'judet_sector': judet_sector,
                'localitate': localitate,
                'prenume_mama': prenume_mama,
                'prenume_tata': prenume_tata,
                'anul_nasterii': anul_nasterii,
                'luna_nasterii': luna_nasterii,
                'ziua_nasterii': ziua_nasterii,
                'locul_nasterii': locul_nasterii
            }
            adauga_inregistrari(cursant_data, 'cursant')

        elif request.form['form_type'] == 'companie':
            nume = request.form['companieNume']
            localitate = request.form['companieLocalitate']
            judet = request.form['companieJudet']

            companie_data = {
                'nume': nume,
                'localitate': localitate,
                'judet': judet,
            }
            adauga_inregistrari(companie_data, 'companie')

        elif request.form['form_type'] == 'comisie':
            director = request.form['comisieDirector']
            secretar = request.form['comisieSecretar']
            presedinte = request.form['comisiePresedinte']

            comisie_data = {
                'director': director,
                'secretar': secretar,
                'presedinte': presedinte,
            }
            adauga_inregistrari(comisie_data, 'comisie')

        elif request.form['form_type'] == 'curs':
            nume_curs = request.form['cursNume']
            descriere = request.form['cursDescriere']
            cor = request.form['cursCor']
            nr_registru = request.form['cursNrRegistru']
            data_incepere = request.form['cursDataIncepere']
            data_finalizare = request.form['cursDataFinalizare']
            durata = request.form['cursDurata']
            anul_examinarii = request.form['cursAnulExaminarii']
            luna_examinarii = request.form['cursLunaExaminarii']
            ziua_examinarii = request.form['cursExaminarii']

            curs_data = {
                'nume_curs': nume_curs,
                'descriere': descriere,
                'cor': cor,
                'nr_registru': nr_registru,
                'data_incepere': data_incepere,
                'data_finalizare': data_finalizare,
                'durata': durata,
                'anul_examinarii': anul_examinarii,
                'luna_examinarii': luna_examinarii,
                'ziua_examinarii': ziua_examinarii,
            }
            adauga_inregistrari(curs_data, 'curs')

        return redirect(url_for('adaugare'))
    return render_template('adaugare_date.html')


@app.route('/generare_documente', methods=['GET', 'POST'])
def generare_documente():
    return render_template('generare_documente.html')


@app.route('/actualizare_date', methods=['GET', 'POST'])
def actualizare_date():
    if request.method == 'POST':
        table = request.form.get('table')
        column = request.form.get('column')
        old_value = request.form['old_value']
        new_value = request.form.get('new_value')
        if not table or not column or not new_value:
            return "Error: Missing data in form", 400

        actualizeaza_inregistrare(table, column, old_value, new_value)
        return redirect(url_for('actualizare_date'))
    return render_template('actualizare_date.html')


@app.route('/stergere_date', methods=['GET', 'POST'])
def stergere_date():
    if request.method == 'POST':
        table = request.form['table']
        column = request.form['column']
        value = request.form['value']
        sterge_inregistrare(table, column, value)
        return redirect(url_for('stergere_date'))
    return render_template('stergere_date.html')


if __name__ == '__main__':
    app.run(debug=True)
