"use-strict";
var cs_homepage
cs_homepage || (cs_homepage = {});
cs_homepage.forms || (cs_homepage.forms = {});
cs_homepage.utils || (cs_homepage.utils = {
    submitMessage: function(csrfToken, formData) {
        var crsfToken = csrfToken;
        var headers = {
            "X-CSRFToken": crsfToken
        };

        promise.post('/message', formData, headers)
               .then(function(error, text, xhr) {
            if (error) {
                alert('Error ' + xhr.status);
                return;
            }
            alert('The formData was submitted.');
        });
    }
});
