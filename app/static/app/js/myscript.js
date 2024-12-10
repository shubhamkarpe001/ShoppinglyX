$('#slider1, #slider2, #slider3,#slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

$('.plus-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]; // Get the quantity element
    $.ajax({
        type: "GET",
        url: "/pluscart",
        data: {
            prod_id: id
        },
        success: function(data) {
            eml.innerText = data.quantity; 
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerText = data.totalamount// Update the quantity displayed
            // Optionally, update the total amount displayed as well
        }
    })
})

$('.minus-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]; // Get the quantity element
    $.ajax({
        type: "GET",
        url: "/minuscart",
        data: {
            prod_id: id
        },
        success: function(data) {
            eml.innerText = data.quantity;
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerText = data.totalamount // Update the quantity displayed
            // Optionally, update the total amount displayed as well
        }
    })
})

// $('.remove-cart').click(function () {
//     console.log("Inside the ajax")
//     var id = $(this).attr("pid").toString();
//     var eml = this
//     console.log(id)
//      // Get the quantity element
//     $.ajax({
//         type: "GET",
//         url: "/removecart",
//         data: {
//             prod_id: id
//         },
//         success: function(data) {
//             document.getElementById("amount").innerText = data.amount
//             document.getElementById("totalamount").innerText = data.totalamount // Update the quantity displayed
//             // Optionally, update the total amount displayed as well
//         }
//     })
// })

// $('.remove-cart').click(function (e) {
//     e.preventDefault(); // Prevent the default anchor behavior
//     var id = $(this).attr("pid").toString();
    
//     $.ajax({
//         type: "GET",
//         url: "/removecart", // Ensure this URL points to your remove_cart view
//         data: {
//             prod_id: id
//         },
//         success: function(data) {
//             // Update the cart display with the new amounts
//             document.getElementById("amount").innerText = data.amount;
//             document.getElementById("totalamount").innerText = data.totalamount;
//             // Optionally, remove the cart item from the DOM
//             // $(this).closest('.cart-item-selector').remove(); // Change '.cart-item-selector' to the correct class
//         },
//         error: function(xhr) {
//             alert('Error removing item: ' + xhr.responseText);
//         }
//     });
// });

$('.remove-cart').click(function (e) {
    console.log(":This is the ajax function")
    e.preventDefault(); // Prevent the default link behavior
    var id = $(this).attr("pid").toString();
    
    $.ajax({
        type: "GET",
        url: "/removecart", // Ensure this matches your URL pattern
        data: {
            prod_id: id
        },
        success: function(data) {
            // Optionally, update the cart display with the new amounts
            // Here you may need to adjust how you handle the data response
        },
        error: function(xhr) {
            alert('Error removing item: ' + xhr.responseText);
        }
    });
});


