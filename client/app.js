function onClickedEstimatedLoan(){
    console.log("Estimate loan button clicked");
    var gender = document.getElementById("uiGender");
    var education = document.getElementById("uiEducation");
    var married = document.getElementById("uiMarried");
    var dependents = document.getElementById("uiDependents");
    var employed = document.getElementById("uiEmployed");
    var area = document.getElementById("uiArea");
    var applicantincome = document.getElementById("uiApIncome");
    var coapplicantincome = document.getElementById("uiCapIncome");
    var loanamount = document.getElementById("uiLoanAm");
    var loanamountterm = document.getElementById("uiLoanAmTrm");
    var credithistory = document.getElementById("uiCreditHistory");
    var approvalResult = document.getElementById("uiApprovalResult");

    console.log(gender.value, education.value, married.value, dependents.value, employed.value, area.value, applicantincome.value, coapplicantincome.value, loanamount.value, loanamountterm.value, credithistory.value)
    
    var predict_url = "/predict_loan"
    $.post(predict_url,
        {
            gender: gender.value,
            education: education.value,
            married: married.value,
            dependents: dependents.value,
            employed: employed.value,
            area: area.value,
            applicantincome: parseInt(applicantincome.value),
            coapplicantincome: parseInt(coapplicantincome.value),
            loanamount: parseInt(loanamount.value),
            loanamountterm: parseInt(loanamountterm.value),
            credithistory: parseInt(credithistory.value),
        },
        function (data, status){
            console.log("Approval Result: ", data.estimated_loan);
            if (data.estimated_loan.toString() == 'Loan Approved'){
                approvalResult.innerHTML = "<h2 class='text-result-success'>"+data.estimated_loan.toString()+"</h2>"
            }
            else{
                approvalResult.innerHTML = "<h2 class='text-result-failed'>"+data.estimated_loan.toString()+"</h2>"
            }
    });
}

function onPageLoad() {
    console.log("document loaded");
    var url_gender = "http://127.0.0.1:5000/get_gender";
    var url_education = "http://127.0.0.1:5000/get_education";
    var url_married = "http://127.0.0.1:5000/get_married";
    var url_dependents = "http://127.0.0.1:5000/get_dependents";
    var url_employed = "http://127.0.0.1:5000/get_employed";
    var url_area = "http://127.0.0.1:5000/applicantarea";
    $.get(url_gender, function(data_gender, status){
        console.log("Get Gender response");
        if (data_gender) {
            var gender = data_gender.gender;
            var uiGender = document.getElementById("uiGender");
            $("#uiGender").empty();
            for (var i in gender) {
                var opt = new Option(gender[i]);
                $("#uiGender").append(opt);
                console.log(opt)
            }
        }
    });
    $.get(url_education, function(data_education, status){
        console.log("got response for get_education request");
        if (data_education) {
            var education = data_education.education;
            var uiEducation = document.getElementById("uiEducation");
            $("#uiEducation").empty();
            for (var i in education) {
                var opt = new Option(education[i]);
                $("#uiEducation").append(opt);
                console.log(opt)
            }
        }
    });
    $.get(url_married, function(data_married, status){
        console.log("got response for get_married request");
        if (data_married) {
            var married = data_married.married;
            var uiMarried = document.getElementById("uiMarried");
            $("#uiMarried").empty();
            for (var i in married) {
                var opt = new Option(married[i]);
                $("#uiMarried").append(opt);
                console.log(opt)
            }
        }
    });
    $.get(url_dependents, function(data_dependents, status){
        console.log("got response for get_dependents request");
        if (data_dependents) {
            var dependents = data_dependents.dependents;
            var uiDependents = document.getElementById("uiDependents");
            $("#uiDependents").empty();
            for (var i in dependents) {
                var opt = new Option(dependents[i]);
                $("#uiDependents").append(opt);
                console.log(opt)
            }
        }
    });
    $.get(url_employed, function(data_employed, status){
        console.log("got response for get_employed request");
        if (data_employed) {
            var employed = data_employed.employed;
            var uiEmployed = document.getElementById("uiEmployed");
            $("#uiEmployed").empty();
            for (var i in employed) {
                var opt = new Option(employed[i]);
                $("#uiEmployed").append(opt);
                console.log(opt)
            }
        }
    });
    $.get(url_area, function(data_area, status){
        console.log("got response for applicantarea request");
        if (data_area) {
            var area = data_area.area;
            var uiArea = document.getElementById("uiArea");
            $("#uiArea").empty();
            for (var i in area) {
                var opt = new Option(area[i]);
                $("#uiArea").append(opt);
                console.log(opt)
            }
        }
    });
    
}

window.onload = onPageLoad;