function orderResultMessage(s) {
  document.getElementById("result-order").innerHTML = s;
}
function subResultMessage(s) {
  document.getElementById("result-sub").innerHTML = s;
}

const order_options = {
    style: {
      shape: "rect",
      layout: "vertical",
      color: "gold",
      label: "paypal",
    },
    message: {
      amount: 0,
    } ,
    async createOrder() {
      try {
        const response = await fetch("/api/order-create", {
          method: "POST",
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify({id: "some-digital-good"}),
        });

        const orderData = await response.json();

        if (orderData.id) {
          return orderData.id;
        }
        const errorDetail = orderData?.details?.[0];
        const errorMessage = errorDetail
          ? `${errorDetail.issue} ${errorDetail.description} (${orderData.debug_id})`
          : JSON.stringify(orderData);

        throw new Error(errorMessage);
      } catch (error) {
        console.error(error);
        orderResultMessage(`Could not initiate PayPal Checkout...<br><br>${error}`);
      }
    } ,
    async onApprove(data, actions) {
      try {
        const response = await fetch(`/api/order-capture/${data.orderID}`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
        });

        const orderData = await response.json();
        // Three cases to handle:
        //   (1) Recoverable INSTRUMENT_DECLINED -> call actions.restart()
        //   (2) Other non-recoverable errors -> Show a failure message
        //   (3) Successful transaction -> Show confirmation or thank you message

        const errorDetail = orderData?.details?.[0];

        if (errorDetail?.issue === "INSTRUMENT_DECLINED") {
          // (1) Recoverable INSTRUMENT_DECLINED -> call actions.restart()
          // recoverable state, per
          // https://developer.paypal.com/docs/checkout/standard/customize/handle-funding-failures/
          return actions.restart();
        } 
        setup_sub();
        if (errorDetail) {
          // (2) Other non-recoverable errors -> Show a failure message
          throw new Error(`${errorDetail.description} (${orderData.debug_id})`);
        } else if (!orderData.purchase_units) {
          throw new Error(JSON.stringify(orderData));
        } else {
          // (3) Successful transaction -> Show confirmation or thank you message
          // Or go to another URL:  actions.redirect('thank_you.html');
          const transaction =
            orderData?.purchase_units?.[0]?.payments?.captures?.[0] ||
            orderData?.purchase_units?.[0]?.payments?.authorizations?.[0];
          orderResultMessage(
            `Transaction ${transaction.status}: ${transaction.id}<br>
          <br>See console for all available details`
          );
          console.log(
            "Capture result",
            orderData,
            JSON.stringify(orderData, null, 2)
          );
        }
      } catch (error) {
        console.error(error);
        orderResultMessage(
          `Sorry, your transaction could not be processed...<br><br>${error}`
        );
      }
    } ,
    onCancel: function(data) {
      setup_sub();
    },
  };

const sub_options = {
    createSubscription(data, actions) {
          return actions.subscription.create({
              "plan_id": document.getElementById("sub-plan-id").value
          });
      },
    onApprove(data) {
        subResultMessage(`You have successfully created subscription ${data.subscriptionID}`);
    },
    onCancel(data) {
        subResultMessage(`You have successfully cancelled subscription ${data.subscriptionID}`);
    }
  };

function setup_order(){
  document.getElementById("paypal-button-order").innerHTML = "";
  window.paypal_one_time.Buttons(order_options).render("#paypal-button-order"); 
}

function setup_sub(){
  document.getElementById("paypal-button-sub").innerHTML = "";
  window.paypal_subscriptions.Buttons(sub_options).render("#paypal-button-sub"); 
}

setup_order();
setup_sub();
