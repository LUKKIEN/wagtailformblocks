function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1)
                );
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie("csrftoken");
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
}
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    },
});

function showSuccess(form, message) {
    form.replaceWith("<p class='success'>" + message + "</p>");
}

function showError(form, message) {
    form.children("p.error").remove();
    form.prepend("<p class='error'>" + message + "</p>");
}

$(document).on("submit", "form[id^='wagtailformblock_']", (e) => {
    // Prevent the form from submitting on it's own
    e.preventDefault();

    const $form = $(e.target);
    const action = $form.attr("action");
    const data = $form.serializeArray();

    $.post(action, data, function (data) {
        showSuccess($form, data.message);
    }).fail(function (err) {
        showError($form, err.responseJSON.message);
    });
});
