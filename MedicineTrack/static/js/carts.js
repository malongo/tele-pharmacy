var medicine_number = document.getElementById("medicine_number");
var total_price = document.getElementById("total-price");
var updateBtnCart = document.getElementsByClassName("btn-cart");
var updateBtnCart_real = document.getElementsByClassName("btn-cart-real");

for (i = 0; i < updateBtnCart.length; i++) {
    updateBtnCart[i].addEventListener("click", function() {
        var action = this.dataset.action;
        var item = medicine_number.dataset.item;
        if (action == "add") {
            var medicine_num = Number(medicine_number.value);
            medicine_num += 1;
            medicine_number.value = medicine_num;
            total_price.innerHTML =
                total_price.dataset.price * Number(medicine_number.value).toFixed(2);
        } else if (action == "remove") {
            var medicine_num = Number(medicine_number.value);
            medicine_num -= 1;
            medicine_number.value = medicine_num;
            total_price.innerHTML = (
                total_price.dataset.price * Number(medicine_number.value)
            ).toFixed(2);
        }
    });
}

for (i = 0; i < updateBtnCart_real.length; i++) {
    updateBtnCart_real[i].addEventListener("click", function() {
        var action = this.dataset.action;
        var medicineId = this.dataset.medicine;
        var medicineQt = Number(medicine_number.value);

        if (action == "addCart") {
            if (medicineQt >= 1) {
                updateUserOrder(medicineId, action, medicineQt);
            } else {
                render_error();
            }
        } else if (action == "removeCart") {
            if (medicineQt >= 1) {
                updateUserOrder(medicineId, action, medicineQt);
            }
        } else if (action == "removeAll") {
            updateUserOrder(medicineId, action, medicineQt);
        }
    });
}

var render_error = () => {
    setTimeout(() => {
        location.reload();
    }, 2000);
    document.getElementById("error_shopping").innerHTML = `
    <div class="alert alert-info">
    <h3 class="m-3 text-info ">Your Not Specify Quantity
        <button type="button" class="close" data-dismiss="alert" aria-label="Close" style="border:none; float:right" id="Close">
            <span aria-hidden="true">
              <img src="{% static 'images/icons/x w-3.png'%}" alt="" width="20" height="20"> 
            </span>
          </button>
    </h3>
</div>
    `;
};
var render = () => {
    document.getElementById("error_shopping").innerHTML = `
    <div class="alert alert-info">
      <div class="text-align-center bg-clr-teal flex">
          <h3 class="text-clr-white">LOGIN OR CREATE ACCOUNT </h3>
          <a href="{{request.META.HTTP_REFERER}}" class="cat-link btn-2-shop">&#x2190;Back</a>
      </div>
      <div class="login my-5 mx-auto bg-purple">

          <div class="text-align-center bg-clr-teal">
              <h3 class="text-clr-white">TELE-PHARMACY</h3>
          </div>
          <form method="POST" action="{% url 'MedicineTrack:login' %}">
              {% csrf_token %} {{form.as_p}}
              <input type="submit" value="Login">
          </form>
          Don't have an account? <a href="{% url 'MedicineTrack:register' %}"><strong>register here</strong></a>!
      </div>
      
    </div>
      `;
};
var medicine_qty = () => {
    var medicine_num = Number(medicine_number.value);
    medicine_num -= 1;
    medicine_number.value = medicine_num;
    total_price.innerHTML = (
        total_price.dataset.price * Number(medicine_number.value)
    ).toFixed(2);
};

function updateUserOrder(medicineId, action, medicineQt) {
    var url = "/update_item/";
    fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken
            },
            body: JSON.stringify({
                medicineId: medicineId,
                action: action,
                medicineQt: medicineQt
            })
        })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            // alert(data + " " + medicineQt);
            location.reload();
        });
}