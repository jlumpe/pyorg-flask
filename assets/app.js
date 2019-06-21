$(document).ready(function () {

    // Toggle sidebar menu expansion on click
    $('.sidebar li.menu-collapse > a').click(function () {
        console.log('clicked');
        $(this).parent().toggleClass('expanded');
    });

    // Indeterminate state on checkboxes can only be set thru JS
    $('.org-item.org-checkbox-trans > .org-checkbox').each(function () {
        $(this).prop('indeterminate', true);
    });
});