const carDataUrl = '/car'

d3.json(carDataUrl).then(function(response) {

    console.log(response)

    var carData = response["vehicles on lot"]

    // Use D3 to select the table body from the page
    var tbody = d3.select("tbody");

    // populate the table with rows
    for(let i = 0 ; i < carData.length; i++){

    var row = tbody.append("tr");

    row.append("td").text(carData[i]['VIN']);

    row.append("td").text(carData[i]['make']);

    row.append("td").text(carData[i]['model']);

    row.append("td").text(carData[i]['sticker price']);

    row.append("td").text(carData[i]['color']);

    row.append("td").text(carData[i]['manufacture date']);
    }



  });