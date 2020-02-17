/**
 * Created by Shijia on 2016/11/23.
 */
$(function() {
    $('#btnSignUp').click(function() {

        $.ajax({
            url: '/sign_up',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});