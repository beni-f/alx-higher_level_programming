const $list = $('ul#list_movies') 
$.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function(datas){
        $.each(datas.results, function(i, data) {
            $list.append('<li>' + data.title);
        })
    }
})