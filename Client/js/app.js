let selectedPredictions = new Map();
let selectedAttribute = null;
let userFile = null;

// Welcome view asking to provide an CSV file
function renderWelcomeView() {
    //$( ".sup" ).text("Next Step...");
    console.log('sup from Welcome View');
}

// Pretraining view asking to provide predictions and an attribute
function renderPretrainingView(data) {
    console.log('sup from Pretraining View');
    let predictors = data[0];
    $("main").html(
        '<div class="container text-center"> \
            <h1 class="display-1 mt-5">Easy ML</h1> \
                <p class="lead mb-5">Machine Learning accessible to anyone!</p> \
            <div class="col-lg col-5 text-left"> \
                <label for="file">1. Choose your predictors (1-' + data[0].length +')</label> \
            </div> \
            <div id="predicate_buttons">'
                + predictors.map((predictor, index) => renderUnselectedPredictor(predictor, index)).join('') +
            '</div> \
            <div class="col-lg col-5 text-left"> \
                <label>2. Choose an attribute explanation</label> \
            </div> \
            <div id="attribute_buttons" class="mb-5">'
                + predictors.map((predictor, index) => renderAttributes(predictor, index)).join('') +
            '</div> \
            <div class="mb-5"> \
                <button type="button" class="btn btn-primary" onclick="trainButtonDidPress(this)">Submit</button> \
            </div>'
    );
    selectedPredictions = new Map();
    selectedAttribute = null;
}

// Result view that provides the accuracy of the trained model as well as
// allows to predict an attribute based on predictors
function renderResultView() {

}

function renderUnselectedPredictor(predictor, index) {
    // 0 ... n - 1
    return '<button id=predictor_' + predictor + ' type="button" class="btn btn-secondary" onclick="predictionButtonDidClick(this)">' + predictor + '</button>';
}

function renderAttributes(predictor, index) {
    // 0 ... n - 1
    return '<button id=attribute_' + predictor + ' type="button" class="btn btn-secondary" onclick="attributeButtonDidClick(this)">' + predictor + '</button>';
}

function predictionButtonDidClick(button) {
    const id = button.id.replace('predictor_', '');
    if (selectedAttribute !== id) {
        if (isSelected(button)) {
            selectedPredictions.delete(id);
            console.log(selectedPredictions);
            unselectPredictorButton(id);
        } else {
            selectedPredictions.set(id, true);
            console.log(selectedPredictions);
            selectPredictorButton(id);
        }
    }
}

function attributeButtonDidClick(button) {
    const id = button.id.replace('attribute_', '');
    // step 2 has to be after step 1
    if (selectedPredictions.size > 0 && !selectedPredictions.has(id)) {
        unselectAttributeButton(selectedAttribute);
        if (isSelected(button)) {
            selectedAttribute = null;
        } else {
            // if the id is already in the predictions or don't allow the user to choose it
            selectedAttribute = id;
            selectAttributeButton(id);
        }
    }
}

// Predictor buttons
function unselectPredictorButton(id) {
    const element = '<button id=predictor_' + id + ' type="button" class="btn btn-secondary" onclick="predictionButtonDidClick(this)">' + id + '</button>';
    let elementId = '#predictor_' + id;
    $(elementId).replaceWith(element);
}

function selectPredictorButton(id) {
    const element = '<button id=predictor_' + id + ' type="button" class="btn btn-primary" onclick="predictionButtonDidClick(this)">' + id + '</button>';
    let elementId = '#predictor_' + id;
    $(elementId).replaceWith(element);
}

// Attribute buttons
function unselectAttributeButton(id) {
    const element = '<button id=attribute_' + id + ' type="button" class="btn btn-secondary" onclick="attributeButtonDidClick(this)">' + id + '</button>';
    let elementId = '#attribute_' + id;
    $(elementId).replaceWith(element);
}

function selectAttributeButton(id) {
    const element = '<button id=attribute_' + id + ' type="button" class="btn btn-primary" onclick="attributeButtonDidClick(this)">' + id + '</button>';
    let elementId = '#attribute_' + id;
    $(elementId).replaceWith(element);
}

function isSelected(button) {
    return button.className.includes('btn-primary') ;
}


function fileDidAdd() {
    userFile = document.getElementById('file');
    Papa.parse(userFile.files[0], {
        complete: function(results) {
            let data = results.data;
            let predictors = data[0];

            renderPretrainingView(data);
        }
    });
}


function trainButtonDidPress() {
    if (selectedPredictions.size > 0 && selectedAttribute !== null) {

        let form = new FormData();
        form.append("data", "/Users/lysov/Desktop/train.csv");
        console.log(form);

        const settings = {
            "async": true,
            "crossDomain": true,
            "url": "http://127.0.0.1:8000/api/files/?features=1stFlrSF&label=SalePrice/",
            "method": "POST",
            "headers": {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            "processData": false,
            "contentType": false,
            "mimeType": "multipart/form-data",
            "data": form
        }

        $.ajax(settings).done(function (response) {
            console.log(response);
        }).fail(function(xhr, err) {

            var responseTitle= $(xhr.responseText).filter('title').get(0);
            alert($(responseTitle).text() + "\n" + formatErrorMessage(xhr, err) );
        });
    }

}

renderWelcomeView();
