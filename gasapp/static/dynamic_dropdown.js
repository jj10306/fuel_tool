        let make_select = document.getElementById('make');
        let model_select = document.getElementById('model');
        let year_select = document.getElementById('year');

        make_select.onchange = function() {
            make = make_select.value;
            console.log(make);

            fetch('/model/' + make).then(function(response) {

                response.json().then(function(data) {
                    let optionHTML = '';

                    for (let model of data.models) {
                        optionHTML += '<option value="' + model.model + '">' + model.model + '</option>'; //consider making the value model.id and accounting for that in script
                    }
                    model_select.innerHTML = optionHTML;
                });
            });
        }
        model_select.onchange = function() {
            model = model_select.value;
            console.log(model);

            fetch('/year/' + model).then(function(response) {

                response.json().then(function(data) {
                    let optionHTML = '';

                    for (let year of data.years) {
                        optionHTML += '<option value="' + year.id + '">' + year.year + '</option>';
                    }
                    year_select.innerHTML = optionHTML;
                });
            });
        }