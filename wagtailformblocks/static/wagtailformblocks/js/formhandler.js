function showSuccess(form, message) {
    form.replaceWith('<p class=\'success\'>' + message + '</p>');
}

function showError(form, message) {
    form.children('p.error').remove();
    form.prepend('<p class=\'error\'>' + message + '</p>');
}

$(document).on('submit form id[^=wagtailformblock_]', function(e) {
    // Prevent the form from submitting on it's own
    e.preventDefault();

    var $form = $(e.target);
    var action = $form.attr('action');
    var data = $form.serializeArray();

    $.post(action, data, function(data) {
        showSuccess($form, data.message);
    }).fail(function(err) {
        showError($form, err.responseJSON.message);
    });
});
