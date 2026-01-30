document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('searchInput');
    const cityFilter = document.getElementById('cityFilter');
    const cards = document.querySelectorAll('.house-card');

    function filterHouses() {
        const text = searchInput.value.toLowerCase();
        const city = cityFilter.value;

        cards.forEach(card => {
            const title = card.querySelector('.card-title').innerText.toLowerCase();
            const location = card.getAttribute('data-city');
            const district = card.querySelector('.card-location').innerText.toLowerCase();

            let matchesText = title.includes(text) || district.includes(text);
            let matchesCity = city === 'all' || location === city;

            if (matchesText && matchesCity) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    }

    if(searchInput) searchInput.addEventListener('input', filterHouses);
    if(cityFilter) cityFilter.addEventListener('change', filterHouses);
});
