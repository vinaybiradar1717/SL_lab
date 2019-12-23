var models = [
    {
        name: "honda",
        price: 123450,
        year: 2012
    },
    {
        name: "maruti",
        price: 456410,
        year: 2019
    },
    {
        name: "toyota",
        price: 784550,
        year: 2011
    }
]


function Product_1(){
    document.getElementById("product").innerHTML = 
    ` <table>
    <tr>
        <th>Name</th>
        <th>Price</th>
        <th>Year</th>
    </tr>
    <tr>
        <td>${models[0].name}</td>
        <td>${models[0].price}</td>
        <td>${models[0].year}</td>
    </tr>
</table>`;
}
function Product_2(){
    document.getElementById("product").innerHTML = 
    ` <table>
    <tr>
        <th>Name</th>
        <th>Price</th>
        <th>Year</th>
    </tr>
    <tr>
        <td>${models[1].name}</td>
        <td>${models[1].price}</td>
        <td>${models[1].year}</td>
    </tr>
</table>`;
}
function Product_3(){
    document.getElementById("product").innerHTML = 
    ` <table>
    <tr>
        <th>Name</th>
        <th>Price</th>
        <th>Year</th>
    </tr>
    <tr>
        <td>${models[2].name}</td>
        <td>${models[2].price}</td>
        <td>${models[2].year}</td>
    </tr>
</table>`;
}