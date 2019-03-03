const sortObject = (obj) => {
    return Object.keys(obj).sort().reduce(function (result, key) {
        result[key] = obj[key];
        return result;
    }, {});
}
var dataOdering = sortObject(data);

for (var key in dataOdering) {
    for( var i = 0; i < Object(data[key]).length; i++){
        let img = `${dataOdering[key][i].path}/thumb.png`;
        let name = dataOdering[key][i].name;
        tmp(img, name, key, i)
    }
}
