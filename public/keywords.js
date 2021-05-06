
// var submitButton = document.getElementById('submitButton');
// submitButton.addEventListener("click", sendFile)

function sendFile() {

    // // Server request
    // var request = new XMLHttpRequest();

    // // This url could be any url that serves the data we need
    // var requestURL = '/giveMeThing'    

    // get request to get the information (JSON)
    // request.open('GET', requestURL)


    // post request to send data
    // request.open('post', requestURL)

    // Add response listener
    // request.addEventListener('load', function(event){
        
    //     if(event.target.status !== 200) {
    //         alert("Error! Didn't get 200 back")
    //     }

    //     else {

    //         console.log("Got the response")

    //         // This converts the request from JSON to javascript object
    //         var responseParsed = JSON.parse(request.response);
    //         console.log("Response parsed is: ", responseParsed);
    //         var message = document.createElement('h2');
    //         message.textContent = responseParsed.msg;

    //         document.body.appendChild(message); 
    //     }
    // })
    // request.send()
}

// The dropzone options below were crafted with the help of stack overflow. https://stackoverflow.com/questions/17872417/integrating-dropzone-js-into-existing-html-form-with-other-fields

Dropzone.options.myDropzone= {
    paramName: "file",
    autoProcessQueue: false,
    uploadMultiple: false,
    acceptedFiles: '.json',
    maxFiles: 1,
    addRemoveLinks: true,
    init: function() {
        dzClosure = this; // Makes sure that 'this' is understood inside the functions below.

        // for Dropzone to process the queue (instead of default form behavior):
        document.getElementById("submit-all").addEventListener("click", function(e) {
            // Make sure that the form isn't actually being sent.
            e.preventDefault();
            dzClosure.processQueue()
        });

        //send all the form data along with the files:
        this.on("sending", function(file, xhr, formData) {
        });
    }
};