"use-strict";
var cs_homepage
cs_homepage || (cs_homepage = {});
cs_homepage.forms || (cs_homepage.forms = {});
cs_homepage.utils || (cs_homepage.utils = {
    submitEmailMessage: function(csrfToken) {
        var formData = {};
        var crsfToken = csrfToken;
        var headers = {
            "X-CSRFToken": crsfToken
        };
        var form = window.document.querySelector('.contact-form-container');
        var email = window.document.querySelector('#mail-email').value;
        var subject = window.document.querySelector('#mail-subject').value;
        var body = window.document.querySelector('#mail-content').value;

        formData.email = email;
        formData.subject = subject;
        formData.message = body;
        formData.csrf = csrfToken;
        formData.messageType = "email";

        promise.post('/message', formData, headers)
               .then(function(error, text, xhr) {
                    if (error) {
                        // naive alerts are blocked, so insert an html
                        // alert above the form
                        cs_homepage.utils.insertErrorMessage(
                            window.document.forms[0],
                            xhr.status,
                            xhr.responseText
                        );
                        return;
                    } else {
                        // naive alerts are blocked, so modify the submit
                        // button to indicate a success
                        cs_homepage.utils.updateEmailButtonText(
                            window.document.querySelector('.msg-submit')
                        );
                        form.reset();
                    }
                });
    },
    updateEmailButtonText: function(element) {
        element.textContent = 'Sent';
        element.classList.add('bt-disabled');

        // clean up any error messages that may have been shown
        var err = window.document.querySelector('.message-error-notify.mdl-shadow--3dp');
        if (err) {
            err.remove();
        }
    },
    insertErrorMessage: function(element, status, text) {
        var toInsert = document.createElement('div');
        toInsert.className = 'message-error-notify mdl-shadow--3dp';
        toInsert.appendChild(
            document.createTextNode(
                'Error sending message!'
        ));
        toInsert.appendChild(document.createElement('br'));
        toInsert.appendChild(
            document.createTextNode(
                'code:' + status
        ));
        toInsert.appendChild(document.createElement('br'));
        toInsert.appendChild(
            document.createTextNode(
                'message:' + text
        ));

        element.parentNode.insertBefore(toInsert, element);
    }
});
