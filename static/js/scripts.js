/*!
* Start Bootstrap - Clean Blog v6.0.5 (https://startbootstrap.com/theme/clean-blog)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-clean-blog/blob/master/LICENSE)
*/
window.addEventListener('DOMContentLoaded', async () => {
    const response = await fetch("http://localhost:8080/config", { 
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({})
    });
    const defaults = await response.json();
    const usedornewSelectElement = document.getElementById("usedornew");
    const stateSelectElement = document.getElementById("state");
    const brandSelectElement = document.getElementById("brand");
    const modelSelectElement = document.getElementById("model");
    const bodySelectElement = document.getElementById("bodytype");
    const driveSelectElement = document.getElementById("drivetype");
    const fuelSelectElement = document.getElementById("fueltype");
    const transSelectElement = document.getElementById("transmission");
    const cylindersSelectElement = document.getElementById("cylinders");
    const dispSelectElement = document.getElementById("displacement");
    const consSelectElement = document.getElementById("fuelconsumption");

    // Brand selector
    brandSelectElement.innerHTML += defaults.Brand.map(b => `<option value=${b}>${b}</option>`).join("");

    // Used or new selector
    usedornewSelectElement.innerHTML += defaults.UsedOrNew.map(b => `<option value=${b}>${b}</option>`).join("");

    // state selector
    stateSelectElement.innerHTML += defaults.State.map(b => `<option value=${b}>${b}</option>`).join("");

    // Model selector
    brandSelectElement.addEventListener("change", async () => {
        const value = brandSelectElement.value;
        if (!value || value.length == 0) return;

        const response = await fetch("http://localhost:8080/config", { 
            method: "POST",
            headers: {
              "Content-Type": "application/json"
            },
            body: JSON.stringify({ "Brand": value })
          });
          const options = await response.json();
          modelSelectElement.innerHTML = "<option selected>Please select a model</option>";
          modelSelectElement.innerHTML += options.choices.Model.map(m => `<option value=${m}>${m}</option>`).join("");
    });

// Body type selector
    modelSelectElement.addEventListener("change", async () => {
        const value = modelSelectElement.value;
        if (!value || value.length == 0) return;
        const response = await fetch("http://localhost:8080/config", { 
            method: "POST",
            headers: {
              "Content-Type": "application/json"
            },
            body: JSON.stringify({ "Model": value })
          });
          const options = await response.json();
          bodySelectElement.innerHTML = "<option selected>Please select a body type</option>";
          bodySelectElement.innerHTML += options.choices.BodyType.map(m => `<option value=${m}>${m}</option>`).join("");

    });

// Drive type selector
    bodySelectElement.addEventListener("change", async () => {
        const value =  bodySelectElement.value;
        const value2 = modelSelectElement.value;
        if (!value2 || value2.length == 0) return;
        const response = await fetch("http://localhost:8080/config", { 
            method: "POST",
            headers: {
              "Content-Type": "application/json"
            },
            body: JSON.stringify({ "Model": value2,
                                        "BodyType": encodeURIComponent(value) })
          });

          const options = await response.json();
          driveSelectElement.innerHTML = "<option selected>Please select a drive type</option>";
          driveSelectElement.innerHTML += options.choices.DriveType.map(m => `<option value=${m}>${m}</option>`).join("");

    });

// Fuel type selector
    driveSelectElement.addEventListener("change", async () => {
        const value = driveSelectElement.value;
        const value2 = modelSelectElement.value;
        const value3 = bodySelectElement.value;
        if (!value3 || value3.length == 0) return;
        const response = await fetch("http://localhost:8080/config", { 
            method: "POST",
            headers: {
            "Content-Type": "application/json"
            },
            body: JSON.stringify({ "DriveType": value,
                                        "Model": value2,
                                        "BodyType": value3 })
        });
        const options = await response.json();
        fuelSelectElement.innerHTML = "<option selected>Please select a fuel type</option>";
        fuelSelectElement.innerHTML += options.choices.FuelType.map(m => `<option value=${m}>${m}</option>`).join("");

    });

    // Transmission type selector
    fuelSelectElement.addEventListener("change", async () => {
        const value = driveSelectElement.value;
        const value2 = modelSelectElement.value;
        const value3 = bodySelectElement.value;
        const value4 = fuelSelectElement.value;
        if (!value4 || value4.length == 0) return;
        const response = await fetch("http://localhost:8080/config", { 
            method: "POST",
            headers: {
            "Content-Type": "application/json"
            },
            body: JSON.stringify({ "DriveType": value,
                                        "Model": value2,
                                        "BodyType": value3,
                                        "FuelType": value4 })
        });
        const options = await response.json();
        transSelectElement.innerHTML = "<option selected>Please select a transmission type</option>";
        transSelectElement.innerHTML += options.choices.Transmission.map(m => `<option value=${m}>${m}</option>`).join("");

    });

    // Cylinder count selector
    transSelectElement.addEventListener("change", async () => {
        const value = driveSelectElement.value;
        const value2 = modelSelectElement.value;
        const value3 = bodySelectElement.value;
        const value4 = fuelSelectElement.value;
        const value5 = transSelectElement.value;
        if (!value5 || value5.length == 0) return;
        const response = await fetch("http://localhost:8080/config", { 
            method: "POST",
            headers: {
            "Content-Type": "application/json"
            },
            body: JSON.stringify({ "DriveType": value,
                                        "Model": value2,
                                        "BodyType": value3,
                                        "FuelType": value4,
                                        "Transmission": value5 })
        });
        const options = await response.json();
        cylindersSelectElement.innerHTML = "<option selected>Please select the number of cylinders</option>";
        cylindersSelectElement.innerHTML += options.choices.CylindersinEngine.map(m => `<option value=${m}>${m}</option>`).join("");

    });

    // Displacement selector
    cylindersSelectElement.addEventListener("change", async () => {
        const value = driveSelectElement.value;
        const value2 = modelSelectElement.value;
        const value3 = bodySelectElement.value;
        const value4 = fuelSelectElement.value;
        const value5 = transSelectElement.value;
        const value6 = cylindersSelectElement.value;
        if (!value6 || value6.length == 0) return;
        const response = await fetch("http://localhost:8080/config", { 
            method: "POST",
            headers: {
            "Content-Type": "application/json"
            },
            body: JSON.stringify({ "DriveType": value,
                                        "Model": value2,
                                        "BodyType": value3,
                                        "FuelType": value4,
                                        "Transmission": value5,
                                        "CylindersinEngine": value6})
        });
        const options = await response.json();
        dispSelectElement.innerHTML = "<option selected>Please select the displacement</option>";
        dispSelectElement.innerHTML += options.choices["EngineDisplacement(L)"].map(m => `<option value=${m}>${m}</option>`).join("");

    });

    // Fuel consumption selector
    dispSelectElement.addEventListener("change", async () => {
        
        const value = driveSelectElement.value;
        const value2 = modelSelectElement.value;
        const value3 = bodySelectElement.value;
        const value4 = fuelSelectElement.value;
        const value5 = transSelectElement.value;
        const value6 = cylindersSelectElement.value;
        const value7 = dispSelectElement.value;
        if (!value7 || value7.length == 0) return;
        const response = await fetch("http://localhost:8080/config", { 
            method: "POST",
            headers: {
            "Content-Type": "application/json"
            },
            body: JSON.stringify({ "DriveType": value,
                                        "Model": value2,
                                        "BodyType": value3,
                                        "FuelType": value4,
                                        "Transmission": value5,
                                        "CylindersinEngine": value6,
                                        "EngineDisplacement(L)": value7})
        });
        const options = await response.json();
        
        consSelectElement.innerHTML = "<option selected>Please select the fuel consumption</option>";
        consSelectElement.innerHTML += options.choices["FuelConsumption(L)/100km"].map(m => `<option value=${m}>${m}</option>`).join("");

    });
    

    let scrollPos = 0;
    const mainNav = document.getElementById('mainNav');
    const headerHeight = mainNav.clientHeight;
    window.addEventListener('scroll', function() {
        const currentTop = document.body.getBoundingClientRect().top * -1;
        if ( currentTop < scrollPos) {
            // Scrolling Up
            if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-visible');
            } else {
                console.log(123);
                mainNav.classList.remove('is-visible', 'is-fixed');
            }
        } else {
            // Scrolling Down
            mainNav.classList.remove(['is-visible']);
            if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-fixed');
            }
        }
        scrollPos = currentTop;
    });
})

