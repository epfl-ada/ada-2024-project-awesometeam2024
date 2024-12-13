// Set up dimensions and margins
const margin = { top: 40, right: 20, bottom: 50, left: 70 };
const width = 600 - margin.left - margin.right;
const height = 400 - margin.top - margin.bottom;

// Select the SVG container
const svgContainer = d3.select("#chart_release_season")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom);

const svg = svgContainer.append("g")
    .attr("transform", `translate(${margin.left},${margin.top})`);

// Create a tooltip
const tooltip = d3.select(".tooltip");

// Zoom behavior
const zoom = d3.zoom()
    .scaleExtent([1, 5]) // Set zoom scale limits
    .translateExtent([[0, 0], [width + margin.left + margin.right, height + margin.top + margin.bottom]]) // Limit panning
    .on("zoom", (event) => {
        zoomableGroup.attr("transform", event.transform);
    });

// Add the zoom behavior to the SVG
svgContainer.call(zoom);

// Group everything inside a zoomable `g`
const zoomableGroup = svg.append("g");

// Load the data from the CSV file
d3.csv("assets/plots_data/chart_release_season.csv").then(data => {
    // Parse the data (convert strings to numbers)
    data.forEach(d => {
        d.mean = +d.mean; // Convert mean to number
        d.sem = +d.sem;   // Convert standard error to number
    });

    // Set up scales
    const x = d3.scaleBand()
        .domain(data.map(d => d.release_season))
        .range([0, width])
        .padding(0.1);

    const y = d3.scaleLinear()
        .domain([0, d3.max(data, d => d.mean + d.sem)]) // Include error bars in range
        .nice()
        .range([height, 0]);

    // Add x-axis
    zoomableGroup.append("g")
        .attr("transform", `translate(0,${height})`)
        .call(d3.axisBottom(x))
        .selectAll("text")
        .attr("transform", "rotate(-45)")
        .style("text-anchor", "end");

    // Add y-axis
    zoomableGroup.append("g")
        .call(d3.axisLeft(y));

    // Add bars
    zoomableGroup.selectAll(".bar")
        .data(data)
        .enter()
        .append("rect")
        .attr("class", "bar")
        .attr("x", d => x(d.release_season))
        .attr("y", d => y(d.mean))
        .attr("width", x.bandwidth())
        .attr("height", d => height - y(d.mean))
        .style("fill", "steelblue")
        .on("mouseover", (event, d) => {
            tooltip.style("visibility", "visible")
                .html(`<strong>Season:</strong> ${d.release_season}<br>
                       <strong>Mean:</strong> ${d.mean}<br>
                       <strong>SEM:</strong> ${d.sem}`)
                .style("top", `${event.pageY - 10}px`)
                .style("left", `${event.pageX + 10}px`);
            d3.select(event.target).style("fill", "orange");
        })
        .on("mousemove", (event) => {
            tooltip.style("top", `${event.pageY - 10}px`)
                .style("left", `${event.pageX + 10}px`);
        })
        .on("mouseout", (event) => {
            tooltip.style("visibility", "hidden");
            d3.select(event.target).style("fill", "steelblue");
        });

    // Add error bars
    zoomableGroup.selectAll(".error-line")
        .data(data)
        .enter()
        .append("line")
        .attr("class", "error-line")
        .attr("x1", d => x(d.release_season) + x.bandwidth() / 2)
        .attr("x2", d => x(d.release_season) + x.bandwidth() / 2)
        .attr("y1", d => y(d.mean + d.sem))
        .attr("y2", d => y(d.mean - d.sem))
        .style("stroke", "red")
        .style("stroke-width", "1.5px");
}).catch(error => {
    console.error("Error loading the data: ", error);
});
