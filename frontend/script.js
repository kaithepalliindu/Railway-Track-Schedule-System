function loadTrains() {
    fetch("http://127.0.0.1:5000/api/trains")
        .then(response => response.json())
        .then(data => {
            let table = document.getElementById("trainTable");
            table.innerHTML = "";

            data.forEach(train => {
                let row = table.insertRow();
                row.insertCell(0).innerText = train.train_name;
                row.insertCell(1).innerText = train.train_no;
                row.insertCell(2).innerText = train.from;
                row.insertCell(3).innerText = train.to;
                row.insertCell(4).innerText = train.seats_available;
                row.insertCell(5).innerText = train.arrival;
                row.insertCell(6).innerText = train.departure;
            });
        })
        .catch(error => alert("Backend not running"));
}
