document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const submitButton = form.querySelector("button");
    const fileInput = form.querySelector("input[type='file']");
    const spinner = document.createElement("div");

    // Spinner styles
    spinner.className = "spinner";
    spinner.innerHTML = `
        <div class="loadingio-spinner-dual-ball-9b3jh8ff4do">
            <div class="ldio-r6zo1swsh5">
                <div></div><div></div><div></div>
            </div>
        </div>
    `;
    spinner.style.display = "none"; // Initially hide the spinner
    form.appendChild(spinner); // Add the spinner to the form

    // Show the spinner when form is submitted
    form.addEventListener("submit", function() {
        submitButton.style.display = "none"; // Hide the button
        fileInput.style.display = "none"; // Hide the file input
        spinner.style.display = "block"; // Show the spinner
    });
});