/*
Original implementation by @Waaaaghh (https://github.com/Waaaaghh)
Adapted/Modified by @dawnandrew100 (https://github.com/dawnandrew100)
*/
const titles = {
bdo: "Bottom dissolved oxygen (mg/L)",
wt: "Water temperature (°F)",
sec: "Secchi depth (m)",
sal: "Salinity (ppt)",
ph: "pH",
};

const data = window.bayData
console.log("Maryland Chesapeake Bay Data loaded:", data)
const stations = Object.keys(data);
const params = Object.keys(data[stations[0]]);
const months = Object.keys(data[stations[0]][params[0]]);

function createChartContainer(param) {
const container = document.createElement("div");
container.className = "chart-container";

const canvas = document.createElement("canvas");
canvas.id = param;

const title = document.createElement("h3");
title.innerText = titles[param];

container.append(title);
container.appendChild(canvas);
document.getElementById("charts").appendChild(container);
}

function renderChart(param) {
createChartContainer(param);

const columns = ["Minimum", "Maximum", "Mean"].map((column) => {
    return months.map((month) => {
    const stationValues = stations
        .map((station) => data[station][param][month][column])
        .filter((val) => val !== "Not Sampled")
        .map((val) => Number(val));

    if (stationValues.length > 0) {
        const avg =
        stationValues.reduce((a, b) => a + b, 0) / stationValues.length;
        return avg;
    } else {
        return 0; // probably should filter it out
    }
    });
});

new Chart(document.getElementById(param), {
    type: "line",
    data: {
    labels: months,
    datasets: [
        {
        label: "Minimum",
        data: columns[0],
        borderWidth: 1,
        fill: "+1",
        },
        {
        label: "Maximum",
        data: columns[1],
        borderWidth: 1,
        },
        {
        label: "Mean",
        data: columns[2],
        borderWidth: 1,
        },
    ],
    },
    // options: {
    //   scales: {
    //     y: {
    //       beginAtZero: true,
    //     },
    //   },
    // },
});
}

params.forEach((param) => {
renderChart(param);
});
