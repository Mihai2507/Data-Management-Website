function handleDropdownChange() {
            var dropdown = document.getElementById('dropdown');
            var cursantForm = document.getElementById('cursantForm');
            var companieForm = document.getElementById('companieForm');
            var comisieForm = document.getElementById('comisieForm');
            var cursForm = document.getElementById('cursForm');

            cursantForm.classList.add('hidden');
            companieForm.classList.add('hidden');
            comisieForm.classList.add('hidden');
            cursForm.classList.add('hidden');

            if (dropdown.value === 'option1') {
                cursantForm.classList.remove('hidden');
            } else if (dropdown.value === 'option2') {
                companieForm.classList.remove('hidden');
            } else if (dropdown.value === 'option3') {
                comisieForm.classList.remove('hidden');
            } else if (dropdown.value === 'option4') {
                cursForm.classList.remove('hidden');
            }
        }

        function validateForm() {
            var cnp = document.getElementById('cursantCNP').value;
            var nume = document.getElementById('cursantNume').value;

            if (cnp.length !== 13) {
                alert("CNP-ul trebuie să aibă 13 caractere!");
                return false;
            }


            if (!['1', '2', '3', '4', '5', '6', '7', '8'].includes(cnp[0])) {
                alert("CNP-ul nu trebuie să înceapă cu 0 sau 9!");
                return false;
            }


            if (cnp.trim() === "") {
                alert("CNP-ul este gol!");
                return false;
            }


            if (!/^\d+$/.test(cnp)) {
                alert("CNP-ul nu trebuie să conțină litere!");
                return false;
            }

            var valoare_ct = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9];
            var suma = 0;
            for (var i = 0; i < 12; i++) {
                suma += parseInt(cnp[i]) * valoare_ct[i];
            }
            var cifra_control = suma % 11;
            if (cifra_control === 10) {
                cifra_control = 1;
            }
            if (cifra_control !== parseInt(cnp[12])) {
                alert("Ultima cifră a CNP-ului nu este corectă!");
                return false;
            }

            if (nume.trim() === "") {
                alert("Numele nu poate fi gol!");
                return false;
            }


            if (/\d/.test(nume)) {
                alert("Numele nu trebuie să conțină cifre!");
                return false;
            }

            var car_interzise = /[@\/+=?!;<>#$&*()%~':\[\]{}]/;
            if (car_interzise.test(nume)) {
                alert("Numele nu trebuie să conțină caractere speciale interzise!");
                return false;
            }

            return true;
        }