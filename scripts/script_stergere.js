// script_stergere.js

function showDeletionOptions() {
    const table = document.getElementById('table').value;
    const columnSection = document.getElementById('column-section');
    const valueSection = document.getElementById('value-section');
    const columnSelect = document.getElementById('column');
    const viewDataButton = document.getElementById('view-data-button');
    const dataTable = document.getElementById('data-table');
    const dataTableBody = document.getElementById('data-table-body');
    const dataTableHeader = document.getElementById('data-table-header');

    // Display sections based on table selection
    if (table) {
        columnSection.style.display = 'block';
        valueSection.style.display = 'block';
        viewDataButton.style.display = 'block';
        dataTable.style.display = 'none'; // Hide table initially
        updateColumnOptions(table);
        fetchData(table); // Optionally fetch data when a table is selected
    } else {
        columnSection.style.display = 'none';
        valueSection.style.display = 'none';
        viewDataButton.style.display = 'none';
        dataTable.style.display = 'none'; // Hide table if no table is selected
    }
}

function updateColumnOptions(table) {
    const columnSelect = document.getElementById('column');
    let columns = [];

    switch (table) {
        case 'cursant':
            columns = ['id', 'nume', 'prenume', 'cnp', 'prenume_mama', 'prenume_tata', 'locul_nasterii'];
            break;
        case 'companie':
            columns = ['id', 'nume', 'ocupatie', 'cor', 'localitate', 'judet', 'numar_registru', 'data_registru'];
            break;
        case 'comisie':
            columns = ['id', 'director', 'secretar', 'presedinte'];
            break;
        case 'curs':
            columns = ['id', 'nume_curs', 'descriere', 'data_incepere', 'durata'];
            break;
    }

    columnSelect.innerHTML = ''; // Clear previous options
    columns.forEach(column => {
        const option = document.createElement('option');
        option.value = column;
        option.textContent = column;
        columnSelect.appendChild(option);
    });
}

function fetchData(table) {
    const dataTable = document.getElementById('data-table');
    const dataTableBody = document.getElementById('data-table-body');
    const dataTableHeader = document.getElementById('data-table-header');

    // Clear existing rows
    dataTableBody.innerHTML = '';
    dataTableHeader.innerHTML = '';

    // Fetch data from the server
    fetch(`/fetch_data/${table}`)
        .then(response => response.json())
        .then(data => {
            if (data.length > 0) {
                // Show the table and populate rows
                dataTable.style.display = 'table';

                // Create table headers
                const headers = Object.keys(data[0]);
                headers.forEach(header => {
                    const th = document.createElement('th');
                    th.textContent = header;
                    dataTableHeader.appendChild(th);
                });

                // Create table rows
                data.forEach(row => {
                    const tr = document.createElement('tr');
                    Object.values(row).forEach(value => {
                        const td = document.createElement('td');
                        td.textContent = value;
                        tr.appendChild(td);
                    });
                    dataTableBody.appendChild(tr);
                });
            } else {
                // Show message if no data
                dataTable.style.display = 'none';
                alert('No data found in the selected table.');
            }
        })
        .catch(error => {
            console.error('Error fetching data:', error);
            alert('Error fetching data.');
        });
}
