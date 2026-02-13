if (typeof weatherCondition !== "undefined") {

    if (weatherCondition.includes("Cloud")) {
        document.body.style.background =
            "linear-gradient(135deg, #bdc3c7, #2c3e50)";
    }
    else if (weatherCondition.includes("Rain")) {
        document.body.style.background =
            "linear-gradient(135deg, #00c6fb, #005bea)";
    }
    else if (weatherCondition.includes("Clear")) {
        document.body.style.background =
            "linear-gradient(135deg, #fceabb, #f8b500)";
    }
    else if (weatherCondition.includes("Snow")) {
        document.body.style.background =
            "linear-gradient(135deg, #e6dada, #274046)";
    }
}
