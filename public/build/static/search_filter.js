document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("search-input");
    const languageFilter = document.getElementById("language-filter");
    const taskFilter = document.getElementById("task-filter");

    searchInput.addEventListener("input", applyFilters);
    languageFilter.addEventListener("change", applyFilters);
    taskFilter.addEventListener("change", applyFilters);

    function applyFilters() {
        const searchValue = searchInput.value.toLowerCase();
        const languageValue = languageFilter.value;
        const taskValue = taskFilter.value;

        const promptCards = document.querySelectorAll(".prompt-card");
        
        promptCards.forEach((card) => {
            const title = card.querySelector(".prompt-title").innerText.toLowerCase();
            const language = card.getAttribute("data-language");
            const task = card.getAttribute("data-task");
            
            const shouldDisplay =
                (searchValue === "" || title.includes(searchValue)) &&
                (languageValue === "" || language === languageValue) &&
                (taskValue === "" || task === taskValue);
                
        card.style.display = shouldDisplay ? "block" : "none";
    });
}
});