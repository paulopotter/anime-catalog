    function sortObject(obj) {
        return Object.keys(obj).sort().reduce(function (result, key) {
            result[key] = obj[key];
            return result;
        }, {});
    }
    var dataOdering = sortObject(data);
    for (var key in dataOdering) {
        console.log(data[key])
        // rulerDiv.innerHTML += '<span><a href="#' + key + '">'+ key + '</span></a>';
        // var el = document.getElementsByClassName('anime-list')[0];

        // for( var i = 0; i < Object(data[key]).length; i++){
        //     tmpl_content(data[key][i], el, key);
        // }
    }
