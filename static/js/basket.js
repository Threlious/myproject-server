window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {
        let target = event.target;
        let basketId = target.name;
        let basketQuantity = target.value;
        $.ajax({
            url: '/baskets/basket-edit/' + basketId + '/' + basketQuantity + '/',
            success: function (data) {
                $('.basket_list').html(data.result)
            }
        })
    })
}